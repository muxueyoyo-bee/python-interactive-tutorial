import { describe, it, expect } from 'vitest';
import { plotJudge } from '../plot-judge';

describe('plotJudge', () => {
  it('both have plot markers', () => {
    const r = plotJudge(
      'some output\n__PYODIDE_PLOT__:abc123\nmore output',
      'some output\n__PYODIDE_PLOT__:xyz789\nmore output',
    );
    expect(r.status).toBe('pass');
    expect(r.detail).toBe('图表生成成功');
  });

  it('user missing plot', () => {
    const r = plotJudge('no plot here', '__PYODIDE_PLOT__:abc123');
    expect(r.status).toBe('fail');
    expect(r.detail).toContain('未检测到图表输出');
  });

  it('answer missing plot', () => {
    const r = plotJudge('__PYODIDE_PLOT__:abc123', 'no plot here');
    expect(r.status).toBe('fail');
    expect(r.detail).toBe('图表生成不完整');
  });
});
