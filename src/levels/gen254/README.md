# 第254关: 定义异常类层级: ResolverException

> 真实案例：pypa/pip 的 `src\pip\_vendor\resolvelib\resolvers\exceptions.py` 中使用了这个模式。

## 概念介绍

好的代码库用自定义异常类让调用方精确捕获不同错误。

源文件 exceptions.py 定义了如下继承层级：
  • ResolverException → Exception
  • RequirementsConflicted → ResolverException, Generic[RT, CT]
  • InconsistentCandidate → ResolverException, Generic[RT, CT]
  • ResolutionError → ResolverException

请按照这个模式编写这些异常类（每个类只需 pass 语句体）。

## 代码示例

```python
class ResolverException(Exception):
    pass
class RequirementsConflicted(ResolverException, Generic[RT, CT]):
    pass
class InconsistentCandidate(ResolverException, Generic[RT, CT]):
    pass
class ResolutionError(ResolverException):
    pass
```

## 关键点

class 子类名(父类名): —— 父类写在括号里，多个父类用逗号分隔

## 常见陷阱

- `__init__` 不是构造器，是初始化方法（构造器是 `__new__`）
- 实例方法的第一个参数必须显式写 `self`
- `pass` 是一个空语句，占位用

## 你的任务

定义以下异常类: ResolverException(Exception), RequirementsConflicted(ResolverException, Generic[RT, CT]), InconsistentCandidate(ResolverException, Generic[RT, CT]), ResolutionError(ResolverException)

预期行为：参考上方代码示例的输出。
