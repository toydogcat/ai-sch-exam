<script setup>
import { ref, computed, onMounted, watch, nextTick } from 'vue'
import { withBase, useRoute } from 'vitepress'

const route = useRoute()
const questions = ref([])
const userAnswers = ref({})
const isSubmitted = ref(false)
const isLoading = ref(false)
const examineeName = ref('')
const ticketNumber = ref('')
const timeLeft = ref(90 * 60)
const totalDuration = ref(90 * 60)
const examTitle = ref('')
let timer = null

const formatTime = computed(() => {
  const mins = Math.floor(timeLeft.value / 60)
  const secs = timeLeft.value % 60
  return `${mins}:${secs.toString().padStart(2, '0')}`
})

const fetchQuestions = async () => {
  const urlParams = new URLSearchParams(window.location.search)
  const path = urlParams.get('path')
  if (!path) return

  isLoading.value = true
  isSubmitted.value = false
  userAnswers.value = {}
  
  try {
    const res = await fetch(withBase(`/json/${path}.json`))
    if (!res.ok) throw new Error('Network response was not ok')
    const data = await res.json()
    
    examTitle.value = data.title || path.split('/').pop()
    
    if (Array.isArray(data)) {
      questions.value = data
    } else {
      questions.value = data.questions || []
      if (data.duration) {
        totalDuration.value = data.duration * 60
        timeLeft.value = totalDuration.value
      }
    }
    
    // Initialize userAnswers for multi-select (arrays)
    questions.value.forEach((q, idx) => {
      if (q.type === 'multi') {
        userAnswers.value[idx] = []
      }
    })
    
    startTimer()
  } catch (err) {
    console.error('Failed to fetch questions:', err)
  } finally {
    isLoading.value = false
  }
}

watch(questions, () => {
  if (typeof window !== 'undefined' && window.MathJax) {
    nextTick(() => {
      window.MathJax.typesetPromise().catch(err => console.log('MathJax typeset failed: ', err))
    })
  }
})

const startTimer = () => {
  if (timer) clearInterval(timer)
  timer = setInterval(() => {
    if (timeLeft.value > 0 && !isSubmitted.value) {
      timeLeft.value--
    } else if (timeLeft.value === 0 && !isSubmitted.value) {
      submitExam()
      clearInterval(timer)
    }
  }, 1000)
}

const getAnswerValue = (ans) => {
  if (Array.isArray(ans)) return ans.map(a => getAnswerValue(a))
  if (typeof ans === 'number') return ans
  if (typeof ans === 'string') {
    const map = { 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6 }
    return map[ans.toUpperCase()] || ans
  }
  return ans
}

const score = computed(() => {
  if (!isSubmitted.value) return 0
  let totalScore = 0
  let earnedScore = 0
  
  questions.value.forEach((q, idx) => {
    const questionScore = q.score || 2
    totalScore += questionScore
    
    const correctAns = getAnswerValue(q.answer)
    const userAns = userAnswers.value[idx]

    if (q.type === 'multi') {
      // Simple multi-select check: must match exactly
      const u = (userAns || []).sort().join(',')
      const c = (correctAns || []).sort().join(',')
      if (u === c) earnedScore += questionScore
    } else if (q.options && q.options.length) {
      // Single Choice
      if (userAns == correctAns) {
        earnedScore += questionScore
      }
    } else if (q.type === 'fill_in') {
      const u = (userAns || '').toString().trim()
      const c = (q.answer || '').toString().trim()
      if (u === c) earnedScore += questionScore
    }
  })
  
  return totalScore === 0 ? 0 : Math.round((earnedScore / totalScore) * 100)
})

onMounted(() => {
  fetchQuestions()
  ticketNumber.value = 'SCH-' + Math.random().toString(36).substr(2, 9).toUpperCase()
})

// Watch for route query changes to re-fetch
watch(() => route.query.path, (newPath) => {
  if (newPath) fetchQuestions()
})

const submitExam = () => {
  isSubmitted.value = true
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const isCorrect = (q, idx) => {
  if (!isSubmitted.value) return null
  const correctAns = getAnswerValue(q.answer)
  const userAns = userAnswers.value[idx]
  if (q.type === 'multi') {
     return (userAns || []).sort().join(',') === (correctAns || []).sort().join(',')
  }
  return userAns == correctAns
}
</script>

<template>
  <div class="exam-paper">
    <div class="exam-header">
      <div class="header-left">
        <div class="header-item title-row">
          <span class="label">考試：</span>
          <span class="value main-title">{{ examTitle }}</span>
        </div>
        <div class="header-item">
          <span class="label">應試人：</span>
          <input v-model="examineeName" type="text" placeholder="請輸入姓名" class="input-field" :disabled="isSubmitted">
        </div>
        <div class="header-item">
          <span class="label">准考證：</span>
          <span class="value mono">{{ ticketNumber }}</span>
        </div>
      </div>
      
      <div class="header-right">
        <div class="timer-box" :class="{ 'warning': timeLeft < 300, 'expired': timeLeft === 0 }">
          <div class="timer-label">剩餘時間</div>
          <div class="timer-value">{{ formatTime }}</div>
        </div>
        <div class="score-box" :class="{ 'visible': isSubmitted }">
          <div class="score-label">得分</div>
          <div class="score-value">{{ score }}</div>
        </div>
      </div>
    </div>

    <div class="instruction">
        注意：請仔細閱讀題幹，並選擇正確答案。多選題需全部選對才給分。
    </div>

    <div v-if="isLoading" class="loading-state">
      <div class="spinner"></div>
      <p>正在載入試卷...</p>
    </div>

    <div v-else class="exam-content">
      <div v-for="(q, index) in questions" :key="index" class="question-container">
        <!-- Passage Box -->
        <div v-if="q.passage" class="passage-box" v-html="q.passage"></div>

        <div class="question-item" :class="{ 'submitted': isSubmitted, 'correct': isCorrect(q, index) === true, 'wrong': isCorrect(q, index) === false }">
          <div class="question-text">
            <span class="q-num">{{ q.number || (index + 1) }}.</span>
            <span v-html="q.text"></span>
            <span class="q-score" v-if="q.score">({{ q.score }}分)</span>
          </div>

          <!-- Options Section -->
          <div class="options-grid" v-if="q.options && q.options.length">
            <label v-for="(optText, i) in q.options" :key="i" class="option-card" :class="{ 
              'is-correct': isSubmitted && (Array.isArray(getAnswerValue(q.answer)) ? getAnswerValue(q.answer).includes(i + 1) : getAnswerValue(q.answer) == (i + 1)),
              'is-wrong': isSubmitted && (q.type === 'multi' ? userAnswers[index].includes(i+1) : userAnswers[index] == (i+1)) && !(Array.isArray(getAnswerValue(q.answer)) ? getAnswerValue(q.answer).includes(i+1) : getAnswerValue(q.answer) == (i+1)),
              'is-selected': q.type === 'multi' ? userAnswers[index].includes(i+1) : userAnswers[index] == (i+1)
            }">
              <input 
                :type="q.type === 'multi' ? 'checkbox' : 'radio'" 
                :name="'q' + index" 
                :value="i + 1" 
                v-model="userAnswers[index]" 
                :disabled="isSubmitted"
              >
              <div class="check-mark"></div>
              <span class="opt-id">{{ String.fromCharCode(65 + i) }}</span>
              <span class="opt-val" v-html="optText"></span>
            </label>
          </div>

          <!-- Fill-in Section -->
          <div class="fill-input-area" v-else>
             <input 
                type="text" 
                v-model="userAnswers[index]" 
                placeholder="輸入答案..." 
                class="ans-input" 
                :disabled="isSubmitted"
              >
              <div class="ans-reveal" v-if="isSubmitted">
                正確答案：<span class="ans-text">{{ q.answer }}</span>
              </div>
          </div>
        </div>
      </div>
    </div>

    <div class="exam-footer">
      <button v-if="!isSubmitted" @click="submitExam" class="submit-btn">確認交卷</button>
      <button v-else @click="isSubmitted = false" class="retry-btn">重新練習</button>
    </div>
  </div>
</template>

<style scoped>
.exam-paper {
  background: #fdfdfd;
  max-width: 1000px;
  margin: 2rem auto;
  padding: 3rem;
  border-radius: 8px;
  box-shadow: 0 15px 50px rgba(0,0,0,0.1);
  color: #2c3e50;
  font-family: 'Inter', 'Noto Sans TC', sans-serif;
}

.exam-header {
  display: flex;
  justify-content: space-between;
  border-bottom: 3px solid #34495e;
  padding-bottom: 1.5rem;
  margin-bottom: 2rem;
}

.main-title { font-size: 1.8rem; font-weight: 800; color: #2c3e50; }
.title-row { margin-bottom: 1rem; }

.header-item { display: flex; align-items: center; gap: 0.5rem; margin-top: 0.5rem; }
.label { font-weight: 600; color: #7f8c8d; }
.input-field { border: none; border-bottom: 2px solid #bdc3c7; padding: 4px; background: transparent; width: 120px; outline: none; transition: border-color 0.3s; }
.input-field:focus { border-color: #3498db; }

.timer-box, .score-box {
  background: #fff;
  border: 2px solid #ecf0f1;
  padding: 0.8rem 1.2rem;
  border-radius: 12px;
  text-align: center;
  min-width: 100px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}

.score-box { border-color: #27ae60; color: #27ae60; opacity: 0; transform: scale(0.9); transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
.score-box.visible { opacity: 1; transform: scale(1); }
.score-value { font-size: 2.2rem; font-weight: 900; }

.timer-value { font-family: 'JetBrains Mono', monospace; font-size: 1.6rem; font-weight: 700; color: #2c3e50; }
.timer-box.warning { border-color: #e67e22; color: #e67e22; animation: blink 1s infinite; }

@keyframes blink { 50% { opacity: 0.6; } }

.instruction { background: #ebf5fb; border-left: 5px solid #3498db; padding: 1rem; margin-bottom: 2rem; font-size: 0.95rem; border-radius: 0 4px 4px 0; }

.passage-box {
  background: #f8f9fa;
  padding: 1.5rem;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  line-height: 1.8;
  font-size: 1.05rem;
  white-space: pre-wrap;
}

.question-container { margin-bottom: 3rem; }

.question-item {
  padding: 1.5rem;
  border-radius: 8px;
  transition: all 0.3s;
}

.question-text { font-size: 1.2rem; line-height: 1.6; margin-bottom: 1.2rem; font-weight: 500; }
.q-num { font-weight: 800; color: #34495e; margin-right: 0.8rem; }
.q-score { color: #95a5a6; font-size: 0.9rem; margin-left: 0.5rem; }

.options-grid { display: grid; gap: 0.8rem; }

.option-card {
  display: flex;
  align-items: center;
  padding: 1rem 1.2rem;
  background: #fff;
  border: 2px solid #ecf0f1;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s;
  position: relative;
}

.option-card:hover { border-color: #3498db; background: #f7f9fb; }
.option-card.is-selected { border-color: #3498db; background: #ebf5fb; }

input { display: none; }

.opt-id {
  width: 30px;
  height: 30px;
  background: #f1f3f5;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 1rem;
  font-weight: 700;
  color: #495057;
  flex-shrink: 0;
}

.is-selected .opt-id { background: #3498db; color: #fff; }

.option-card.is-correct { border-color: #27ae60; background: #eafaf1; }
.option-card.is-correct .opt-id { background: #27ae60; color: #fff; }

.option-card.is-wrong { border-color: #e74c3c; background: #fdedec; }
.option-card.is-wrong .opt-id { background: #e74c3c; color: #fff; }

.fill-input-area { margin-top: 1rem; }
.ans-input {
  width: 100%;
  padding: 12px;
  border: 2px solid #ecf0f1;
  border-radius: 8px;
  font-size: 1.1rem;
  outline: none;
  transition: border-color 0.3s;
}
.ans-input:focus { border-color: #3498db; }

.ans-reveal { margin-top: 1rem; padding: 1rem; background: #f1f3f4; border-radius: 8px; border-left: 4px solid #27ae60; }
.ans-text { font-weight: 700; color: #27ae60; font-size: 1.2rem; }

.submit-btn, .retry-btn {
  padding: 1rem 3rem;
  font-size: 1.2rem;
  font-weight: 700;
  border-radius: 50px;
  cursor: pointer;
  transition: all 0.3s;
  border: none;
}

.submit-btn { background: #3498db; color: #fff; box-shadow: 0 5px 15px rgba(52,152,219,0.3); }
.submit-btn:hover { background: #2980b9; transform: translateY(-2px); }

.retry-btn { background: #ecf0f1; color: #7f8c8d; }
.retry-btn:hover { background: #bdc3c7; }

.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4rem;
  gap: 1rem;
}

.spinner {
  width: 40px;
  height: 40px;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

.instruction { background: #ebf5fb; border-left: 5px solid #3498db; padding: 1rem; margin-bottom: 2rem; font-size: 0.95rem; border-radius: 0 4px 4px 0; }

@media (max-width: 768px) {
  .exam-paper { padding: 1.5rem; margin: 0; }
  .exam-header { flex-direction: column; align-items: flex-start; gap: 1rem; }
  .header-right { width: 100%; justify-content: space-between; }
}
</style>
