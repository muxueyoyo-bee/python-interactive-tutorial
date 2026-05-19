import { describe, it, expect } from 'vitest';
import { dataframeJudge } from '../dataframe-judge';

describe('dataframeJudge', () => {
  it('exact match', () => {
    const r = dataframeJudge('a,b\n1,2', 'a,b\n1,2');
    expect(r.status).toBe('pass');
    expect(r.detail).toBe('数据框输出完全匹配');
  });

  it('whitespace normalization — line level', () => {
    const r = dataframeJudge('  a,b  \n  1,2  ', 'a,b\n1,2');
    expect(r.status).toBe('pass');
  });

  it('row count mismatch', () => {
    const r = dataframeJudge('a\nb\nc', 'a\nb');
    expect(r.status).toBe('fail');
    expect(r.detail).toContain('你的输出 3 行');
    expect(r.detail).toContain('预期 2 行');
  });

  it('content mismatch', () => {
    const r = dataframeJudge('a,b\n1,2', 'a,b\n3,4');
    expect(r.status).toBe('fail');
    expect(r.detail).toBe('数据框输出不匹配');
  });
});
