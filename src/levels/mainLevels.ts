import type { LevelType } from "./level.d";

// Vite glob: auto-imports all level*/index.ts and gen*/index.ts modules
// No manual imports needed — scales to 600+ levels
const levelModules = import.meta.glob<{ default: LevelType }>(
  ["./level*/index.ts", "./gen*/index.ts"],
  { eager: true },
);

const mainLevels: LevelType[] = Object.entries(levelModules)
  .map(([path, mod]) => ({ level: mod.default, path }))
  .sort((a, b) => {
    const numA = parseInt(a.path.match(/(\d+)/)?.[1] || "0", 10);
    const numB = parseInt(b.path.match(/(\d+)/)?.[1] || "0", 10);
    return numA - numB;
  })
  .map(({ level }) => level);

export default mainLevels;
