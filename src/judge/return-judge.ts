import type { JudgeOptions, JudgeResult } from './types';

function normalize(s: string): string {
  return s
    .replace(/，/g, ',')
    .replace(/、/g, ',')
    .replace(/。/g, '.')
    .replace(/；/g, ';')
    .replace(/：/g, ':')
    .replace(/？/g, '?')
    .replace(/！/g, '!')
    .replace(/（/g, '(')
    .replace(/）/g, ')')
    .replace(/【/g, '[')
    .replace(/】/g, ']')
    .replace(/‘/g, "'")
    .replace(/’/g, "'")
    .replace(/“/g, '"')
    .replace(/”/g, '"')
    .replace(/ /g, ' ');
}

export function returnJudge(userRaw: string, answerRaw: string, opts?: JudgeOptions): JudgeResult {
  const normalizePunctuation = opts?.normalizePunctuation ?? true;
  let userParsed: unknown;
  let answerParsed: unknown;
  let userParseOk = false;
  let answerParseOk = false;

  try {
    userParsed = JSON.parse(userRaw);
    userParseOk = true;
  } catch {
    // fall back to string comparison
  }

  try {
    answerParsed = JSON.parse(answerRaw);
    answerParseOk = true;
  } catch {
    // fall back to string comparison
  }

  if (userParseOk && answerParseOk) {
    const userType = typeof userParsed;
    const answerType = typeof answerParsed;

    if (userType !== answerType) {
      return {
        status: 'fail',
        detail: `你的返回值类型是 ${userType}，期望的返回值类型是 ${answerType}`,
      };
    }

    const userSerialized = JSON.stringify(userParsed);
    const answerSerialized = JSON.stringify(answerParsed);

    if (userSerialized === answerSerialized) {
      return { status: 'pass', detail: '返回值完全匹配' };
    } else {
      return {
        status: 'fail',
        detail: '返回值不匹配',
        diff: { line: 0, user: userRaw, expected: answerRaw },
      };
    }
  }

  const userStr = normalizePunctuation ? normalize(userRaw) : userRaw;
  const answerStr = normalizePunctuation ? normalize(answerRaw) : answerRaw;

  if (userStr === answerStr) {
    return { status: 'pass', detail: '返回值完全匹配' };
  }

  return {
    status: 'fail',
    detail: '返回值不匹配',
    diff: { line: 0, user: userRaw, expected: answerRaw },
  };
}
