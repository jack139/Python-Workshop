## 编程实践1 : 计算器



### 目标和要求

- 实现正整数运算：加、减、乘、除
- 程序中只能使用加1和减1运算
- 以函数形式提供运算功能



### 加

```python
def add(a, b):
    s = a
    for i in range(1, b+1):
        s = s + 1
    return s
```



### 减

```python
def minus(a, b):
    s = a
    for i in range(1, b+1):
        s = s - 1
    return s
```



### 乘

```python
def multiple(a, b):
    s = a
    for i in range(1, b):
        s = add(s, a)
    return s
```



### 除

```python
def divide(a, b):
    s = a
    d = 0
    while s >= b:
        d = d + 1
        s = minus(s, b)
    return d, s
```

