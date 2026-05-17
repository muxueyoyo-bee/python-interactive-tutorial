# 第三十一关: pathlib 路径操作

pathlib 是面向对象的路径处理模块, 比 os.path 更直观.

## Path 对象

```python
from pathlib import Path
p = Path("/home/user/docs/report.pdf")
print(p.name)      # report.pdf  -- 文件名
print(p.suffix)    # .pdf        -- 扩展名
print(p.parent)    # /home/user/docs -- 父目录
```

## 常用属性

| 属性 | 含义 |
|------|------|
| .name | 文件名(含扩展名) |
| .suffix | 扩展名 |
| .parent | 父目录路径 |
| .stem | 文件名(不含扩展名) |

## 你的任务

创建 Path 对象表示 /home/user/docs/report.pdf, 打印文件名, 扩展名和父目录.

预期输出:
```
report.pdf
.pdf
/home/user/docs
```
