import { defineStore } from "pinia";
import { allLevels } from "../levels";

export interface LevelProgress {
  completed: boolean;
  code: string;
  attempts: number;
  solvedAt?: string;
}

export const useGlobalStore = defineStore("global", {
  state: () => ({
    currentLevelKey: "level1",
    mainLevelProgress: {} as Record<string, LevelProgress>,
    customLevelProgress: {} as Record<string, LevelProgress>,
    settings: {
      fontSize: 16,
      autoRun: false,
      editorMinimap: false,
    },
    pyodideLoaded: false,
    pyodideLoading: false,
  }),

  getters: {
    currentLevel(state) {
      const found = allLevels.find((l) => l.key === state.currentLevelKey);
      return found || allLevels[0];
    },

    currentLevelIndex(state) {
      return allLevels.findIndex((l) => l.key === state.currentLevelKey);
    },

    isLastMainLevel(): (state: any) => boolean {
      return (state: any) => {
        const mainLevels = allLevels.filter((l) => l.type === "main");
        const lastKey = mainLevels[mainLevels.length - 1]?.key;
        return state.currentLevelKey === lastKey;
      };
    },

    prevLevel(state) {
      const idx = allLevels.findIndex((l) => l.key === state.currentLevelKey);
      if (idx <= 0) return null;
      return allLevels[idx - 1];
    },

    nextLevel(state) {
      const idx = allLevels.findIndex((l) => l.key === state.currentLevelKey);
      if (idx >= allLevels.length - 1) return null;
      return allLevels[idx + 1];
    },

    totalCompleted(state) {
      return Object.values(state.mainLevelProgress).filter((p) => p.completed)
        .length;
    },

    isCurrentLevelCompleted(state) {
      return (
        state.mainLevelProgress[state.currentLevelKey]?.completed || false
      );
    },
  },

  actions: {
    setCurrentLevelKey(key: string) {
      this.currentLevelKey = key;
    },

    completeLevel(key: string, code: string) {
      const progress = this.mainLevelProgress[key] || {
        completed: false,
        code: "",
        attempts: 0,
      };
      this.mainLevelProgress[key] = {
        ...progress,
        completed: true,
        code,
        attempts: progress.attempts + 1,
        solvedAt: new Date().toISOString(),
      };
    },

    recordAttempt(key: string, code: string) {
      const progress = this.mainLevelProgress[key] || {
        completed: false,
        code: "",
        attempts: 0,
      };
      this.mainLevelProgress[key] = {
        ...progress,
        code,
        attempts: progress.attempts + 1,
      };
    },

    getSavedCode(key: string): string {
      return this.mainLevelProgress[key]?.code || "";
    },

    reset() {
      this.$reset();
    },
  },

  persist: {
    key: "python-mother-state",
    storage: window.localStorage,
  },
});
