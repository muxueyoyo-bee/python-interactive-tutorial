import pandas as pd
data = {
    "电影": ["流浪地球", "满江红", "封神", "无名", "深海", "长安三万里"],
    "评分": [7.9, 6.7, 7.3, 6.5, 7.6, 8.3],
    "票房": [46.8, 45.4, 26.3, 9.3, 9.2, 18.2],
}
df = pd.DataFrame(data)
df["性价比"] = df["票房"] / df["评分"]
top = df.sort_values("评分", ascending=False).head(3)
print(top[["电影","评分","票房"]].to_string(index=False))
