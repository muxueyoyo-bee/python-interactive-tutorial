// Lazy-load README content via Vite glob import
const readmeModules = import.meta.glob<{ default: string }>(
  "./level*/README.md",
  { query: "?raw", import: "default" }
);

const contentCache: Record<string, string> = {};

export async function loadContent(levelKey: string): Promise<string> {
  if (contentCache[levelKey]) return contentCache[levelKey];

  const path = `./${levelKey}/README.md`;
  const loader = readmeModules[path];
  if (!loader) return "";

  const content = await loader();
  contentCache[levelKey] = content;
  return content;
}
