## 编程实践2 : 排序



### 目标和要求

- 对一个数组进行排序：从大到小



### 选择排序

> 时间复杂度 O(n^2)

```python
# 选择排序
def select_sort(a):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a
```



- 调用

```python
import random

a = [i for i in range(10)]
random.shuffle(a)
print(a)
print(select_sort(a))
print(a)

# 输出
# [8, 9, 2, 4, 0, 5, 1, 3, 6, 7]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```



### 快速排序

> 时间复杂度 O(nlogn)。由C.A.R.Hoare（托尼·霍尔）于1960年提出，他曾获1980年图灵奖。

```python
def quick_sort(a):
    if len(a) < 2:
        return a
    mid = a[len(a) // 2]
    left, right = [], []
    a.remove(mid)
    for i in a:
        if i <= mid:
            right.append(i)
        else:
            left.append(i)
    return quick_sort(left) + [mid] + quick_sort(right)
```



- 调用

```python
import random

a = [i for i in range(10)]
random.shuffle(a)
print(a)
print(quick_sort(a))
print(a)

# 输出
# [8, 9, 2, 4, 0, 5, 1, 3, 6, 7]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# [8, 9, 2, 4, 0, 1, 3, 6, 7]

# 思考一下：为什么排序后列表 a 少了一个数？
```



### 一个彩蛋

```python
def q(a):
    return a if len(a) <= 1 else q([i for i in a[1:] if i > a[0]]) + [a[0]] + q([i for i in a[1:] if i <= a[0]])
```
