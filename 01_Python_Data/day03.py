from pathlib import Path
import pandas as  pd

# 找到项目根目录
project_dir = Path(__file__).resolve().parent.parent

# 找到昨天清理后的数据文件
csv_path = project_dir / "data" / "students_cleaned.csv"

# 读取文件，保存为表格
df = pd.read_csv(csv_path)

print("学生数据:")
print(df)

selected_df = df[
    (df["scores"] > 85) & (df["study_hours"] > 4)
]

print("\n 成绩大于85且学习时间大于4小时的学生:")
print(selected_df)

either_df = df[
    (df["scores"] > 90) | (df["study_hours"] < 2)
]

print("\n成绩大于90,或者学习成绩少于俩小时的学生")
print(either_df)

df["passed"] = df["scores"]  >= 60

print("\n添加标记后的表格")
print(df) 

df["excellent"] = df["scores"] > 90
excellent_df = df[df["excellent"]]

print("\n优秀学生:")
print(excellent_df)


excellent_cout = df["excellent"].sum()
print("\n优秀学生人数:",excellent_cout)

passed_cout = df["passed"].sum()
print("\n校及格人数:",passed_cout)

output_path = project_dir / "data" / "students_day03.csv"

# 保存包含passed和excellent 列的表格
df.to_csv(output_path,index = False)

print("\n第三天的数据已保存到:",output_path)