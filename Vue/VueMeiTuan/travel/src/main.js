import Vue from 'vue'
import App from './App.vue'
import fastClick from 'fastclick'
import './assets/styles/reset.css'
import './assets/styles/border.css'
import './assets/styles/iconfont.css'

Vue.config.productionTip = true
fastClick.attach(document.body)

new Vue({
  render: h => h(App),
}).$mount('#app')
