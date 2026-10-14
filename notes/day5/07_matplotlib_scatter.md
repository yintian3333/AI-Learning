# 今天解决什么问题
用散点图观察学习时间与成绩的关系，给每个点标上学生姓名，再保存图片。

## dropna() 去掉指定列缺失的值
plot_df = df.dropna(subset=["study_hours", "scores"])
subset：指定检查哪些列。

这些列中只要有一个缺失值，就排除这一行。

结果保存到 plot_df，原来的 df 不变。

2. 绘制散点图：scatter()

plt.scatter(plot_df["study_hours"], plot_df["scores"])

第一个参数：横坐标，学习时间。

第二个参数：纵坐标，成绩。

每位学生对应一个点。

## 3. 用 for 循环逐行取数据

for index, row in plot_df.iterrows():
    print(row["name"])

iterrows()：逐行提供索引标签和行内容。

index：当前行的索引标签。

row：当前行的数据。

冒号下面缩进的代码，对每一行执行一次。

处理 Tom 时：

row["name"]          # "Tom"
row["study_hours"]   # 2
row["scores"]        # 70

下一次循环时，row 会换成下一位学生的数据。

index 和 row 是自己取的变量名，定义和使用时必须一致。

## 4. 给点添加姓名：annotate()
for index, row in plot_df.iterrows():
    plt.annotate(
        row["name"],
        (row["study_hours"], row["scores"]),
        xytext=(5, 5),
        textcoords="offset points"
    )
每次循环，给当前学生对应的点添加姓名。
row["name"]

要显示的文字

(row["study_hours"], row["scores"])

对应点的横、纵坐标

xytext=(5, 5)

文字向右、向上各偏移 5 个点

textcoords="offset points"

使用相对于该坐标的图形尺寸偏移

## 5. 创建文件夹并保存图片

image_dir = project_dir / "images"
image_dir.mkdir(parents=True, exist_ok=True)

image_path = image_dir / "study_hours_scores_day05.png"

plt.tight_layout()
plt.savefig(image_path, dpi=150)

print("图片已保存到：", image_path)

plt.show()
mkdir()：创建文件夹。

parents=True：需要时创建缺少的上层文件夹。

exist_ok=True：文件夹已经存在时，不因此报错。

tight_layout()：自动调整布局，减少标签被裁切的问题。

savefig()：保存当前图表。

dpi=150：设置图片分辨率。

show()：显示图表窗口。