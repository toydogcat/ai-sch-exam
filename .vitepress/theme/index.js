import DefaultTheme from 'vitepress/theme'
import Paper from './components/Paper.vue'
import './custom.css'
import { watch } from 'vue'
import { useRoute } from 'vitepress'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Paper', Paper)

    // Busuanzi integration for SPA
    if (typeof window !== 'undefined') {
      const route = useRoute()
      watch(() => route.path, () => {
        // Trigger busuanzi reload
        const script = document.createElement('script')
        script.src = '//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js'
        script.async = true
        // Remove old script if exists
        const oldScript = document.querySelector('script[src*="busuanzi"]')
        if (oldScript) oldScript.remove()
        document.head.appendChild(script)
      }, { immediate: true })
    }
  }
}
