<template>
  <div class="python-editor">
    <div class="editor-toolbar">
      <a-space>
        <a-button type="primary" @click="runCode" :loading="isExecuting">
          <play-circle-outlined /> 运行 (Ctrl+Enter)
        </a-button>
        <a-button @click="resetCode">
          <undo-outlined /> 重置
        </a-button>
        <a-collapse
          v-if="level.hint || level.answer"
          :active-key="activeCollapseKeys"
          @change="onCollapseChange"
          class="toolbar-collapse"
        >
          <a-collapse-panel key="hint" header="查看提示">
            <a-alert type="info" :message="level.hint" />
          </a-collapse-panel>
          <a-collapse-panel key="answer" header="查看答案">
            <a-alert
              type="warning"
              message="确定要看答案吗？作弊可学不到东西哦！"
            >
              <template #description>
                <CodeEditor
                  :model-value="level.answer"
                  :read-only="true"
                  :font-size="14"
                  language="python"
                />
              </template>
            </a-alert>
          </a-collapse-panel>
          <a-collapse-panel key="init" header="预执行代码" v-if="level.setupCode">
            <CodeEditor
              :model-value="level.setupCode"
              :read-only="true"
              :font-size="14"
              language="python"
            />
          </a-collapse-panel>
        </a-collapse>
      </a-space>
      <div class="execution-time" v-if="executionTime > 0">
        {{ executionTime }}ms
      </div>
    </div>

    <div class="editor-main">
      <CodeEditor
        ref="codeEditorRef"
        v-model="currentCode"
        :font-size="store.settings.fontSize"
        @run="runCode"
      />
    </div>

    <div class="result-area">
      <PythonResult
        :has-run="hasRun"
        :stdout="displayStdout"
        :return-value="returnValue"
        :error="errorMsg"
        :plots="plots"
        :is-executing="isExecuting"
      />
      <div v-if="hasRun && level.answer" class="answer-reference">
        <a-divider>参考答案</a-divider>
        <CodeEditor
          :model-value="level.answer"
          :read-only="true"
          :font-size="14"
          language="python"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from "vue";
import { PlayCircleOutlined, UndoOutlined } from "@ant-design/icons-vue";
import CodeEditor from "./CodeEditor.vue";
import PythonResult from "./PythonResult.vue";
import { useGlobalStore } from "../core/globalStore";
import { execute } from "../engine/executor";
import { extractPlots, stripPlotMarkers } from "../engine/pyodide/plot-capture";
import type { LevelType } from "../levels";

const props = defineProps<{
  level: LevelType;
}>();

const store = useGlobalStore();
const codeEditorRef = ref<InstanceType<typeof CodeEditor> | null>(null);

const currentCode = ref(props.level.defaultCode);
const isExecuting = ref(false);
const hasRun = ref(false);
const displayStdout = ref("");
const returnValue = ref<unknown>(undefined);
const errorMsg = ref<string | null>(null);
const plots = ref<string[]>([]);
const executionTime = ref(0);
const activeCollapseKeys = ref<string[]>([]);

function onCollapseChange(keys: string[] | string) {
  activeCollapseKeys.value = Array.isArray(keys) ? keys : [keys];
}

watch(
  () => props.level.key,
  () => {
    const savedCode = store.getSavedCode(props.level.key);
    currentCode.value = savedCode || props.level.defaultCode;
    hasRun.value = false;
    displayStdout.value = "";
    errorMsg.value = null;
    plots.value = [];
    executionTime.value = 0;
    activeCollapseKeys.value = [];
  }
);

async function runCode() {
  if (isExecuting.value) return;

  isExecuting.value = true;
  errorMsg.value = null;
  plots.value = [];
  executionTime.value = 0;

  try {
    const setupCode = props.level.setupCode || "";

    const userResult = await execute({
      code: setupCode + "\n" + currentCode.value,
      timeoutMs: 5000,
    });

    plots.value = extractPlots(userResult.stdout);
    displayStdout.value = userResult.error
      ? userResult.error
      : stripPlotMarkers(userResult.stdout) +
        (userResult.stderr ? "\n" + userResult.stderr : "");
    returnValue.value = userResult.returnValue;
    errorMsg.value = userResult.error;
    executionTime.value = userResult.executionTimeMs;
    hasRun.value = true;

    store.recordAttempt(props.level.key, currentCode.value);
    store.completeLevel(props.level.key, currentCode.value);
  } catch (e: unknown) {
    const err = e as Error;
    errorMsg.value = err.message || String(e);
    displayStdout.value = "";
    hasRun.value = true;
  } finally {
    isExecuting.value = false;
  }
}

function resetCode() {
  currentCode.value = props.level.defaultCode;
  hasRun.value = false;
  displayStdout.value = "";
  errorMsg.value = null;
  plots.value = [];
}
</script>

<style scoped>
.python-editor {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.editor-toolbar {
  padding: 8px 16px;
  background: #fafafa;
  border-bottom: 1px solid #e8e8e8;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-shrink: 0;
}

.toolbar-collapse {
  max-width: 400px;
}

.toolbar-collapse :deep(.ant-collapse-header) {
  padding: 4px 8px !important;
  font-size: 13px;
}

.toolbar-collapse :deep(.ant-collapse-content-box) {
  padding: 8px !important;
}

.execution-time {
  font-size: 12px;
  color: #999;
  padding-top: 4px;
}

.editor-main {
  flex: 1;
  min-height: 200px;
  overflow: hidden;
}

.result-area {
  flex-shrink: 0;
  max-height: 40%;
  overflow-y: auto;
  border-top: 1px solid #e8e8e8;
}

.answer-reference {
  padding: 0 12px 12px;
}
</style>
