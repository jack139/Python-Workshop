## 程序流程2



### for 循环

```python

for letter in 'Python':
    print(letter)


for i in [1, 2, 3, 4]:
    print(i)

for i in range(4):
    print(i+1)


fruits = ["banana", "apple", "mango"]

for fruit in fruits:
    print (fruit)

for i in range(len(fruits)):
    print (fruits[i])

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
