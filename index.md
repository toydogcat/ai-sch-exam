---
layout: home
hero:
  name: "AI 教育測驗系統"
  text: "會考 / 學測 / 分科測驗"
  tagline: "全台最完整的歷年試題數位化平台，提供擬真線上測驗與深度解析。"
  image:
    src: /logo.png
    alt: AI Exam Logo
  actions:
    - theme: romance
      text: 國中教育會考 (CAP)
      link: /cap
    - theme: brand
      text: 學科能力測驗 (GSAT)
      link: /gsat
    - theme: alt
      text: 分科測驗 (AST)
      link: /ast

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
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  text-decoration: none !important;
  color: var(--vp-c-text-1) !important;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
  overflow: hidden;
}
.dark .glass-card {
  background: rgba(30, 30, 30, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}
.glass-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}
.card-icon {
  font-size: 3rem;
  margin-bottom: 1.5rem;
}
.glass-card h3 {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0 0 0.5rem 0;
}
.glass-card p {
  color: var(--vp-c-text-2);
  margin-bottom: 1.5rem;
}
.badge {
  display: inline-block;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 600;
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
}
.glass-card.cap:hover { border-color: #3eaf7c; }
.glass-card.gsat:hover { border-color: #3b82f6; }
.glass-card.ast:hover { border-color: #f59e0b; }
</style>
