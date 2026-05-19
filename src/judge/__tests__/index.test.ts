import { describe, it, expect } from 'vitest';
import { judge, registerJudge } from '../index';

describe('judge (unified entry)', () => {
  it('stdout mode', () => {
    const r = judge('stdout', 'hello\n', 'hello\n');
    expect(r.status).toBe('pass');
  });

  it('return mode', () => {
    const r = judge('return', '42', '42');
    expect(r.status).toBe('pass');
  });

  it('both mode — pass', () => {
    const r = judge('both', 'hello\n', 'hello\n');
    expect(r.status).toBe('pass');
  });

  it('both mode — stdout fails first', () => {
    const r = judge('both', 'wrong', 'correct');
    expect(r.status).toBe('fail');
    expect(r.detail).toContain('第 1 行不匹配');
  });

  it('dataframe mode', () => {
    const r = judge('dataframe', 'a,b\n1,2', 'a,b\n1,2');
    expect(r.status).toBe('pass');
  });

  it('plot mode', () => {
    const r = judge('plot', '__PYODIDE_PLOT__:x', '__PYODIDE_PLOT__:y');
    expect(r.status).toBe('pass');
  });

  it('custom judge — extensibility', () => {
    registerJudge('always-pass' as 'stdout', () => ({
      status: 'pass',
      detail: 'always ok',
    }));
    const r = judge('always-pass' as 'stdout', '', '');
    expect(r.status).toBe('pass');
  });

  it('unknown mode throws', () => {
    expect(() => judge('unknown' as 'stdout', '', '')).toThrow();
  });
});
