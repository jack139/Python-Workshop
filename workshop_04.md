## 程序流程2



### for 循环

```python
for letter in 'Python':
    print(letter)   # 按字母输出： P、y、t、h、o、n
```



```python
for i in [1, 2, 3, 4]:
    print(i)        # 输出 1、2、3、4

for i in range(4):  # range() 生成 0～4
    print(i+1)      # 输出 1、2、3、4

for i in range(1, 5):   # range() 生成 1～4
    print(i)            # 输出 1、2、3、4

for i in range(4, 0, -1):   # range() 生成 4～1
    print(i)                # 输出 4、3、2、1
```



```python
fruits = ["banana", "apple", "mango"]

for fruit in fruits:
    print (fruit)

for i in range(len(fruits)):
    print (fruits[i])

for i, fruit in enumerate(fruits): # enumerate生成 序号 和 值
    print (i, fruit)
```



### while 循环

```python
i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    else:
        print(i)    # 输出双数2、4、6、8、10
```



```python
i = 1
while 1:            # 循环条件为1必定成立： 无限循环
    i += 1
    if i > 10:      # 当i大于10时跳出循环
        break
    if i%2 > 0:     # 非双数时跳过输出
        continue
    else:
        print(i)    # 输出双数2、4、6、8、10
```
