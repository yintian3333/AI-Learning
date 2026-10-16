# Day 7：用函数整理数据处理流程


## 今天解决什么问题

把“读取数据 → 排除缺失行 → 添加等级”封装成函数，方便重复调用。

## 1. 定义数据处理函数

def prepare_students(csv_path):
    df = pd.read_csv(csv_path)

    clean_df = df.dropna(
        subset=["study_hours", "scores"]
    ).copy()

    clean_df["level"] = clean_df["scores"].apply(get_level)

    return clean_df

需要提前导入 Pandas，并在调用时已经定义好 get_level()。

执行过程：

csv_path 接收传入的文件路径。

read_csv() 读取数据。

dropna() 排除学习时间或成绩缺失的行。

copy() 创建一份独立的结果表格，供后面修改。

apply(get_level) 为每个成绩判断等级。

return clean_df 返回处理后的表格。

## 2. 传入路径，接收表格

project_dir = Path(__file__).resolve().parent.parent
input_path = project_dir / "data" / "students.csv"

students = prepare_students(input_path)

调用时：

外面的 input_path
    ↓ 传入
函数参数 csv_path
    ↓
读取和处理文件
    ↓ return
外面的 students 接收结果

函数可以返回文字、数字、布尔值，也可以返回 DataFrame。
