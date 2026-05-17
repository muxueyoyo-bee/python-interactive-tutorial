<template>
  <a-config-provider :theme="{ token: { colorPrimary: '#306998' } }" :locale="zhCN">
    <div id="app-container">
      <a-row class="header" align="middle" :wrap="false">
        <a-col flex="180px">
          <router-link to="/" class="logo-link">
            <a-row align="middle" :wrap="false">
              <img src="/favicon.svg" alt="Python 交互教程" class="logo" />
              <span class="title">Python 交互教程</span>
            </a-row>
          </router-link>
        </a-col>
        <a-col flex="auto">
          <a-menu
            :selected-keys="selectedKeys"
            mode="horizontal"
            :style="{ lineHeight: '64px' }"
            @click="doClickMenu"
          >
            <a-menu-item key="/learn/level1">
              <book-outlined />学习
            </a-menu-item>
            <a-menu-item key="/levels">
              <appstore-outlined />关卡
            </a-menu-item>
          </a-menu>
        </a-col>
      </a-row>
      <div class="content">
        <router-view />
      </div>
    </div>
  </a-config-provider>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import { BookOutlined, AppstoreOutlined } from "@ant-design/icons-vue";
import zhCN from "ant-design-vue/es/locale/zh_CN";

const route = useRoute();
const router = useRouter();

const isLevelRoute = computed(() => route.path.startsWith("/learn"));
const selectedKeys = computed(() => {
  if (route.path.startsWith("/learn")) return ["/learn/level1"];
  return [route.path];
});

const doClickMenu = ({ key }: { key: string }) => {
  router.push({ path: key });
};
</script>

<style scoped>
#app-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  background: #fff;
  border-bottom: 1px solid #e8e8e8;
  padding: 0 24px;
  flex-shrink: 0;
}

.logo-link {
  text-decoration: none;
}

.logo {
  width: 36px;
  height: 36px;
  margin-right: 8px;
}

.title {
  font-size: 20px;
  font-weight: 700;
  color: var(--python-dark);
  white-space: nowrap;
}

.content {
  flex: 1;
  overflow: hidden;
}
</style>
