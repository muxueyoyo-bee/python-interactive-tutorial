import type { RouteRecordRaw } from "vue-router";
import IndexPage from "../pages/IndexPage.vue";
import LevelsPage from "../pages/LevelsPage.vue";
import PlaygroundPage from "../pages/PlaygroundPage.vue";

export default [
  {
    path: "/",
    redirect: "/learn/level1",
  },
  {
    path: "/learn/:levelKey?",
    component: IndexPage,
    props: true,
  },
  {
    path: "/levels",
    component: LevelsPage,
  },
  {
    path: "/playground",
    component: PlaygroundPage,
  },
] as RouteRecordRaw[];
