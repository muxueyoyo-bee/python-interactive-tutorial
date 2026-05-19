import type { JudgeOptions, JudgeResult } from './types';

function normalize(s: string): string {
  return s
    .split('\n')
    .map(line => line.trim())
    .filter(line => line.length > 0)
    .join('\n');
}

function countRows(s: string): number {
  return s
    .split('\n')
    .filter(line => line.trim().length > 0)
    .length;
}

export function dataframeJudge(user: string, answer: string, _opts?: JudgeOptions): JudgeResult {
  const userRows = countRows(user);
  const answerRows = countRows(answer);

  if (userRows !== answerRows) {
    return {
      status: 'fail',
      detail: `你的输出 ${userRows} 行，预期 ${answerRows} 行`,
    };
  }

  if (normalize(user) === normalize(answer)) {
    return {
      status: 'pass',
      detail: '数据框输出完全匹配',
    };
  }

  return {
    status: 'fail',
    detail: '数据框输出不匹配',
  };
}
