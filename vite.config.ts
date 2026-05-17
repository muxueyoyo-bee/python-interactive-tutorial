import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import monacoEditorPlugin from "vite-plugin-monaco-editor";

export default defineConfig({
  plugins: [
    vue({
      include: [/\.vue$/, /\.md$/],
    }),
    monacoEditorPlugin({
      languageWorkers: ["editorWorkerService"],
    }),
  ],
  base: "./",
  build: {
    target: "es2020",
    rollupOptions: {
      output: {
        manualChunks: {
          monaco: ["monaco-editor"],
          antd: ["ant-design-vue"],
        },
      },
    },
  },
  optimizeDeps: {
    exclude: ["monaco-editor"],
  },
});
