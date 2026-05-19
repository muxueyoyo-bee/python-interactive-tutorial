export type CompareMode = 'stdout' | 'return' | 'both' | 'dataframe' | 'plot';

export interface JudgeOptions {
  trimWhitespace?: boolean;
  numericTolerance?: number;
  ignoreTrailingNewline?: boolean;
  ignoreCase?: boolean;
  normalizePunctuation?: boolean;
}

export interface JudgeResult {
  status: 'pass' | 'fail';
  detail: string;
  diff?: {
    line: number;
    user: string;
    expected: string;
  };
}
