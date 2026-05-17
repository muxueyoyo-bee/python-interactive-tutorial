import { createApp } from "vue";
import Antd from "ant-design-vue";
import App from "./App.vue";
import * as VueRouter from "vue-router";
import routes from "./configs/routes";
import { createPinia } from "pinia";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import "ant-design-vue/dist/reset.css";
import "./style.css";

const router = VueRouter.createRouter({
  history: VueRouter.createWebHashHistory(),
  routes,
});

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

createApp(App).use(Antd).use(router).use(pinia).mount("#app");
