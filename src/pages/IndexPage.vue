<template>
  <div class="index-page">
    <!-- Pyodide loading overlay -->
    <a-modal
      :open="loadingPyodide"
      :closable="false"
      :mask-closable="false"
      title="正在加载 Python 引擎"
      :footer="null"
    >
      <a-spin tip="首次加载需要下载约 15MB 数据，请耐心等待...">
        <div style="padding: 24px; text-align: center">
          {{ loadingMessage }}
        </div>
      </a-spin>
    </a-modal>

    <a-row class="main-row" :gutter="[16, 16]">
      <!-- Left: Question Board -->
      <a-col :lg="11" :xs="24" class="left-panel">
        <QuestionBoard
          v-if="level"
          :level="level"
          :result-status="resultStatus"
        />
      </a-col>

      <!-- Right: Editor + Results -->
      <a-col :lg="13" :xs="24" class="right-panel">
        <PythonEditor
          v-if="level"
          ref="pythonEditorRef"
          :key="level.key"
          :level="level"
          @result-change="onResultChange"
        />
        <a-empty v-else description="关卡未找到" />
      </a-col>
    </a-row>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch, reactive } from "vue";
import { useRoute } from "vue-router";
import QuestionBoard from "../components/QuestionBoard.vue";
import PythonEditor from "../components/PythonEditor.vue";
import { getLevelByKey, type LevelType } from "../levels";
import { useGlobalStore } from "../core/globalStore";
import { loadContent } from "../levels/contentLoader";

const props = defineProps<{ levelKey?: string }>();
const route = useRoute();
const store = useGlobalStore();

const resultStatus = ref(-1);
const loadingPyodide = ref(false);
const loadingMessage = ref("");
const levelContent = ref("");

const baseLevel = computed(() => {
  const key = props.levelKey || (route.params.levelKey as string) || "level1";
  return getLevelByKey(key);
});

const level = computed((): LevelType | null => {
  if (!baseLevel.value) return null;
  return { ...baseLevel.value, content: levelContent.value || baseLevel.value.content };
});

// Lazy-load level content when level changes
watch(
  () => baseLevel.value?.key,
  async (key) => {
    if (!key) return;
    store.setCurrentLevelKey(key);
    levelContent.value = "";
    levelContent.value = await loadContent(key);
  },
  { immediate: true }
);

function onResultChange(status: number) {
  resultStatus.value = status;
}
</script>

<style scoped>
.index-page {
  height: 100%;
  overflow: hidden;
}

.main-row {
  height: 100%;
  margin: 0 !important;
}

.left-panel {
  height: 100%;
  overflow-y: auto;
  border-right: 1px solid #f0f0f0;
  background: #fff;
}

.right-panel {
  height: 100%;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
</style>
