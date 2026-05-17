<template>
  <div class="levels-page">
    <div class="levels-hero">
      <h1>选择关卡</h1>
      <p>共 {{ allLevels.length }} 关 · 循序渐进掌握 Python</p>
      <a-progress
        :percent="Math.round((store.totalCompleted / mainLevels.length) * 100)"
        :format="() => `${store.totalCompleted}/${mainLevels.length}`"
        style="max-width: 400px; margin: 0 auto"
      />
    </div>

    <div
      v-for="phase in phases"
      :key="phase.name"
      class="phase-section"
    >
      <h2 class="phase-title">
        <span class="phase-icon">{{ phase.icon }}</span>
        {{ phase.name }}
        <a-tag style="margin-left: 8px">{{ getPhaseCount(phase.start, phase.count) }} 关</a-tag>
      </h2>

      <a-row :gutter="[12, 12]">
        <a-col
          v-for="(level, idx) in mainLevels.slice(phase.start, phase.start + phase.count)"
          :key="level.key"
          :xs="12"
          :sm="8"
          :md="6"
          :lg="4"
        >
          <a-card
            :hoverable="true"
            class="level-card"
            :class="{
              completed: isCompleted(level.key),
              locked: false,
            }"
            @click="openLevel(level.key)"
          >
            <div class="card-number">{{ phase.start + idx + 1 }}</div>
            <div class="card-title">{{ level.title }}</div>
            <div class="card-tags">
              <a-tag
                v-for="tag in level.tags.slice(0, 2)"
                :key="tag"
                size="small"
                color="blue"
              >
                {{ tag }}
              </a-tag>
            </div>
            <a-rate :value="level.difficulty" :count="5" disabled style="font-size: 12px" />
            <div v-if="isCompleted(level.key)" class="completed-badge">
              <check-circle-filled style="color: #52c41a; font-size: 20px" />
            </div>
          </a-card>
        </a-col>
      </a-row>
    </div>

    <!-- Custom levels section -->
    <div v-if="customLevels.length > 0" class="phase-section">
      <h2 class="phase-title">
        <span class="phase-icon">🎯</span> 实战关卡
      </h2>
      <a-row :gutter="[12, 12]">
        <a-col
          v-for="level in customLevels"
          :key="level.key"
          :xs="12"
          :sm="8"
          :md="6"
          :lg="4"
        >
          <a-card
            :hoverable="true"
            class="level-card custom-card"
            @click="openLevel(level.key)"
          >
            <div class="card-number">⭐</div>
            <div class="card-title">{{ level.title }}</div>
            <a-rate :value="level.difficulty" :count="5" disabled style="font-size: 12px" />
          </a-card>
        </a-col>
      </a-row>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { useRouter } from "vue-router";
import { CheckCircleFilled } from "@ant-design/icons-vue";
import { allLevels, mainLevels, customLevels } from "../levels";
import { useGlobalStore } from "../core/globalStore";

const router = useRouter();
const store = useGlobalStore();

const phases = [
  { name: "基础语法", icon: "📖", start: 0, count: 15 },
  { name: "中级", icon: "⚡", start: 15, count: 10 },
  { name: "进阶", icon: "🔥", start: 25, count: 10 },
  { name: "数据分析", icon: "📊", start: 35, count: 10 },
];

function getPhaseCount(start: number, count: number): number {
  return Math.min(count, mainLevels.length - start);
}

function isCompleted(key: string): boolean {
  return store.mainLevelProgress[key]?.completed || false;
}

function openLevel(key: string) {
  router.push({ path: `/learn/${key}` });
}
</script>

<style scoped>
.levels-page {
  padding: 24px;
  max-width: 1200px;
  margin: 0 auto;
  height: 100%;
  overflow-y: auto;
}

.levels-hero {
  text-align: center;
  margin-bottom: 32px;
}

.levels-hero h1 {
  font-size: 28px;
  color: var(--python-dark);
  margin-bottom: 8px;
}

.phase-section {
  margin-bottom: 32px;
}

.phase-title {
  font-size: 20px;
  margin-bottom: 16px;
  color: var(--python-dark);
}

.phase-icon {
  font-size: 24px;
}

.level-card {
  position: relative;
  cursor: pointer;
  transition: transform 0.2s;
}

.level-card:hover {
  transform: translateY(-2px);
}

.level-card.completed {
  border-color: #52c41a;
}

.level-card .card-number {
  font-size: 28px;
  font-weight: 700;
  color: var(--python-blue);
  margin-bottom: 4px;
}

.level-card.custom-card .card-number {
  color: #fa8c16;
}

.level-card .card-title {
  font-size: 13px;
  margin-bottom: 8px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.level-card .card-tags {
  margin-bottom: 8px;
}

.completed-badge {
  position: absolute;
  top: 8px;
  right: 8px;
}
</style>
