import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/ai-sch-exam/',
  title: "AI 教育測驗系統",
  description: "會考 / 學測 / 分科測驗 線上模擬測驗系統",
  head: [
    ['script', { async: true, src: 'https://busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js' }],
    ['script', {}, `
      window.MathJax = {
        tex: {
          inlineMath: [['$', '$'], ['\\\\(', '\\\\)']]
        },
        options: {
          skipHtmlTags: ['script', 'style', 'textarea', 'pre', 'code']
        }
      };
    `],
    ['script', { id: 'MathJax-script', async: true, src: 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js' }]
  ],
  markdown: {
    math: true
  },
  themeConfig: {
    nav: [
      { text: '首頁', link: '/' },
      { text: '開始測驗', link: '/exams' },
      { text: '心得與解析', link: 'https://toydogcat.github.io/ai-exp-sch-exam/' }
    ],
    sidebar: [
      {
        text: '國中教育會考 (CAP)',
        items: [
          { text: '會考概覽', link: '/cap' }
        ]
      },
      {
        text: '大學入學考試 (CEEC)',
        items: [
          { text: '學測 (GSAT)', link: '/gsat' },
          { text: '分科測驗 (AST)', link: '/ast' }
        ]
      },
      {
        text: '高等數學 (Advanced Math)',
        items: [
          { text: '微積分隨機線上測驗', link: '/calculus' }
        ]
      }
    ],
    footer: {
      message: '總訪問量 <span id="busuanzi_value_site_pv"></span> 次 | 訪客數 <span id="busuanzi_value_site_uv"></span> 人',
      copyright: 'Copyright © 2026-present AI School Exam Team'
    }
  }
})
