export interface ExecuteRequest {
  type: 'execute';
  id: string;
  code: string;
  timeoutMs?: number;
}

export interface ExecuteResponse {
  type: 'result';
  id: string;
  stdout: string;
  stderr: string;
  error: string | null;
  returnValue: unknown;
  executionTimeMs: number;
}

export interface ExecuteProgress {
  type: 'progress';
  id: string;
  msg: string;
}

export type WorkerMessage = ExecuteRequest;
export type MainMessage = ExecuteResponse | ExecuteProgress;
