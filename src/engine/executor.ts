import type { ExecuteRequest, MainMessage } from './worker/messages';

export interface PyodideResult {
  stdout: string;
  stderr: string;
  error: string | null;
  returnValue: unknown;
  executionTimeMs: number;
}

export interface ExecuteOptions {
  code: string;
  timeoutMs?: number;
  onProgress?: (msg: string) => void;
}

export function execute(options: ExecuteOptions): Promise<PyodideResult> {
  const timeoutMs = options.timeoutMs ?? 5000;

  return new Promise((resolve, reject) => {
    const worker = new Worker(
      new URL('./worker/worker.ts', import.meta.url),
      { type: 'module' },
    );
    const id = crypto.randomUUID();

    const timeout = setTimeout(() => {
      worker.terminate();
      reject(new Error('代码执行超时（>5秒），请检查是否有死循环'));
    }, timeoutMs);

    worker.onmessage = (e: MessageEvent<MainMessage>) => {
      const msg = e.data;

      if (msg.type === 'progress') {
        options.onProgress?.(msg.msg);
        return;
      }

      if (msg.type === 'result' && msg.id === id) {
        clearTimeout(timeout);
        worker.terminate();
        resolve({
          stdout: msg.stdout,
          stderr: msg.stderr,
          error: msg.error,
          returnValue: msg.returnValue,
          executionTimeMs: msg.executionTimeMs,
        });
      }
    };

    worker.onerror = (e: ErrorEvent) => {
      clearTimeout(timeout);
      worker.terminate();
      reject(new Error(`Worker 错误: ${e.message}`));
    };

    const request: ExecuteRequest = {
      type: 'execute',
      id,
      code: options.code,
      timeoutMs,
    };

    worker.postMessage(request);
  });
}
