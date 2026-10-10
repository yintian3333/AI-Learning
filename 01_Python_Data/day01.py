# ========Numpy==========
import numpy as np


scores = np.array([80, 92, 75, 88, 95])

print('全部成绩:',scores)
print("平均成绩：",scores.mean())
print("最高成绩:",scores.max())
print("最低成绩:",scores.min())
print("大于85分:",scores[scores > 85])


a = np.array([1, 2, 3])
print("一维数组:")
print(a)
print("shape:", a.shape)

b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n二维数组:")
print(b)
print("shape:", b.shape)

# ========pandas========
import pandas as pd
data = {
    "name":["Tom", "Jack", "Alice", "Bob"],
    "study_hours":[2, 5, 4, 1],
    "scores":[70, 95, 88, 60]
}

df = pd.DataFrame(data)

print("\n学生数据:")
print(df)

print("\n平均成绩:")
print(df["scores"].mean())

print("\n成绩大于80:")
print(df[df["scores"]>80])

print("\n学习时间大于3个小时的人:")
print(df[df["study_hours"]>3])

print("\n求平均学习时间:")
print(df["study_hours"].mean())

print("\n最高分:")
print(df["scores"].max())

print("学习时间大于3小时的人的平均成绩:")
print(df[df["study_hours"]>3]["scores"].mean())

import matplotlib.pyplot as plt

plt.bar(df["name"],df["study_hours"])

plt.title("Student Study_hours")
plt.xlabel("Name")
plt.ylabel("study_hours")

plt.show()