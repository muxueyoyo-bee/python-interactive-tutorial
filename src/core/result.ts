export const enum JudgeStatus {
  DEFAULT = -1,
  ERROR = 0,
  SUCCEED = 1,
}

export const STATUS_TEXT: Record<number, string> = {
  [JudgeStatus.DEFAULT]: "未执行",
  [JudgeStatus.ERROR]: "❌ 答案错误",
  [JudgeStatus.SUCCEED]: "✅ 回答正确",
};

export type CompareMode = "stdout" | "return" | "both" | "dataframe" | "plot";

export interface JudgeResult {
  status: JudgeStatus;
  userStdout: string;
  answerStdout: string;
  detail: string;
}

/**
 * Judge user output against expected answer output.
 */
export function judge(
  userStdout: string,
  answerStdout: string,
  userReturn: unknown,
  answerReturn: unknown,
  compareMode: CompareMode
): JudgeResult {
  const trimmedUser = userStdout.trim();
  const trimmedAnswer = answerStdout.trim();

  switch (compareMode) {
    case "stdout":
      return compareStdout(trimmedUser, trimmedAnswer);

    case "return":
      return compareReturn(userReturn, answerReturn);

    case "both":
      return compareBoth(trimmedUser, trimmedAnswer, userReturn, answerReturn);

    case "dataframe":
      return compareDataframe(trimmedUser, trimmedAnswer);

    case "plot":
      return comparePlot(trimmedUser, trimmedAnswer);

    default:
      return compareStdout(trimmedUser, trimmedAnswer);
  }
}

function compareStdout(user: string, answer: string): JudgeResult {
  if (user === answer) {
    return {
      status: JudgeStatus.SUCCEED,
      userStdout: user,
      answerStdout: answer,
      detail: "输出完全匹配",
    };
  }
  return {
    status: JudgeStatus.ERROR,
    userStdout: user,
    answerStdout: answer,
    detail: "输出不匹配，请仔细对比你的输出和预期输出",
  };
}

function compareReturn(user: unknown, answer: unknown): JudgeResult {
  const userJson = JSON.stringify(user);
  const answerJson = JSON.stringify(answer);

  if (userJson === answerJson) {
    return {
      status: JudgeStatus.SUCCEED,
      userStdout: `返回值: ${userJson}`,
      answerStdout: `返回值: ${answerJson}`,
      detail: "返回值完全匹配",
    };
  }
  return {
    status: JudgeStatus.ERROR,
    userStdout: `你的返回值: ${userJson}`,
    answerStdout: `预期返回值: ${answerJson}`,
    detail: "返回值不匹配",
  };
}

function compareBoth(
  userStdout: string,
  answerStdout: string,
  userReturn: unknown,
  answerReturn: unknown
): JudgeResult {
  const stdoutMatch = userStdout === answerStdout;
  const returnMatch =
    JSON.stringify(userReturn) === JSON.stringify(answerReturn);

  if (stdoutMatch && returnMatch) {
    return {
      status: JudgeStatus.SUCCEED,
      userStdout: `${userStdout}\n返回值: ${JSON.stringify(userReturn)}`,
      answerStdout: `${answerStdout}\n返回值: ${JSON.stringify(answerReturn)}`,
      detail: "输出和返回值均匹配",
    };
  }
  const issues: string[] = [];
  if (!stdoutMatch) issues.push("输出内容不匹配");
  if (!returnMatch) issues.push("返回值不匹配");
  return {
    status: JudgeStatus.ERROR,
    userStdout: `${userStdout}\n返回值: ${JSON.stringify(userReturn)}`,
    answerStdout: `${answerStdout}\n返回值: ${JSON.stringify(answerReturn)}`,
    detail: issues.join("；"),
  };
}

function compareDataframe(user: string, answer: string): JudgeResult {
  // Normalize whitespace and compare CSV-like output
  const normalize = (s: string) =>
    s
      .split("\n")
      .map((line) => line.trim())
      .filter((line) => line.length > 0)
      .join("\n");

  if (normalize(user) === normalize(answer)) {
    return {
      status: JudgeStatus.SUCCEED,
      userStdout: user,
      answerStdout: answer,
      detail: "数据框输出完全匹配",
    };
  }
  return {
    status: JudgeStatus.ERROR,
    userStdout: user,
    answerStdout: answer,
    detail: "数据框输出不匹配",
  };
}

function comparePlot(user: string, answer: string): JudgeResult {
  const userHasPlot = user.includes("__PYODIDE_PLOT__:");
  const answerHasPlot = answer.includes("__PYODIDE_PLOT__:");

  if (userHasPlot && answerHasPlot) {
    return {
      status: JudgeStatus.SUCCEED,
      userStdout: user,
      answerStdout: answer,
      detail: "图表生成成功",
    };
  }
  if (!userHasPlot) {
    return {
      status: JudgeStatus.ERROR,
      userStdout: user,
      answerStdout: answer,
      detail: "未检测到图表输出，请确认你调用了绘图函数",
    };
  }
  return {
    status: JudgeStatus.ERROR,
    userStdout: user,
    answerStdout: answer,
    detail: "图表生成不完整",
  };
}
