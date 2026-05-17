import pandas as pd
data = {
    "鐢靛奖": ["娴佹氮鍦扮悆", "婊℃睙绾?, "灏佺", "鏃犲悕", "娣辨捣", "闀垮畨涓変竾閲?],
    "璇勫垎": [7.9, 6.7, 7.3, 6.5, 7.6, 8.3],
    "绁ㄦ埧": [46.8, 45.4, 26.3, 9.3, 9.2, 18.2],
}
df = pd.DataFrame(data)
df["鎬т环姣?] = df["绁ㄦ埧"] / df["璇勫垎"]
top = df.sort_values("璇勫垎", ascending=False).head(3)
print(top[["鐢靛奖","璇勫垎","绁ㄦ埧"]].to_string(index=False))
