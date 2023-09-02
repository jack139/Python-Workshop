## Python 基础



### 一个python程序

```python
PI = 3.14

radius = [1, 2, 3]
result = {}

def circle_area(r):
    area = PI * r ** 2
    return area


for r in radius:
    result[str(r)] = circle_area(r)

print(result)

# {'1': 3.14, '2': 12.56, '3': 28.26}
```



### 关键字、运算符、变量、常量

- 关键字

```text
and or not if elif else for while True False continue 
break pass try except finally raise from import def 
return class lambda del global nonlocal in is None 
assert as with yield 
```

- 运算符

```text
+ - * / % ** //
== != > < >= <=
= += -= *= /= %= **= //=
& | ^ ~ >> <<
and or not in is
```

- 变量

- 常量



### 基本数据结构

- 字符串

```python
s = "ABC-def"
s[1:3] # "BC"
s[-3:] # "def"
len(s) # 7
s.split('-') # ['ABC', 'def']
s.lower() # 'abc-def'
s.upper() # 'ABC-DEF'
s.isalpha() # False
s.isdigit() # False
s.replace('-', '+') # 'ABC+def'
```

- 列表

```python
a = [1, 2, 3, 2]
a[1:3] # [2, 3]
a[-1:] # [2]
a.append(4) # [1, 2, 3, 2, 4]
len(a) # 5
[x+1 for x in a] # [2, 3, 4, 3, 5]
a + [6] # [1, 2, 3, 2, 4, 6]
4 in a # True
5 not in a # True
```


- 元组

```python
c = (1, 2, 3, 2)
c[1:3] # (2, 3)
c[-1:] # (2)
```


- 字典

```python
b = {"a": 1, "b": 2}
b["c"] = 3 # {"a": 1, "b": 2, "c": 3}
list(b.keys()) # ["a", "b", "c"]
[x for x in enumerate(b)] # [(0, 'a'), (1, 'b'), (2, 'c')]
list(b.items()) #[('a', 1), ('b', 2), ('c', 3)]
del b["b"] # {"a": 1, "c":3}
```


- 集合

```python
d = set([1, 2, 3, 2]) # {1, 2, 3}
d.add(4) # {1, 2, 3, 4}
d.add(3) # {1, 2, 3, 4}
d.remove(2) # {1, 3, 4}
```
