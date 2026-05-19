const PLOT_MARKER_PREFIX = '__PYODIDE_PLOT__:';

export function extractPlots(stdout: string): string[] {
  const plots: string[] = [];
  const regex = new RegExp(`${PLOT_MARKER_PREFIX}([^\\n]+)`, 'g');
  let match: RegExpExecArray | null;
  while ((match = regex.exec(stdout)) !== null) {
    plots.push(match[1]);
  }
  return plots;
}

export function stripPlotMarkers(stdout: string): string {
  const regex = new RegExp(`${PLOT_MARKER_PREFIX}[^\\n]+\\n?`, 'g');
  return stdout.replace(regex, '');
}
