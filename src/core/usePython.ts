import { ref } from "vue";
import {
  initializePyodide,
  executePython,
  isPyodideLoaded,
  type PyodideResult,
} from "./pyodideExecutor";
import { useGlobalStore } from "./globalStore";

export function usePython() {
  const store = useGlobalStore();
  const isExecuting = ref(false);
  const stdout = ref("");
  const stderr = ref("");
  const returnValue = ref<unknown>(undefined);
  const error = ref<string | null>(null);

  async function ensurePyodide(): Promise<void> {
    if (isPyodideLoaded()) return;
    store.pyodideLoading = true;
    await initializePyodide((msg) => {
      stdout.value = msg;
    });
    store.pyodideLoading = false;
    store.pyodideLoaded = true;
  }

  async function run(code: string): Promise<PyodideResult> {
    isExecuting.value = true;
    error.value = null;

    try {
      await ensurePyodide();
      const result = await executePython(code);
      stdout.value = result.stdout;
      stderr.value = result.stderr;
      returnValue.value = result.returnValue;
      error.value = result.error;
      return result;
    } catch (e: unknown) {
      const err = e as Error;
      error.value = err.message || String(e);
      throw e;
    } finally {
      isExecuting.value = false;
    }
  }

  return {
    isExecuting,
    stdout,
    stderr,
    returnValue,
    error,
    ensurePyodide,
    run,
  };
}
