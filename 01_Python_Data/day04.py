from pathlib import Path
import pandas as pd

project_dir = Path(__file__).resolve().parent.parent

# 读取昨天的数据、包含优秀标记的数据
csv_path = project_dir / "data" / "students_day03.csv"
df = pd.read_csv(csv_path)

print("学生数据:")
print(df)

# 按是否优秀分组，计算每组的平均成绩
average_scores = df.groupby("excellent")["scores"].mean()

print("\n各组的平均成绩:")
print(average_scores)

average_hours = df.groupby("excellent")["study_hours"].mean()

print("\n各组的平均学习时间:")
print(average_hours)

max_scores = df.groupby("excellent")["scores"].max()

print("\n各组的最高成绩:")
print(max_scores)

score_summary = df.groupby("excellent")["scores"].agg(
    ["count", "mean", "max", "min"]
)

print("\n各组的成绩统计:")
print(score_summary)

score_summary = score_summary.rename(
    index = {False: "非优秀", True: "优秀"},
    columns = {
        "count":"有效成绩数",
        "mean":"平均分",
        "max":"最高分",
        "min":"最低分"
    }
)

score_summary.index.naem = "组别"

print("\n中文成绩统计表:")
print(score_summary)

output_path = project_dir/"data"/"score_summary.csv"

score_summary.to_csv(
    output_path,
    index = True,
    index_label = "组别",
    encoding = "utf-8-sig"
)

print("\n统计表已保存到:",output_path)