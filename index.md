---
layout: home
hero:
  name: "AI 教育測驗系統"
  text: "會考 / 學測 / 分科測驗"
  tagline: "全台最完整的歷年試題數位化平台，提供擬真線上測驗與深度解析。"
  image:
    src: /logo.webp
    alt: AI Exam Logo
  actions:
    - theme: alt
      text: 國中教育會考 (CAP)
      link: /cap
    - theme: brand
      text: 學科能力測驗 (GSAT)
      link: /gsat
    - theme: brand
      text: 分科測驗 (AST)
      link: /ast
    - theme: romance
      text: 微積分
      link: /calculus

features:
  - title: 數位化精準還原
    details: 完美還原紙本試卷排版，包含精細圖表、地圖與實驗圖。
    icon: 📝
  - title: 英聽線上模擬
    details: 內建英聽播放系統，隨時隨地練習聽力理解。
    icon: 🎧
  - title: 自動閱卷分析
    details: 交卷後立即給分，掌握自己的學習弱點。
    icon: 📊
---

<div class="main-entry">
  <div class="section-title">
    <h2>考試類別選擇</h2>
    <p>點選下方進入對應的試題庫</p>
  </div>

  <div class="glass-grid">
    <a href="./cap" class="glass-card cap">
      <div class="card-icon">🏫</div>
      <h3>國中教育會考 (CAP)</h3>
      <p>國中升高中入學考試</p>
      <div class="badge">收錄 111-114 年</div>
    </a>
    <a href="./gsat" class="glass-card gsat">
      <div class="card-icon">🎓</div>
      <h3>學科能力測驗 (GSAT)</h3>
      <p>高中升大學多元入學考試</p>
      <div class="badge">收錄 112-115 年</div>
    </a>
    <a href="./ast" class="glass-card ast">
      <div class="card-icon">🧪</div>
      <h3>分科測驗 (AST)</h3>
      <p>大學入學指定科目考試</p>
      <div class="badge">收錄 111-113 年</div>
    </a>
    <a href="./calculus" class="glass-card calculus">
      <div class="card-icon">🧮</div>
      <h3>微積分隨機測驗 (Calculus)</h3>
      <p>高等數學線上模擬測驗</p>
      <div class="badge">自訂章節題庫抽題</div>
    </a>
  </div>
</div>

<style>
.main-entry {
  max-width: 1100px;
  margin: 4rem auto;
  padding: 0 2rem;
}
.section-title {
  text-align: center;
  margin-bottom: 3rem;
}
.section-title h2 {
  font-size: 2.2rem;
  font-weight: 800;
  border: none;
}
.glass-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}
.glass-card {
  position: relative;
  padding: 2.5rem;
  border-radius: 32px;
  background: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  text-decoration: none !important;
  color: var(--vp-c-text-1) !important;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.glass-card:hover {
  transform: translateY(-12px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}

.glass-card.cap:hover { 
  background: rgba(62, 175, 124, 0.1);
  border-color: #3eaf7c; 
}
.glass-card.gsat:hover { 
  background: rgba(59, 130, 246, 0.1);
  border-color: #3b82f6; 
}
.glass-card.ast:hover { 
  background: rgba(245, 158, 11, 0.1);
  border-color: #f59e0b; 
}
.glass-card.calculus:hover { 
  background: rgba(236, 72, 153, 0.1);
  border-color: #ec4899; 
}

.card-icon {
  font-size: 3.5rem;
  margin-bottom: 1.5rem;
  transition: transform 0.3s ease;
}
.glass-card:hover .card-icon {
  transform: scale(1.1) rotate(5deg);
}

.glass-card h3 {
  font-size: 1.6rem;
  font-weight: 800;
  margin: 0 0 0.75rem 0;
  letter-spacing: -0.02em;
}

.glass-card p {
  color: var(--vp-c-text-2);
  margin-bottom: 1.5rem;
  font-size: 1rem;
}

.badge {
  display: inline-block;
  padding: 6px 16px;
  border-radius: 100px;
  font-size: 0.85rem;
  font-weight: 700;
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-2);
  transition: all 0.3s ease;
}

.glass-card.cap:hover .badge { background: #3eaf7c; color: #fff; }
.glass-card.gsat:hover .badge { background: #3b82f6; color: #fff; }
.glass-card.ast:hover .badge { background: #f59e0b; color: #fff; }
.glass-card.calculus:hover .badge { background: #ec4899; color: #fff; }
</style>
