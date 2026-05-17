import md from "./README.md?raw";
import answer from "./answer.py?raw";
import type { LevelType } from "../level.d";

const level: LevelType = {
  key: "bank-interest",
  title: "银行复利计算器",
  category: "实战",
  description: "计算每年本金按复利增长的结果",
  content: md,
  defaultCode: 'def compound_interest(principal, rate, years):\n    # TODO: 逐年计算复利, 打印每年末金额\n    total = principal\n    # for y in range(1, years+1):\n    #     total *= (1 + rate)\n    return total\n\nresult = compound_interest(10000, 0.03, 5)\n# TODO: 打印总收益\n',
  answer,
  hint: '你存了10000元到银行, 年利率3%。用函数实现复利计算, 打印每年末的本息合计。...',
  type: "custom",
  difficulty: 2,
  compareMode: "stdout",
  tags: ['函数', '数学', '循环'],
};

export default level;
