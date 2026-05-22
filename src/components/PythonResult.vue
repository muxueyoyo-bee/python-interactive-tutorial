<template>
  <a-card
    title="执行结果"
    size="small"
    class="result-card"
  >
    <a-spin :spinning="isExecuting" tip="代码执行中...">
      <template v-if="error">
        <a-alert
          type="error"
          :message="'Python 运行错误'"
          :description="error"
          show-icon
          style="margin-bottom: 12px"
        />
      </template>

      <a-tabs v-if="!isExecuting && hasOutput" size="small">
        <a-tab-pane key="stdout" tab="输出">
          <pre class="output-pre">{{ displayStdout || '(无输出)' }}</pre>
        </a-tab-pane>

        <a-tab-pane
          key="return"
          tab="返回值"
          v-if="returnValue !== undefined"
        >
          <pre class="output-pre">{{ JSON.stringify(returnValue, null, 2) }}</pre>
        </a-tab-pane>

        <a-tab-pane
          key="plots"
          tab="图表"
          v-if="plots.length > 0"
        >
          <div v-for="(plot, i) in plots" :key="i" class="plot-container">
            <img :src="'data:image/png;base64,' + plot" class="plot-img" />
          </div>
        </a-tab-pane>
      </a-tabs>

      <a-empty
        v-if="!isExecuting && !hasOutput && !error"
        description="点击「运行」按钮执行代码"
      />
    </a-spin>
  </a-card>
</template>

<script setup lang="ts">
import { computed } from "vue";

const props = withDefaults(
  defineProps<{
    hasRun?: boolean;
    stdout?: string;
    returnValue?: unknown;
    error?: string | null;
    plots?: string[];
    isExecuting?: boolean;
  }>(),
  {
    hasRun: false,
    stdout: "",
    returnValue: undefined,
    error: null,
    plots: () => [],
    isExecuting: false,
  }
);

const hasOutput = computed(
  () => props.stdout || props.plots.length > 0 || props.returnValue !== undefined
);
const displayStdout = computed(() => props.stdout);
</script>

<style scoped>
.result-card {
  margin-top: 8px;
}

.output-pre {
  background: #f6f8fa;
  border-radius: 4px;
  padding: 12px;
  font-family: "Consolas", "Monaco", monospace;
  font-size: 13px;
  line-height: 1.5;
  white-space: pre-wrap;
  word-break: break-all;
  max-height: 300px;
  overflow-y: auto;
  margin: 0;
}

.plot-container {
  text-align: center;
  padding: 8px;
}

.plot-img {
  max-width: 100%;
  border: 1px solid #e8e8e8;
  border-radius: 4px;
}
</style>
