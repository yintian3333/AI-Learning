def is_passed(score):
    return score >= 60

# 调用函数,并保存返回结果
result = is_passed(55)

if result:
    print("这位学生及格了")

else:
    print("这位学生没及格")

print("是否及格:",result)

def get_result(score):
    if score >= 60:
        return "及格"
    else:
        return "不及格"
print("85分",get_result(85))
print("55分",get_result(55))
print("60分",get_result(55))

def get_level(score):
    if score >= 85:
        return "优秀"
    elif  score >= 60:
        return "及格"
    else:
        return "不及格"

print(get_level(90))  # 优秀
print(get_level(60))  # 及格
print(get_level(59))  # 不及格

from pathlib import Path
import pandas as pd


project_dir = Path(__file__).resolve().parent.parent
csv_path = project_dir / "data" / "students_cleaned.csv"

df = pd.read_csv(csv_path)

# 对每个成绩调用get_level,生成等级列
df["level"] = df["scores"].apply(get_level)

print("\n添加等级后的学生数据:")
print(df)

level_counts = df["level"].value_counts()

print("\n各等级的学生人数:")
print(level_counts)

output_path = project_dir / "data" / "students_day06.csv"

# 保存包含level列的完整学生表格
df.to_csv(output_path, index = False, encoding = "utf-8-sig")

print("\n学生登记表已保存到",output_path)