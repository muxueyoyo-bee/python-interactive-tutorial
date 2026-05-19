import { describe, it, expect } from 'vitest';
import { returnJudge } from '../return-judge';

describe('returnJudge', () => {
  it('exact match — both strings', () => {
    const r = returnJudge('hello', 'hello');
    expect(r.status).toBe('pass');
  });

  it('JSON match — same object', () => {
    const r = returnJudge('{"a":1}', '{"a":1}');
    expect(r.status).toBe('pass');
    expect(r.detail).toBe('返回值完全匹配');
  });

  it('JSON mismatch', () => {
    const r = returnJudge('{"a":1}', '{"a":2}');
    expect(r.status).toBe('fail');
  });

  it('type mismatch — number vs string', () => {
    const r = returnJudge('42', '"42"');
    expect(r.status).toBe('fail');
    expect(r.detail).toContain('你的返回值类型是 number');
    expect(r.detail).toContain('期望的返回值类型是 string');
  });
});
