import mainLevels from "./mainLevels";
import customLevels from "./customLevels";
import type { LevelType } from "./level.d";

export const allLevels: LevelType[] = [...mainLevels, ...customLevels];

export { mainLevels, customLevels };
export type { LevelType, CompareMode, LevelCategory } from "./level.d";

export function getLevelByKey(key: string): LevelType {
  return (
    allLevels.find((level) => level.key === key) || allLevels[0]
  );
}

export function getNextLevel(currentLevel: LevelType): LevelType | null {
  const idx = allLevels.findIndex((l) => l.key === currentLevel.key);
  if (idx < 0 || idx >= allLevels.length - 1) return null;
  return allLevels[idx + 1];
}

export function getPrevLevel(currentLevel: LevelType): LevelType | null {
  const idx = allLevels.findIndex((l) => l.key === currentLevel.key);
  if (idx <= 0) return null;
  return allLevels[idx - 1];
}
