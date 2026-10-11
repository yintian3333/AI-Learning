from pathlib import Path
import pandas as pd

# 根据代码文件的位置，找到项目根目录
project_dir = Path(__file__).resolve().parent.parent

# 读取CSV文件
df = pd.read_csv(project_dir / "data" / "students.csv")

print("学生数据:")
print(df)

print("\n每列缺失数据的数量:")
print(df.isna().sum())

# 计算已有成绩的平均值,mean() 默认跳过缺失值
average_score = df["scores"].mean()
print("\n已有成绩的平均值:",average_score)

# 填补缺失值,再把结果存回scores列.
# py 赋值语句计算规则从右到左,先填入缺失数据再取出scores 
df["scores"] = df["scores"].fillna(average_score)

print("\n填补后的学生数据:")
print(df)

#按成绩从高到低排序
sorted_df = df.sort_values(by = "scores",ascending = False)

print("\n按成绩从高到低排序:")
print(sorted_df)

import matplotlib.pylab as plt

# 成绩高到低排序
score_sorted_df = df.sort_values(by = "scores", ascending = False)

# 用姓名和对应的成绩画柱状图
plt.bar(score_sorted_df["name"], score_sorted_df["scores"])

plt.title("Student Scores")
plt.xlabel("Name")
plt.ylabel("Score")

plt.show()

# 设置输出文件位置
output_path = project_dir / "data" / "students_cleaned.csv"

# 保存按成绩排序的表格
score_sorted_df.to_csv(output_path,index = False)

print("\n处理后的数据已保存到:",output_path)

# 重新读取刚才保存的文件
check_df = pd.read_csv(output_path)

print("\n重新的读取保存的文件:")
print(check_df)

print("\n保存后的缺失值数量:")
# 连续调用方法后一步依赖前一步的结果
print(check_df.isna().sum())


