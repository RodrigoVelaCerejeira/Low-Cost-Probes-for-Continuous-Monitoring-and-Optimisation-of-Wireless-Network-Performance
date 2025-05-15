import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/tailwind.css'

import Vue3Toastify, { toast } from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';

const app = createApp(App);

app.use(router);
app.use(Vue3Toastify, {
    autoClose: 10000,
    position: 'top-right',

});

app.mount('#app');