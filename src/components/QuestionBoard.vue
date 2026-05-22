<template>
  <div class="question-board">
    <div class="question-header">
      <div>
        <a-tag :color="categoryColor">{{ level.category }}</a-tag>
        <a-rate
          :value="level.difficulty"
          :count="5"
          disabled
          style="font-size: 14px"
        />
      </div>
      <h2 class="level-title">{{ level.title }}</h2>
      <p class="level-desc">{{ level.description }}</p>
    </div>

    <a-divider />

    <div class="question-content">
      <MdViewer :value="level.content" />
    </div>

    <a-divider />

    <div class="level-nav">
      <a-space>
        <a-button
          v-if="prevLevel"
          @click="navigateTo(prevLevel.key)"
          size="small"
        >
          ← 上一关
        </a-button>
        <a-button
          v-if="nextLevel"
          type="primary"
          @click="navigateTo(nextLevel.key)"
          size="small"
        >
          下一关 →
        </a-button>
      </a-space>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { useRouter } from "vue-router";
import type { LevelType } from "../levels";
import { getPrevLevel, getNextLevel, allLevels } from "../levels";
import MdViewer from "./MdViewer.vue";

const props = defineProps<{
  level: LevelType;
  resultStatus?: number;
}>();

defineEmits<{
  congrats: [];
}>();

const router = useRouter();

const prevLevel = computed(() => getPrevLevel(props.level));
const nextLevel = computed(() => getNextLevel(props.level));

const mainLevels = allLevels.filter((l) => l.type === "main");
const isLastMainLevel = computed(
  () => props.level.key === mainLevels[mainLevels.length - 1]?.key
);

const categoryColor = computed(() => {
  const map: Record<string, string> = {
    基础语法: "blue",
    中级: "green",
    进阶: "orange",
    数据分析: "purple",
    AI基础: "cyan",
    AI进阶: "gold",
    Transformer: "geekblue",
    搭建模型: "magenta",
    实战: "red",
  };
  return map[props.level.category] || "default";
});

function navigateTo(key: string) {
  router.push({ path: `/learn/${key}` });
}
</script>

<style scoped>
.question-board {
  padding: 16px 24px;
  height: 100%;
  overflow-y: auto;
}

.question-header {
  margin-bottom: 8px;
}

.level-title {
  margin: 8px 0 4px;
  font-size: 20px;
  color: var(--python-dark);
}

.level-desc {
  color: #666;
  font-size: 14px;
  margin: 0;
}

.question-content {
  min-height: 200px;
}

.level-nav {
  padding: 8px 0;
}
</style>
