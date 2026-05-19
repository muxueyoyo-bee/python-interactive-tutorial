import type { CompareMode, JudgeOptions, JudgeResult } from './types';

type JudgeFn = (user: string, answer: string, opts?: JudgeOptions) => JudgeResult;

const judges = new Map<CompareMode, JudgeFn>();

export function registerJudge(mode: CompareMode, fn: JudgeFn): void {
  judges.set(mode, fn);
}

export function getJudge(mode: CompareMode): JudgeFn {
  const fn = judges.get(mode);
  if (!fn) throw new Error(`No judge registered for mode: ${mode}`);
  return fn;
}

export function judge(mode: CompareMode, user: string, answer: string, opts?: JudgeOptions): JudgeResult {
  return getJudge(mode)(user, answer, opts);
}
