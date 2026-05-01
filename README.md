# ai-sch-exam
The [school exam](https://toydogcat.github.io/ai-sch-exam/).

## Reference
- [大學入學考試中心](https://www.ceec.edu.tw/)
- [國中教育會考](https://cap.rcpet.edu.tw/)

## 網站統計
本專案採用 **不蒜子 (Busuanzi)** 來進行網站的訪問量與訪客數統計：
- **引入方式**：在 `.vitepress/config.js` 的 `head` 區塊透過 CDN 引入 JS 腳本（`https://cdn.jsdelivr.net/gh/sukkaw/busuanzi@2.3/bsz.pure.mini.js`）。
- **顯示位置**：在 `themeConfig.footer` 的 `message` 區塊，使用不蒜子指定的標籤 ID (`busuanzi_value_site_pv`, `busuanzi_value_site_uv`) 來動態呈現總訪問量及訪客數。
