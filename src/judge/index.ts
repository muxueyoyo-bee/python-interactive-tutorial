import { judge as judgeFn, getJudge, registerJudge } from './registry';
import { stdoutJudge } from './stdout-judge';
import { returnJudge } from './return-judge';
import { dataframeJudge } from './dataframe-judge';
import { plotJudge } from './plot-judge';
import type { JudgeOptions, JudgeResult } from './types';

registerJudge('stdout', stdoutJudge);
registerJudge('return', returnJudge);
registerJudge('dataframe', dataframeJudge);
registerJudge('plot', plotJudge);

registerJudge('both', (user: string, answer: string, opts?: JudgeOptions): JudgeResult => {
  const stdoutResult = stdoutJudge(user, answer, opts);
  if (stdoutResult.status === 'fail') return stdoutResult;
  return returnJudge(user, answer, opts);
});

export { registerJudge, getJudge };
export { judgeFn as judge };
export type { CompareMode, JudgeOptions, JudgeResult } from './types';
