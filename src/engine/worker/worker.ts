import type { ExecuteRequest, MainMessage } from './messages';

declare function importScripts(...urls: string[]): void;

interface PyodideRuntime {
  runPython(code: string): unknown;
  setStdout(options: { batched: (msg: string) => void }): void;
  setStderr(options: { batched: (msg: string) => void }): void;
}

const PYODIDE_CDN = 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js';

let pyodide: PyodideRuntime | null = null;

async function initPyodide(): Promise<PyodideRuntime> {
  importScripts(PYODIDE_CDN);

  const loadPyodide = (self as unknown as Record<string, unknown>).loadPyodide as
    | ((opts: { indexURL: string }) => Promise<PyodideRuntime>)
    | undefined;

  if (!loadPyodide) {
    throw new Error('Pyodide failed to load: loadPyodide not found');
  }

  return loadPyodide({
    indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/',
  });
}

self.onmessage = async (e: MessageEvent<ExecuteRequest>) => {
  const { id, code } = e.data;
  let stdout = '';
  let stderr = '';

  try {
    if (!pyodide) {
      self.postMessage({ type: 'progress', id, msg: '正在加载 Pyodide...' } satisfies MainMessage);
      pyodide = await initPyodide();
    }

    pyodide.runPython("import sys; sys.modules.pop('__main__', None)");

    pyodide.setStdout({
      batched: (msg: string) => {
        stdout += msg + '\n';
      },
    });
    pyodide.setStderr({
      batched: (msg: string) => {
        stderr += msg + '\n';
      },
    });

    const start = performance.now();
    const returnValue = pyodide.runPython(code);
    const executionTimeMs = Math.round(performance.now() - start);

    self.postMessage({
      type: 'result',
      id,
      stdout,
      stderr,
      error: null,
      returnValue,
      executionTimeMs,
    } satisfies MainMessage);
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : String(err);
    self.postMessage({
      type: 'result',
      id,
      stdout,
      stderr,
      error: message,
      returnValue: null,
      executionTimeMs: 0,
    } satisfies MainMessage);
  }
};
