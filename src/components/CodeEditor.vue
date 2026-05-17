<template>
  <div ref="editorContainer" class="code-editor-container"></div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch, nextTick } from "vue";
import * as monaco from "monaco-editor";

const props = withDefaults(
  defineProps<{
    modelValue: string;
    readOnly?: boolean;
    fontSize?: number;
    theme?: string;
    language?: string;
  }>(),
  {
    readOnly: false,
    fontSize: 16,
    theme: "vs",
    language: "python",
  }
);

const emit = defineEmits<{
  "update:modelValue": [value: string];
  run: [];
}>();

const editorContainer = ref<HTMLElement | null>(null);
let editor: monaco.editor.IStandaloneCodeEditor | null = null;

onMounted(async () => {
  await nextTick();
  if (!editorContainer.value) return;

  editor = monaco.editor.create(editorContainer.value, {
    value: props.modelValue,
    language: props.language,
    theme: props.theme,
    fontSize: props.fontSize,
    readOnly: props.readOnly,
    minimap: { enabled: false },
    scrollBeyondLastLine: false,
    renderWhitespace: "selection",
    tabSize: 4,
    automaticLayout: true,
    lineNumbers: "on",
    wordWrap: "on",
    suggest: { showWords: true },
  });

  editor.onDidChangeModelContent(() => {
    const value = editor!.getValue();
    emit("update:modelValue", value);
  });

  editor.addAction({
    id: "run-python",
    label: "Run Python Code",
    keybindings: [monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter],
    run: () => emit("run"),
  });
});

onUnmounted(() => {
  editor?.dispose();
});

watch(
  () => props.modelValue,
  (newVal) => {
    if (editor && editor.getValue() !== newVal) {
      editor.setValue(newVal);
    }
  }
);

watch(
  () => props.fontSize,
  (size) => {
    editor?.updateOptions({ fontSize: size });
  }
);

defineExpose({
  focus: () => editor?.focus(),
  getValue: () => editor?.getValue() || "",
});
</script>

<style scoped>
.code-editor-container {
  height: 100%;
  min-height: 280px;
}
</style>
