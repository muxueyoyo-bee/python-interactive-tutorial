import type { JudgeOptions, JudgeResult } from './types';

function defaultOptions(opts?: JudgeOptions): Required<JudgeOptions> {
  return {
    trimWhitespace: opts?.trimWhitespace ?? true,
    numericTolerance: opts?.numericTolerance ?? 0,
    ignoreTrailingNewline: opts?.ignoreTrailingNewline ?? true,
    ignoreCase: opts?.ignoreCase ?? false,
    normalizePunctuation: opts?.normalizePunctuation ?? true,
  };
}

function normalizePunctuation(s: string): string {
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

function collapseWhitespace(s: string): string {
  return s.replace(/[ \t]+/g, ' ').trim();
}

function normalizeForComparison(s: string, options: Required<JudgeOptions>): string {
  let result = s;
  if (options.normalizePunctuation) {
    result = normalizePunctuation(result);
  }
  if (options.ignoreCase) {
    result = result.toLowerCase();
  }
  return result;
}

function stripTrailingNewline(s: string): string {
  return s.replace(/\n$/, '');
}

export function stdoutJudge(user: string, answer: string, opts?: JudgeOptions): JudgeResult {
  const options = defaultOptions(opts);

  const userNorm = normalizeForComparison(user, options);
  const answerNorm = normalizeForComparison(answer, options);

  if (userNorm === answerNorm) {
    return { status: 'pass', detail: '输出完全正确' };
  }

  // strip trailing newlines (independent of trimWhitespace)
  if (options.ignoreTrailingNewline) {
    const userStripped = stripTrailingNewline(userNorm);
    const answerStripped = stripTrailingNewline(answerNorm);
    if (userStripped === answerStripped) {
      return { status: 'pass', detail: '忽略尾部换行后匹配' };
    }
  }

  // trim outer whitespace only (does not collapse internal spaces)
  if (options.trimWhitespace) {
    const userTrimmed = userNorm.trim();
    const answerTrimmed = answerNorm.trim();
    if (userTrimmed === answerTrimmed) {
      return { status: 'pass', detail: '忽略首尾空白后匹配' };
    }
    // collapse internal whitespace too
    const userCollapsed = collapseWhitespace(userTrimmed);
    const answerCollapsed = collapseWhitespace(answerTrimmed);
    if (userCollapsed === answerCollapsed) {
      return { status: 'pass', detail: '忽略多余空白后匹配' };
    }
  }

  const userLines = userNorm.split('\n');
  const answerLines = answerNorm.split('\n');
  const maxLines = Math.max(userLines.length, answerLines.length);

  for (let i = 0; i < maxLines; i++) {
    const rawUserLine = userLines[i] ?? '';
    const rawAnswerLine = answerLines[i] ?? '';
    const userLine = options.trimWhitespace ? collapseWhitespace(rawUserLine) : rawUserLine;
    const answerLine = options.trimWhitespace ? collapseWhitespace(rawAnswerLine) : rawAnswerLine;

    if (!compareLines(userLine, answerLine, options)) {
      return {
        status: 'fail',
        detail: `第 ${i + 1} 行不匹配：用户输出 "${rawUserLine}"，期望 "${rawAnswerLine}"`,
        diff: { line: i + 1, user: rawUserLine, expected: rawAnswerLine },
      };
    }
  }

  return { status: 'pass', detail: '逐行比较完全匹配' };
}

function compareLines(userLine: string, answerLine: string, options: Required<JudgeOptions>): boolean {
  if (userLine === answerLine) return true;

  if (options.numericTolerance > 0) {
    const uNum = parseFloat(userLine);
    const aNum = parseFloat(answerLine);
    if (!isNaN(uNum) && !isNaN(aNum)) {
      return Math.abs(uNum - aNum) <= options.numericTolerance;
    }
  }

  return false;
}
