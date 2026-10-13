# pandas分组统计
## 它解决什么问题

把学生按“优秀”和“非优秀”分组，比较各组的成绩和学习时间。

筛选是挑出符合条件的行；分组统计是分别计算每组的整体情况。

## 1. 分组计算平均成绩

average_scores = df.groupby("excellent")["scores"].mean()

执行顺序：

groupby("excellent")：按 excellent 列分组，True 一组、False 一组。

["scores"]：选择成绩列。

.mean()：分别计算每组的平均成绩。

## 2. 更换统计列或统计方法

# 每组平均学习时间
df.groupby("excellent")["study_hours"].mean()

# 每组最高成绩
df.groupby("excellent")["scores"].max()

# 每组最低成绩
df.groupby("excellent")["scores"].min()

选择的列决定“统计什么数据”，方法决定“怎样统计”。

## 3. 一次计算多个指标：agg()

score_summary = df.groupby("excellent")["scores"].agg(
    ["count", "mean", "max", "min"]
)

agg()用来执行指定的统计操作
列表中的字符串是统计操作名称，在这里不用写成 mean()。

名称

含义

count

非缺失成绩的数量

mean

平均成绩

max

最高成绩

min

最低成绩

结果是一张 DataFrame，每行代表一组，每列代表一个统计指标。

## 4. count() 和 size() 的区别

df.groupby("excellent")["scores"].count()

统计每组中非缺失成绩的数量。

df.groupby("excellent").size()

统计每组的总行数，即每组学生人数。

成绩缺失时，count() 可能小于学生人数；size() 仍会计算这行。

## 5. 修改行标签和列名：rename()

score_summary = score_summary.rename(
    index={False: "非优秀", True: "优秀"},
    columns={
        "count": "有效成绩数",
        "mean": "平均分",
        "max": "最高分",
        "min": "最低分"
    }
)

index=：修改行标签。

columns=：修改列名。

{旧名称: 新名称}：字典，表示对应关系。

rename() 默认返回改名后的表格，需要赋值保存结果。它只改变名称，不改变统计数值。

## 6. 修改索引名称

score_summary.index.name = "组别"

区分：

“非优秀、优秀”是索引中的标签。

“组别”是整个索引的名称。

## 我的理解

分组统计就是先把数据按类别分开，再对每一组执行相同的计算，方便比较。