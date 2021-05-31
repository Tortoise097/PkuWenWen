import { createApp } from 'vue'
import App from './App.vue'
//import VueRouter from 'vue-router'
import ElementPlus from 'element-plus';
//import element from 'element-plus'
import 'element-plus/lib/theme-chalk/index.css';
import router from './router'
import axios from 'axios'
import {ElMessage} from 'element-plus'


const app = createApp(App)
app.use(router)
//app.use(element)
app.use(ElementPlus)
app.config.globalProperties.$http = axios
app.config.globalProperties.$url = 'http://127.0.0.1:8000'
app.config.globalProperties.$message= ElMessage
app.provide('$message', ElMessage)

app.mount('#app')

