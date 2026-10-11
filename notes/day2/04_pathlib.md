# pathlib

## 导入方法
from pathlib import Path

## 他解决什么问题
1.拼接文件路径。

2.找到文件所在的文件夹。

3.判断文件是否存在。

4.创建文件夹。

## 常用操作
path() 把路径变成方便操作的路径对象
.resolve() 得到完整的绝对路径
.parent() 找到上一层文件夹
project_dir = Path(__file__).resolve().parent.parent

## 我的理解

Path 就像一个“文件地址工具”，帮助程序准确找到文件位置。