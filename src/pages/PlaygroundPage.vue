<template>
  <div class="playground-page">
    <div class="pg-header">
      <h2>Python 练习广场</h2>
      <p>自由编写 Python 代码，不受关卡限制~</p>
      <a-button type="primary" @click="runCode" :loading="isExecuting">
        运行 (Ctrl+Enter)
      </a-button>
      <a-button style="margin-left: 8px" @click="clearAll">清空</a-button>
    </div>

    <a-row :gutter="[16, 16]" class="pg-main">
      <a-col :md="12" :xs="24" class="pg-editor-col">
        <CodeEditor
          ref="codeEditorRef"
          v-model="code"
          :font-size="16"
          @run="runCode"
        />
        <a-card title="执行历史" size="small" style="margin-top: 8px">
          <a-collapse v-if="history.length > 0">
            <a-collapse-item
              v-for="(entry, i) in history"
              :key="i"
              :header="entry.code.slice(0, 80)"
            >
              <pre class="output-pre">{{ entry.output || entry.error }}</pre>
            </a-collapse-item>
          </a-collapse>
          <a-empty v-else description="暂无执行历史" />
        </a-card>
      </a-col>

      <a-col :md="12" :xs="24">
        <PythonResult
          :result-status="resultStatus"
          :stdout="displayStdout"
          :return-value="returnValue"
          :error="errorMsg"
          :plots="plots"
          :is-executing="isExecuting"
        />
      </a-col>
    </a-row>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import CodeEditor from "../components/CodeEditor.vue";
import PythonResult from "../components/PythonResult.vue";
import {
  executePython,
  getPlotBase64,
  stripPlotMarkers,
} from "../core/pyodideExecutor";
import { usePython } from "../core/usePython";
import { JudgeStatus } from "../core/result";

const { ensurePyodide, isExecuting } = usePython();
const codeEditorRef = ref<InstanceType<typeof CodeEditor> | null>(null);

const DEFAULT_CODE = `# Python 练习广场
# 在这里自由编写 Python 代码
# 按 Ctrl+Enter 运行

print("Hello, Python!")

# 试试这些：
# name = input("你叫什么名字？")
# for i in range(10):
#     print(i)
`;

const code = ref(DEFAULT_CODE);
const resultStatus = ref(JudgeStatus.DEFAULT);
const displayStdout = ref("");
const returnValue = ref<unknown>(undefined);
const errorMsg = ref<string | null>(null);
const plots = ref<string[]>([]);
const history = ref<
  { code: string; output: string; error: string | null }[]
>([]);

async function runCode() {
  if (isExecuting.value) return;
  isExecuting.value = true;
  errorMsg.value = null;
  plots.value = [];

  try {
    await ensurePyodide();

    const result = await executePython(code.value);
    plots.value = getPlotBase64(result.stdout);
    displayStdout.value = stripPlotMarkers(result.stdout);
    returnValue.value = result.returnValue;
    errorMsg.value = result.error;
    resultStatus.value = result.error
      ? JudgeStatus.ERROR
      : JudgeStatus.SUCCEED;

    history.value.unshift({
      code: code.value,
      output: result.stdout,
      error: result.error,
    });
    if (history.value.length > 20) {
      history.value = history.value.slice(0, 20);
    }
  } catch (e: unknown) {
    const err = e as Error;
    errorMsg.value = err.message || String(e);
    resultStatus.value = JudgeStatus.ERROR;
  } finally {
    isExecuting.value = false;
  }
}

function clearAll() {
  code.value = DEFAULT_CODE;
  resultStatus.value = JudgeStatus.DEFAULT;
  displayStdout.value = "";
  errorMsg.value = null;
  plots.value = [];
  history.value = [];
}
</script>

<style scoped>
.playground-page {
  height: 100%;
  padding: 16px 24px;
  overflow-y: auto;
}

.pg-header {
  margin-bottom: 16px;
}

.pg-header h2 {
  margin-bottom: 4px;
  color: var(--python-dark);
}

.pg-header p {
  color: #666;
  margin-bottom: 12px;
}

.pg-main {
  height: calc(100% - 120px);
}

.pg-editor-col {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.output-pre {
  background: #f6f8fa;
  border-radius: 4px;
  padding: 8px;
  font-family: Consolas, Monaco, monospace;
  font-size: 13px;
  white-space: pre-wrap;
  word-break: break-all;
  max-height: 200px;
  overflow-y: auto;
}
</style>
