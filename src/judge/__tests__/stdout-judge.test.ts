import { describe, it, expect } from 'vitest';
import { stdoutJudge } from '../stdout-judge';

describe('stdoutJudge', () => {
  it('exact match', () => {
    const r = stdoutJudge('hello\n', 'hello\n');
    expect(r.status).toBe('pass');
    expect(r.detail).toBe('输出完全正确');
  });

  it('trim whitespace match', () => {
    const r = stdoutJudge('  hello  ', 'hello');
    expect(r.status).toBe('pass');
    expect(r.detail).toBe('忽略首尾空白后匹配');
  });

  it('trailing newline ignored', () => {
    const r = stdoutJudge('hello\n', 'hello');
    expect(r.status).toBe('pass');
    expect(r.detail).toBe('忽略尾部换行后匹配');
  });

  it('line mismatch with diff', () => {
    const r = stdoutJudge('line1\nwrong\nline3', 'line1\ncorrect\nline3');
    expect(r.status).toBe('fail');
    expect(r.diff).toBeDefined();
    expect(r.diff!.line).toBe(2);
    expect(r.diff!.user).toBe('wrong');
    expect(r.diff!.expected).toBe('correct');
  });

  it('numeric tolerance — within range', () => {
    const r = stdoutJudge('3.14', '3.140', { numericTolerance: 0.01 });
    expect(r.status).toBe('pass');
  });

  it('numeric tolerance — outside range', () => {
    const r = stdoutJudge('3.14', '3.16', { numericTolerance: 0.01 });
    expect(r.status).toBe('fail');
  });

  it('multiline — numeric tolerance with multiple lines', () => {
    const r = stdoutJudge('3.14\n2.71', '3.141\n2.718', { numericTolerance: 0.01 });
    expect(r.status).toBe('pass');
  });

  it('line count mismatch', () => {
    const r = stdoutJudge('a\nb\nc', 'a\nb');
    expect(r.status).toBe('fail');
    expect(r.diff!.line).toBe(3);
  });

  it('ignoreCase', () => {
    const r = stdoutJudge('Hello', 'hello', { ignoreCase: true });
    expect(r.status).toBe('pass');
  });

  it('case sensitive by default', () => {
    const r = stdoutJudge('Hello', 'hello');
    expect(r.status).toBe('fail');
  });

  it('custom options — exact only', () => {
    const r = stdoutJudge(' hello ', 'hello', {
      trimWhitespace: false,
      ignoreTrailingNewline: false,
    });
    expect(r.status).toBe('fail');
  });

  it('normalizes Chinese punctuation to English', () => {
    const r = stdoutJudge('你好，世界。', '你好,世界.');
    expect(r.status).toBe('pass');
  });

  it('normalizes fullwidth brackets and quotes', () => {
    const r = stdoutJudge('结果：（成功）', '结果:(成功)');
    expect(r.status).toBe('pass');
  });

  it('normalizes mixed punctuation in multiline', () => {
    const r = stdoutJudge('第一行：结果\n第二行（确认）', '第一行:结果\n第二行(确认)');
    expect(r.status).toBe('pass');
  });

  it('disables punctuation normalization when set false', () => {
    const r = stdoutJudge('你好，世界', '你好,世界', {
      normalizePunctuation: false,
    });
    expect(r.status).toBe('fail');
  });

  it('normalizes non-breaking space to regular space', () => {
    const r = stdoutJudge('hello world', 'hello world');
    expect(r.status).toBe('pass');
  });

  it('tolerates extra spaces within lines', () => {
    const r = stdoutJudge('hello   world', 'hello world');
    expect(r.status).toBe('pass');
  });

  it('passes when only punctuation differs', () => {
    const r = stdoutJudge('答案是：42！', '答案是:42!');
    expect(r.status).toBe('pass');
  });
});
