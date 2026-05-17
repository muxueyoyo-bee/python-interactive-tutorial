export type CompareMode = "stdout" | "return" | "both" | "dataframe" | "plot";

export type LevelCategory =
  | "基础语法"
  | "中级"
  | "进阶"
  | "数据分析"
  | "AI基础"
  | "AI进阶"
  | "Transformer"
  | "搭建模型"
  | "实战";

export interface LevelType {
  key: string;
  title: string;
  category: LevelCategory;
  description: string;
  content: string;
  defaultCode: string;
  answer: string;
  hint: string;
  type: "main" | "custom";
  difficulty: 1 | 2 | 3 | 4 | 5;
  compareMode: CompareMode;
  setupCode?: string;
  tags: string[];
}
