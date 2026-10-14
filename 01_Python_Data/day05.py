from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# 找到项目根目录
project_dir = Path(__file__).resolve().parent.parent

# 读取原始数据
csv_path = project_dir / "data" / "students.csv"
df = pd.read_csv(csv_path)

# 本次只使用学习成绩和成绩都不缺失的行
plot_df = df.dropna(subset = ["study_hours","scores"])

print("用于画图的数据:")
print(plot_df)

# 横坐标是学习时间,纵坐标是成绩.
plt.scatter(plot_df["study_hours"],plot_df["scores"])

plt.title("Study Hours and Scores")
plt.xlabel("Study Hours")
plt.ylabel("Score")

for index, row in plot_df.iterrows():
    plt.annotate(
        row["name"],
        (row["study_hours"], row["scores"]),
        xytext = (5, 5),
        textcoords = "offset points"
    )

# 设置图片文件夹的位置
image_dir = project_dir / "images"

# 文件夹不存在就创建
image_dir.mkdir(parents = True,exist_ok = True)

# 设置图片保存位置
image_path = image_dir / "study_hours_scores_day05.png"

# 调整布局并保存图片
plt.tight_layout()
plt.savefig(image_path,dpi = 150)

print("图片已保存到:",image_path)

plt.show()