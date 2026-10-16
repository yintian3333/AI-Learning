from pathlib import Path
import pandas as pd

# 根据成绩返回等级
def get_level(score):
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

# 读取数据、排除缺失成绩，在添加等级列
def prepare_students(csv_path):
    df = pd.read_csv(csv_path)

    clean_df = df.dropna(
        subset = ["study_hours","scores"]
    ).copy()

    clean_df["level"] = clean_df["scores"].apply(get_level)

    return clean_df

project_dir = Path(__file__).resolve().parent.parent
input_path = project_dir / "data" / "students.csv"

if input_path.exists():
    students = prepare_students(input_path)
    
    print("处理后的学生成绩:")
    print(students)

# 设置输出位置
    output_path = project_dir / "data" / "students07.csv"

# 保存函数返回的表格
    students.to_csv(
        output_path,
        index = False,
        encoding = "utf-8-sig"
    )

    print("\n结果已保存到:",output_path)

else:
    print("找不到数据文件,请检查:",input_path)