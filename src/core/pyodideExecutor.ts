// Pyodide singleton — Python execution engine in browser via WebAssembly

const PYODIDE_VERSION = "0.26.4";
const PYODIDE_CDN = `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/pyodide.js`;

interface PyodideRuntime {
  runPython(code: string): unknown;
  runPythonAsync(code: string): Promise<unknown>;
  loadPackage(names: string[], options?: { messageCallback?: (msg: string) => void }): Promise<void>;
  setStdout(options: { batched: (text: string) => void }): void;
  setStderr(options: { batched: (text: string) => void }): void;
  globals: Map<string, unknown>;
  loadedPackages: Record<string, string>;
}

declare var loadPyodide: (options: {
  indexURL: string;
  stdout?: (text: string) => void;
  stderr?: (text: string) => void;
}) => Promise<PyodideRuntime>;

export interface PyodideResult {
  stdout: string;
  stderr: string;
  error: string | null;
  executionTimeMs: number;
  returnValue: unknown;
}

let pyodideInstance: PyodideRuntime | null = null;
let initPromise: Promise<void> | null = null;
let stdoutBuf: string[] = [];
let stderrBuf: string[] = [];

function collectStdout(text: string) {
  stdoutBuf.push(text);
}

function collectStderr(text: string) {
  stderrBuf.push(text);
}

export function getPyodide(): PyodideRuntime | null {
  return pyodideInstance;
}

export function isPyodideLoaded(): boolean {
  return pyodideInstance !== null;
}

export async function initializePyodide(
  onProgress?: (msg: string) => void
): Promise<void> {
  if (pyodideInstance) return;
  if (initPromise) return initPromise;

  initPromise = (async () => {
    // Inject pyodide script tag if not already present
    if (typeof loadPyodide === "undefined") {
      onProgress?.("正在加载 Pyodide 引擎...");
      await new Promise<void>((resolve, reject) => {
        const script = document.createElement("script");
        script.src = PYODIDE_CDN;
        script.onload = () => resolve();
        script.onerror = () =>
          reject(new Error("Pyodide CDN 加载失败，请检查网络连接"));
        document.head.appendChild(script);
      });
    }

    onProgress?.("正在初始化 Python 运行时...");
    pyodideInstance = await loadPyodide({
      indexURL: `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`,
    });

    // Use batched stdout/stderr for proper line-by-line capture
    pyodideInstance.setStdout({ batched: collectStdout });
    pyodideInstance.setStderr({ batched: collectStderr });

    // Preload commonly used data science packages
    onProgress?.("正在预加载 numpy, pandas, matplotlib...");
    await pyodideInstance.loadPackage(["numpy", "pandas", "matplotlib", "scikit-learn"]);

    // Ensure UTF-8 stdout encoding for Chinese output
    pyodideInstance.runPython(`
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
`);

    // Setup matplotlib capture hook for Phase 4 data science levels
    pyodideInstance.runPython(`
import functools
_plot_count = 0

def _setup_matplotlib_capture():
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import io
        import base64

        original_show = plt.show
        def _capture_show(*args, **kwargs):
            buf = io.BytesIO()
            plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
            buf.seek(0)
            encoded = base64.b64encode(buf.read()).decode('utf-8')
            plt.clf()
            print(f'__PYODIDE_PLOT__:{encoded}')
        plt.show = _capture_show
    except ImportError:
        pass
`);

    onProgress?.("Pyodide 就绪");
  })();

  return initPromise;
}

export async function executePython(
  code: string
): Promise<PyodideResult> {
  if (!pyodideInstance) {
    throw new Error("Pyodide not initialized. Call initializePyodide() first.");
  }

  stdoutBuf = [];
  stderrBuf = [];

  const startTime = performance.now();

  let error: string | null = null;
  let returnValue: unknown = undefined;

  try {
    returnValue = pyodideInstance.runPython(code);
  } catch (e: unknown) {
    const err = e as Error;
    error = err.message || String(e);
  }

  const executionTimeMs = Math.round(performance.now() - startTime);

  return {
    stdout: stdoutBuf.join(""),
    stderr: stderrBuf.join(""),
    error,
    executionTimeMs,
    returnValue,
  };
}

export async function resetPyodide(): Promise<void> {
  pyodideInstance = null;
  initPromise = null;
  stdoutBuf = [];
  stderrBuf = [];
  await initializePyodide();
}

export function getPlotBase64(stdout: string): string[] {
  const plots: string[] = [];
  const regex = /__PYODIDE_PLOT__:([^\n]+)/g;
  let match;
  while ((match = regex.exec(stdout)) !== null) {
    plots.push(match[1]);
  }
  return plots;
}

export function stripPlotMarkers(stdout: string): string {
  return stdout.replace(/__PYODIDE_PLOT__:[^\n]+\n?/g, "");
}
