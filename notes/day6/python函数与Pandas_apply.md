# Python 函数与 Pandas apply

## 今天解决什么问题

自己定义成绩等级判断函数，再把它应用到成绩列，自动生成等级、统计人数并保存结果。

## 1. 定义和调用函数

def is_passed(score):
    return score >= 60

result = is_passed(85)
print(result)  # True

def：定义函数。

is_passed：函数名，由自己取。

score：参数，接收调用时传入的成绩。

return：返回结果，并结束这次函数调用。

is_passed(85)：调用函数，把 85 传给 score。
定义函数是在记下操作；调用函数时才执行里面的代码。

## 2. return 和 print 的区别

print()：把内容显示在终端。

return：把结果交回调用位置，供后续使用。

def is_passed(score):
    print(score >= 60)

result = is_passed(85)
print(result)

输出：

True
None
## 3. 对整列应用函数：apply()

df["level"] = df["scores"].apply(get_level)

执行过程：

取出 scores 列。

apply() 把每个成绩分别传给 get_level。

收集函数返回的等级。

把结果保存到新列 level。

例如：

98 → get_level(98) → 优秀
88 → get_level(88) → 及格

为什么 get_level 后面不加括号？

get_level(85)

表示现在调用函数。

df["scores"].apply(get_level)

表示把函数交给 Pandas，由它对每个成绩调用。

函数需要先定义，再交给 apply() 使用。

## 4. 统计等级人数：value_counts()

level_counts = df["level"].value_counts()
print(level_counts)

统计每种等级出现的次数，默认按次数从多到少排列。

## 我的理解

函数是把一套操作取个名字，方便重复使用。

apply() 把自己写的函数用于一列中的每个值，避免为每位学生重复写判断代码。

Lucy 的等级基于之前填补的估算成绩，不是实际成绩。


