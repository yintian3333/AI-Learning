# 05_pandas多条件筛选和新增列

## 今天解决什么问题
从学生表格中筛选符合条件的人，添加“是否及格”“是否优秀”的标记，并统计人数。

## 多条件筛选
## 1. 并且 &

selected_df = df[
    (df["scores"] > 85) & (df["study_hours"] > 4)
]

含义：成绩大于 85，并且学习时间大于 4 小时，两个条件都满足才保留。

内层 df["列名"]：取出列。

比较运算：生成每行对应的 True/False。

&：组合两个条件。

外层 df[...]：保留条件为 True 的整行。

## 2. 或者 |

either_df = df[
    (df["scores"] > 90) | (df["study_hours"] > 3)
]

含义：成绩大于 90，或者学习时间大于 3 小时，至少满足一个条件就保留。

## 新增列
df["passed"] = df["scores"] >= 60
df["excellent"] = df["scores"] >= 90

>=：大于或等于，包括刚好等于的情况。

passed：是否及格。

excellent：是否优秀。

先计算右边的判断结果，再保存到左边的列。

列不存在时创建新列；列已存在时更新该列。

## 用布尔列筛选
excellent_df = df[df["excellent"]]

excellent 列已经包含 True/False，所以可以直接作为筛选条件。

内层取出标记列，外层保留 True 对应的整行。

## 统计人数
excellent_count = df["excellent"].sum()
passed_count = df["passed"].sum()

print("优秀人数：", excellent_count)
print("及格人数：", passed_count)

布尔列求和时：

True  → 1
False → 0

因此 .sum() 可以统计满足条件的人数。

## 保存今天的结果

output_path = project_dir / "data" / "students_day03.csv"
df.to_csv(output_path, index=False)

保存 df，保留所有学生和新增的标记列。

index=False 表示不把行索引写入文件。

## 我的理解

筛选是根据条件挑选整行；新增列是把判断结果保存到表格中，方便以后筛选和统计。

Lucy 的成绩来自平均值填补，所以她的标记基于估算值，不是实际成绩。