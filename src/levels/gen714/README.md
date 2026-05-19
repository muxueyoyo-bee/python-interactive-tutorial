# 第714关: 编写 try/except 错误处理

> 真实案例：pypa/pip 的 `src\pip\_vendor\distlib\resources.py` 中使用了这个模式。

## 概念介绍

健壮的代码用 try/except 优雅地处理异常。

源文件 resources.py 使用了 try/except 捕获多种异常类型。

请仿照此模式编写错误处理代码。

## 代码示例

```python
try:
    result = int('not a number')
    except (ImportError, AttributeError) as e:
        print(f'Caught (ImportError, AttributeError): {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
finally:
    print('Cleanup complete')
```

## 关键点

try: ... except SomeError as e: ... finally: ...

## 常见陷阱

- `except:` 不加异常类型会捕获所有异常(包括 KeyboardInterrupt)，通常不推荐
- `except Exception as e:` 中的 `as e` 可以获取异常对象
- `finally` 无论是否发生异常都会执行

## 你的任务

编写 try/except 块：尝试 int('not a number')，捕获 (ImportError, AttributeError), ImportError, IndexError，并在 finally 中打印 'Cleanup complete'。

预期行为：参考上方代码示例的输出。
