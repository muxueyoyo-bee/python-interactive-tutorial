import type { JudgeOptions, JudgeResult } from './types';

const PLOT_MARKER = '__PYODIDE_PLOT__:';

export function plotJudge(user: string, answer: string, _opts?: JudgeOptions): JudgeResult {
  const userHasPlot = user.includes(PLOT_MARKER);
  const answerHasPlot = answer.includes(PLOT_MARKER);

  if (userHasPlot && answerHasPlot) {
    return {
      status: 'pass',
      detail: '图表生成成功',
    };
  }

  if (!userHasPlot) {
    return {
      status: 'fail',
      detail: '未检测到图表输出，请确认你调用了绘图函数',
    };
  }

  return {
    status: 'fail',
    detail: '图表生成不完整',
  };
}
