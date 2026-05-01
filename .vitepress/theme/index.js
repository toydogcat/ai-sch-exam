import DefaultTheme from 'vitepress/theme'
import Paper from './components/Paper.vue'
import './custom.css'
import { onMounted, watch } from 'vue'
import { useRoute } from 'vitepress'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Paper', Paper)
  },
  setup() {
    // Busuanzi integration for SPA — must be in setup() context
    if (typeof window !== 'undefined') {
      const route = useRoute()
      const reloadBusuanzi = () => {
        const oldScript = document.querySelector('script[src*="busuanzi"]')
        if (oldScript) oldScript.remove()
        const script = document.createElement('script')
        script.src = 'https://cdn.jsdelivr.net/gh/sukkaw/busuanzi@2.3/bsz.pure.mini.js'
        script.async = true
        document.head.appendChild(script)
      }
      onMounted(reloadBusuanzi)
      watch(() => route.path, reloadBusuanzi)
    }
  }
}
