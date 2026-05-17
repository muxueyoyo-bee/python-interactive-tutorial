# 量化实战: 股票均线分析

> 涉及主线知识: 第40关 pandas读取数据, 第41关 groupby, 第5关 列表

## 场景

你在一家量化基金工作, 老板让你分析某股票的近期走势。均线(Moving Average)是最基础的技术指标 -- 计算过去N天的平均收盘价, 平滑价格波动。

## 移动均线原理

- **MA5**: 过去5天收盘价的平均值, 反应短期趋势
- **MA10**: 过去10天平均值, 反应中期趋势
- **金叉**: MA5从下方上穿MA10 -> 买入信号
- **死叉**: MA5从上方下穿MA10 -> 卖出信号

## pandas rolling 用法

```python
df['ma5'] = df['close'].rolling(window=5).mean()
df['ma10'] = df['close'].rolling(window=10).mean()
```

rolling(5) 创建一个长度为5的滑动窗口, .mean() 计算窗口内的均值。前4行会是NaN(数据不够5个)。

## 你的任务

生成20天随机股价数据, 计算MA5和MA10, 用 dropna() 去掉NaN行, 打印结果。

> 提示: `np.cumsum(np.random.randn(20)) + 100` 可以生成随机游走的价格序列。
