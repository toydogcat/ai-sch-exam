<script setup>
import { ref, computed, watch, onMounted, nextTick } from 'vue'
import { withBase } from 'vitepress'

const allQuestions = ref([])
const drawnQuestions = ref([])
const userAnswers = ref({})
const isSubmitted = ref(false)
const isLoading = ref(true)
const loadError = ref('')

// Modes: 'setup' | 'test' | 'result'
const currentMode = ref('setup')

// Sub-modes: 'mock' (大考) | 'mini' (小考)
const examMode = ref('mock')

// Sliders counts
const choiceCount = ref(5)
const fillCount = ref(5)

const availableChapters = ref([]) // Raw section names

// Dynamic chapters for Mock mode extracted from all raw questions
const availableExamChapters = computed(() => {
  const set = new Set()
  allQuestions.value.forEach(q => {
    if (q.chapter) {
      const chKey = q.chapter.split(' ')[0]
      if (chKey) set.add(chKey)
    }
  })
  return Array.from(set).sort()
})

const selectedExamChapters = ref(['Ch0', 'Ch1', 'Ch2', 'Ch3', 'Ch4', 'Ch5', 'Ch6', 'Ch7', 'Ch8', 'Ch9', 'Ch10', 'Ch11', 'Ch12', 'Ch13', 'Ch14', 'Ch15', 'Ch16'])

// Mini mode selections
const selectedMiniChapter = ref('Ch1')
const selectedMiniSections = ref([])

const chapterLabels = {
  'Ch0': '第 0 章：先備知識與函數',
  'Ch1': '第 1 章：極限與連續',
  'Ch2': '第 2 章：導數與微分',
  'Ch3': '第 3 章：微分的應用',
  'Ch4': '第 4 章：積分',
  'Ch5': '第 5 章：積分的應用',
  'Ch6': '第 6 章：反函數與超越函數',
  'Ch7': '第 7 章：進階積分技巧與方法',
  'Ch8': '第 8 章：進階積分應用',
  'Ch9': '第 9 章：微分方程',
  'Ch10': '第 10 章：參數方程與極坐標',
  'Ch11': '第 11 章：無窮序列與級數',
  'Ch12': '第 12 章：向量與空間幾何',
  'Ch13': '第 13 章：向量函數',
  'Ch14': '第 14 章：偏導數',
  'Ch15': '第 15 章：重積分',
  'Ch16': '第 16 章：向量微積分'
}

// Filter raw sections belonging to selectedMiniChapter
const availableMiniSections = computed(() => {
  return availableChapters.value.filter(sec => sec.startsWith(selectedMiniChapter.value))
})

// Automatically populate mini section selections when mini chapter changes
watch(selectedMiniChapter, (newCh) => {
  selectedMiniSections.value = availableChapters.value.filter(sec => sec.startsWith(newCh))
}, { immediate: true })

// Score calculation
const score = computed(() => {
  if (!isSubmitted.value) return 0
  let totalScore = 0
  let earnedScore = 0

  drawnQuestions.value.forEach((q, idx) => {
    totalScore += 10
    const userAns = userAnswers.value[idx]
    const correctAns = q.answer

    if (q.type === 'single') {
      const u = (userAns || '').toString().toUpperCase().trim()
      const c = (correctAns || '').toString().toUpperCase().trim()
      const map = { 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6 }
      
      if (u === c || map[u] == correctAns || u == map[c]) {
        earnedScore += 10
      }
    } else if (q.type === 'fill') {
      const u = (userAnswers.value[idx] || '').toString().trim().toLowerCase()
      const c = (correctAns || '').toString().trim().toLowerCase()
      if (u === c) {
        earnedScore += 10
      }
    }
  })

  return totalScore === 0 ? 0 : Math.round((earnedScore / totalScore) * 100)
})

const fetchBank = async () => {
  isLoading.value = true
  loadError.value = ''
  try {
    const chaptersToLoad = ['ch0', 'ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8', 'ch9', 'ch10', 'ch11', 'ch12', 'ch13', 'ch14', 'ch15', 'ch16']
    let combinedQuestions = []
    
    for (const ch of chaptersToLoad) {
      try {
        const res = await fetch(withBase(`/json/calculus_bank_${ch}.json`))
        if (res.ok) {
          const data = await res.json()
          combinedQuestions = combinedQuestions.concat(data.questions || [])
        }
      } catch (e) {
        console.warn(`無法讀取題庫 ${ch}:`, e)
      }
    }
    
    if (combinedQuestions.length === 0) {
      throw new Error('無法讀取任何題庫資料')
    }
    
    allQuestions.value = combinedQuestions
    
    const chapters = new Set()
    allQuestions.value.forEach(q => {
      if (q.chapter) chapters.add(q.chapter)
    })
    availableChapters.value = Array.from(chapters).sort()

    // Pre-select mock exam chapters
    const examChapters = new Set()
    allQuestions.value.forEach(q => {
      if (q.chapter) {
        const chKey = q.chapter.split(' ')[0]
        if (chKey) examChapters.add(chKey)
      }
    })
    selectedExamChapters.value = Array.from(examChapters).sort()

    // Pre-select mini sections
    selectedMiniSections.value = availableChapters.value.filter(sec => sec.startsWith(selectedMiniChapter.value))
  } catch (err) {
    console.error(err)
    loadError.value = `題庫載入失敗：${err.message}`
  } finally {
    isLoading.value = false
  }
}

// Draw logic
const drawQuestions = () => {
  userAnswers.value = {}
  isSubmitted.value = false

  let pool = []
  if (examMode.value === 'mock') {
    pool = allQuestions.value.filter(q => {
      if (!q.chapter) return false
      const chKey = q.chapter.split(' ')[0]
      return selectedExamChapters.value.includes(chKey)
    })
  } else {
    pool = allQuestions.value.filter(q => selectedMiniSections.value.includes(q.chapter))
  }

  const choicesPool = pool.filter(q => q.type === 'single')
  const fillPool = pool.filter(q => q.type === 'fill')

  const shuffle = (arr) => arr.sort(() => 0.5 - Math.random())

  const selectedChoices = shuffle(choicesPool).slice(0, choiceCount.value)
  const selectedFill = shuffle(fillPool).slice(0, fillCount.value)

  drawnQuestions.value = [...selectedChoices, ...selectedFill]

  if (drawnQuestions.value.length === 0) {
    alert('請確認抽題條件，目前符合條件的題目為 0。')
    return
  }

  currentMode.value = 'test'

  nextTick(() => {
    if (typeof window !== 'undefined' && window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise().catch(() => {})
    }
  })
}

const submitQuiz = () => {
  isSubmitted.value = true
  currentMode.value = 'result'
  window.scrollTo({ top: 0, behavior: 'smooth' })
  nextTick(() => {
    if (typeof window !== 'undefined' && window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise().catch(() => {})
    }
  })
}

const resetSetup = () => {
  currentMode.value = 'setup'
  drawnQuestions.value = []
  userAnswers.value = {}
  isSubmitted.value = false
}

const handleChoiceCountChange = () => {
  if (choiceCount.value + fillCount.value > 10) {
    fillCount.value = 10 - choiceCount.value
  }
}

const handleFillCountChange = () => {
  if (choiceCount.value + fillCount.value > 10) {
    choiceCount.value = 10 - fillCount.value
  }
}

onMounted(() => {
  fetchBank()
})
</script>

<template>
  <div class="calculus-quiz">
    <!-- Header/Hero Banner -->
    <div class="quiz-banner">
      <div class="banner-badge">📚 題庫隨機抽題</div>
      <h1>微積分線上測驗系統</h1>
      <p>自訂抽題模式：支援手機瀏覽與動態 MathJax 數學算式渲染。</p>
    </div>

    <!-- Error State -->
    <div v-if="loadError && !isLoading" class="error-card">
      <p>{{ loadError }}</p>
      <button @click="fetchBank" class="retry-action-btn">重新載入</button>
    </div>

    <!-- Loading state -->
    <div v-else-if="isLoading" class="loading-card">
      <div class="spinner"></div>
      <p>正在載入題庫與章節資訊...</p>
    </div>

    <!-- Setup Mode Screen -->
    <div v-else-if="currentMode === 'setup'" class="setup-screen glass-card">
      <div class="setup-header">
        <h2>🔧 設定測驗條件</h2>
        <p>自訂想要抽取的題目總數與章節 (加起來最多 10 題)</p>
      </div>

      <!-- Mode Selection Segmented Tabs -->
      <div class="mode-tabs">
        <button 
          class="tab-btn" 
          :class="{ 'active': examMode === 'mock' }" 
          @click="examMode = 'mock'"
        >
          🏆 大考模式 (依章節)
        </button>
        <button 
          class="tab-btn" 
          :class="{ 'active': examMode === 'mini' }" 
          @click="examMode = 'mini'"
        >
          📝 小考模式 (依單一章內各節)
        </button>
      </div>

      <div class="setup-body">
        <!-- Mode 1: 大考模式 -->
        <div v-if="examMode === 'mock'" class="config-section">
          <label class="section-label">📚 選擇抽題章節：</label>
          <div class="chapter-grid">
            <label v-for="ch in availableExamChapters" :key="ch" class="checkbox-card" :class="{ 'is-checked': selectedExamChapters.includes(ch) }">
              <input type="checkbox" :value="ch" v-model="selectedExamChapters">
              <span class="custom-chk-lbl">{{ chapterLabels[ch] || ch }}</span>
            </label>
          </div>
        </div>

        <!-- Mode 2: 小考模式 -->
        <div v-else class="config-section">
          <div class="mini-selector-row">
            <label class="section-label">📚 選擇特定章節：</label>
            <select v-model="selectedMiniChapter" class="mini-select">
              <option v-for="ch in availableExamChapters" :key="ch" :value="ch">
                {{ chapterLabels[ch] || ch }}
              </option>
            </select>
          </div>

          <label class="section-label mt-4">📋 選擇抽題小節：</label>
          <div class="chapter-grid">
            <label v-for="sec in availableMiniSections" :key="sec" class="checkbox-card" :class="{ 'is-checked': selectedMiniSections.includes(sec) }">
              <input type="checkbox" :value="sec" v-model="selectedMiniSections">
              <span class="custom-chk-lbl">{{ sec.split('：')[1] || sec }}</span>
            </label>
          </div>
        </div>

        <!-- Limits Sliders/Counters -->
        <div class="config-grid">
          <div class="config-card">
            <div class="card-title">
              <span>🔘 選擇題題數</span>
              <span class="count-badge">{{ choiceCount }} 題</span>
            </div>
            <input type="range" v-model.number="choiceCount" min="0" max="10" @input="handleChoiceCountChange" class="slider">
          </div>

          <div class="config-card">
            <div class="card-title">
              <span>✏️ 填充題題數</span>
              <span class="count-badge">{{ fillCount }} 題</span>
            </div>
            <input type="range" v-model.number="fillCount" min="0" max="10" @input="handleFillCountChange" class="slider">
          </div>
        </div>
      </div>

      <div class="setup-footer">
        <button 
          @click="drawQuestions" 
          class="draw-btn" 
          :disabled="choiceCount + fillCount === 0 || (examMode === 'mock' && selectedExamChapters.length === 0) || (examMode === 'mini' && selectedMiniSections.length === 0)"
        >
          開始抽出題目 ({{ choiceCount + fillCount }} 題)
        </button>
      </div>
    </div>

    <!-- Test Mode Screen -->
    <div v-else class="test-screen">
      <div class="quiz-status-bar glass-card">
        <div class="status-left">
          <span class="total-status">進行中測驗：{{ drawnQuestions.length }} 題</span>
          <span class="status-meta">（選擇題：{{ drawnQuestions.filter(q => q.type === 'single').length }} 題，填充題：{{ drawnQuestions.filter(q => q.type === 'fill').length }} 題）</span>
        </div>
        <div class="status-right" v-if="currentMode === 'result'">
          <div class="score-pill">
            <span class="label">得分</span>
            <span class="val">{{ score }}</span>
          </div>
        </div>
      </div>

      <div class="questions-list">
        <div v-for="(q, idx) in drawnQuestions" :key="idx" class="q-card glass-card" :class="{ 'is-correct': currentMode === 'result' && (q.type === 'single' ? (userAnswers[idx] === q.answer) : (userAnswers[idx]?.toString().toLowerCase().trim() === q.answer.toString().toLowerCase().trim())), 'is-wrong': currentMode === 'result' && !(q.type === 'single' ? (userAnswers[idx] === q.answer) : (userAnswers[idx]?.toString().toLowerCase().trim() === q.answer.toString().toLowerCase().trim())) }">
          
          <div class="q-header">
            <div class="q-meta">
              <span class="q-badge" :class="q.type">{{ q.type === 'single' ? '選擇題' : '填充題' }}</span>
              <span class="chapter-badge">{{ q.chapter }}</span>
            </div>
            <span class="q-num">第 {{ idx + 1 }} 題</span>
          </div>

          <!-- Problem text -->
          <div class="q-content" v-html="q.text"></div>

          <!-- Choice Option Rendering -->
          <div v-if="q.type === 'single'" class="q-options">
            <label v-for="(opt, optIdx) in q.options" :key="optIdx" class="option-row" :class="{ 'selected': userAnswers[idx] === String.fromCharCode(65 + optIdx) }">
              <input type="radio" :name="'q_' + idx" :value="String.fromCharCode(65 + optIdx)" v-model="userAnswers[idx]" :disabled="currentMode === 'result'">
              <span class="opt-label">{{ String.fromCharCode(65 + optIdx) }}</span>
              <span class="opt-text" v-html="opt"></span>
            </label>
          </div>

          <!-- Fill-in Rendering -->
          <div v-else class="q-fill">
            <input type="text" v-model="userAnswers[idx]" class="fill-input" placeholder="請在此輸入答案..." :disabled="currentMode === 'result'">
          </div>

          <!-- Result Feedback Section -->
          <div v-if="currentMode === 'result'" class="q-feedback">
            <div class="fb-ans">
              <span>正確答案：</span>
              <strong class="correct-text">{{ q.answer }}</strong>
            </div>
            <div v-if="q.solution" class="fb-sol">
              <div class="sol-title">💡 詳細解析：</div>
              <div class="sol-text" v-html="q.solution"></div>
            </div>
          </div>

        </div>
      </div>

      <div class="test-footer">
        <button v-if="currentMode === 'test'" @click="submitQuiz" class="submit-action-btn">確認交卷</button>
        <button v-else @click="resetSetup" class="retry-action-btn">重新出題</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.calculus-quiz {
  max-width: 900px;
  margin: 1.5rem auto;
  padding: 0 1rem;
  font-family: 'Inter', -apple-system, sans-serif;
  color: var(--vp-c-text-1);
}

.quiz-banner {
  text-align: center;
  margin-bottom: 2.5rem;
}

.banner-badge {
  display: inline-block;
  padding: 6px 14px;
  background: rgba(245, 158, 11, 0.1);
  border: 1px solid rgba(245, 158, 11, 0.3);
  color: #f59e0b;
  font-size: 0.85rem;
  border-radius: 100px;
  font-weight: 700;
  margin-bottom: 0.75rem;
  letter-spacing: 0.05em;
}

.quiz-banner h1 {
  font-size: 2.6rem;
  font-weight: 800;
  color: var(--vp-c-text-1);
  margin: 0.5rem 0;
  background: linear-gradient(135deg, #f59e0b, #ec4899);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  letter-spacing: -0.02em;
  line-height: 1.3;
  padding: 4px 0;
}

.quiz-banner p {
  color: var(--vp-c-text-2);
  font-size: 1.05rem;
}

.glass-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 2rem;
  box-shadow: 0 15px 35px rgba(0,0,0,0.1);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  margin-bottom: 2rem;
}

.setup-screen {
  animation: fadeIn 0.4s ease;
}

.setup-header {
  margin-bottom: 2rem;
  text-align: center;
}

.setup-header h2 {
  font-size: 1.6rem;
  font-weight: 800;
  color: var(--vp-c-text-1);
  margin-bottom: 0.35rem;
  border: none;
}

.setup-header p {
  color: var(--vp-c-text-2);
  font-size: 0.95rem;
}

.mode-tabs {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.06);
  padding: 6px;
  border-radius: 14px;
}

.tab-btn {
  flex: 1;
  padding: 12px 18px;
  border-radius: 10px;
  border: none;
  font-weight: 700;
  font-size: 1.05rem;
  cursor: pointer;
  background: transparent;
  color: var(--vp-c-text-2);
  transition: all 0.3s;
}

.tab-btn:hover {
  background: rgba(255, 255, 255, 0.04);
}

.tab-btn.active {
  background: #f59e0b;
  color: #fff;
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.25);
}

.mini-selector-row {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}

.mini-select {
  width: 100%;
  padding: 12px 16px;
  border-radius: 12px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 1.05rem;
  color: var(--vp-c-text-1);
  outline: none;
  cursor: pointer;
  transition: all 0.3s;
}

.mini-select:focus {
  border-color: #f59e0b;
  box-shadow: 0 0 10px rgba(245, 158, 11, 0.1);
}

.mt-4 {
  margin-top: 1.25rem;
}

.config-section {
  margin-bottom: 1.75rem;
}

.section-label {
  font-weight: 700;
  font-size: 1.1rem;
  display: block;
  margin-bottom: 0.8rem;
}

.chapter-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1rem;
}

.checkbox-card {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding: 12px 16px;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.25s;
}

.checkbox-card:hover {
  background: rgba(245, 158, 11, 0.05);
  border-color: rgba(245, 158, 11, 0.4);
}

.checkbox-card.is-checked {
  background: rgba(245, 158, 11, 0.12);
  border-color: #f59e0b;
  color: #fff;
}

.custom-chk-lbl {
  font-size: 0.95rem;
  font-weight: 600;
}

.config-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-top: 1rem;
}

.config-card {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.card-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: 700;
}

.count-badge {
  background: var(--vp-c-bg-soft);
  padding: 4px 12px;
  border-radius: 100px;
  font-size: 0.85rem;
  color: var(--vp-c-text-2);
}

.slider {
  -webkit-appearance: none;
  width: 100%;
  height: 8px;
  border-radius: 10px;
  background: var(--vp-c-bg-soft);
  outline: none;
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #f59e0b;
  cursor: pointer;
  box-shadow: 0 0 10px rgba(245, 158, 11, 0.5);
  transition: all 0.1s;
}

.slider::-webkit-slider-thumb:hover {
  transform: scale(1.15);
}

.setup-footer {
  margin-top: 2.5rem;
  text-align: center;
}

.draw-btn {
  background: linear-gradient(135deg, #f59e0b, #d97706);
  color: #fff;
  font-size: 1.2rem;
  font-weight: 800;
  padding: 1rem 3rem;
  border-radius: 100px;
  border: none;
  cursor: pointer;
  transition: all 0.3s;
  box-shadow: 0 8px 20px rgba(245, 158, 11, 0.25);
}

.draw-btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 12px 30px rgba(245, 158, 11, 0.35);
}

.draw-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Status Bar */
.quiz-status-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.75rem;
  margin-bottom: 2rem;
  border-radius: 16px;
}

.status-left {
  display: flex;
  flex-direction: column;
}

.total-status {
  font-size: 1.1rem;
  font-weight: 800;
}

.status-meta {
  color: var(--vp-c-text-2);
  font-size: 0.85rem;
}

.score-pill {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  background: rgba(16, 185, 129, 0.15);
  border: 1px solid rgba(16, 185, 129, 0.3);
  padding: 6px 18px;
  border-radius: 100px;
}

.score-pill .label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #10b981;
}

.score-pill .val {
  font-size: 2rem;
  font-weight: 900;
  color: #10b981;
}

/* Questions List Styles */
.questions-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.q-card {
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  border-radius: 20px;
}

.q-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.q-meta {
  display: flex;
  gap: 0.6rem;
}

.q-badge {
  font-size: 0.75rem;
  padding: 3px 10px;
  border-radius: 100px;
  font-weight: 700;
}

.q-badge.single {
  background: rgba(59, 130, 246, 0.15);
  color: #3b82f6;
}

.q-badge.fill {
  background: rgba(139, 92, 246, 0.15);
  color: #8b5cf6;
}

.chapter-badge {
  font-size: 0.75rem;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  padding: 3px 10px;
  border-radius: 100px;
  font-weight: 600;
}

.q-num {
  font-weight: 800;
  color: #f59e0b;
}

.q-content {
  font-size: 1.15rem;
  line-height: 1.7;
}

.q-options {
  display: grid;
  gap: 0.65rem;
}

.option-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 12px 16px;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 14px;
  cursor: pointer;
  transition: all 0.2s;
}

.option-row:hover {
  border-color: rgba(245, 158, 11, 0.3);
  background: rgba(255,255,255,0.04);
}

.option-row.selected {
  background: rgba(245, 158, 11, 0.08);
  border-color: rgba(245, 158, 11, 0.6);
}

.opt-label {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255,255,255,0.06);
  font-weight: 800;
  font-size: 0.85rem;
  flex-shrink: 0;
}

.option-row.selected .opt-label {
  background: #f59e0b;
  color: #fff;
}

.option-row input {
  display: none;
}

.q-fill .fill-input {
  width: 100%;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  padding: 14px 18px;
  font-size: 1.05rem;
  color: var(--vp-c-text-1);
  outline: none;
  transition: all 0.3s;
}

.q-fill .fill-input:focus {
  border-color: #f59e0b;
  background: rgba(255,255,255,0.05);
  box-shadow: 0 0 10px rgba(245, 158, 11, 0.15);
}

/* Corrections result */
.q-card.is-correct {
  border-color: #10b981;
}

.q-card.is-wrong {
  border-color: #ef4444;
}

.q-feedback {
  margin-top: 1.25rem;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: 14px;
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.correct-text {
  color: #10b981;
  font-size: 1.15rem;
}

.sol-title {
  font-weight: 700;
  color: var(--vp-c-text-2);
  margin-bottom: 0.3rem;
}

.sol-text {
  color: var(--vp-c-text-1);
  line-height: 1.6;
}

.test-footer {
  text-align: center;
  margin-top: 3rem;
}

.submit-action-btn, .retry-action-btn {
  font-size: 1.15rem;
  font-weight: 700;
  padding: 0.85rem 2.5rem;
  border-radius: 50px;
  border: none;
  cursor: pointer;
  transition: all 0.3s;
}

.submit-action-btn {
  background: linear-gradient(135deg, #10b981, #059669);
  color: #fff;
  box-shadow: 0 6px 15px rgba(16, 185, 129, 0.2);
}

.submit-action-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(16, 185, 129, 0.35);
}

.retry-action-btn {
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
  box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}

.retry-action-btn:hover {
  transform: translateY(-2px);
  background: rgba(255,255,255,0.08);
}

.spinner {
  width: 32px;
  height: 32px;
  border: 4px solid var(--vp-c-bg-soft);
  border-top: 4px solid #f59e0b;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin-bottom: 0.8rem;
}

@keyframes spin { 100% { transform: rotate(360deg); } }
@keyframes fadeIn { 0% { opacity: 0; transform: translateY(10px); } }

@media (max-width: 768px) {
  .calculus-quiz { padding: 0 0.5rem; }
  .quiz-banner h1 { font-size: 2rem; }
  .glass-card { padding: 1.5rem; border-radius: 16px; }
}
</style>
