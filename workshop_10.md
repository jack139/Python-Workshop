## 代码实现

### 1. 工具函数

```python
from copy import deepcopy

'''
grid 表示：

s = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
'''

# 返回 0 的位置
def zero_pos(s):
    for i in range(3):
        for j in range(3):
            if s[i][j]==0:
                return i, j
    return None

# 返回 布局s 的所有 下一步
def moves(s):
    m = []
    row, col = zero_pos(s)

    if row > 0: # 上
        m.append(deepcopy(s))
        m[-1][row-1][col], m[-1][row][col] = m[-1][row][col], m[-1][row-1][col]

    if row < 2: # 下
        m.append(deepcopy(s))
        m[-1][row+1][col], m[-1][row][col] = m[-1][row][col], m[-1][row+1][col]

    if col > 0: # 左
        m.append(deepcopy(s))
        m[-1][row][col-1], m[-1][row][col] = m[-1][row][col], m[-1][row][col-1]

    if col < 2: # 右
        m.append(deepcopy(s))
        m[-1][row][col+1], m[-1][row][col] = m[-1][row][col], m[-1][row][col+1]

    return m

# 输出 一组 布局
def print_grid(s):
    for i in range(3):
        l = []
        for n in range(len(s)):
            l.append(''.join([str(x) for x in s[n][i]]))
        print(' '.join(l))
    print()

# 回溯输出结果
def print_result(grids, target_idx):
    print("total grids=", len(grids))
    print("target idx=", target_idx)
    p = [target_idx]
    while p[0]!=-1:
        p = [grids[p[0]][1]] + p
    print("depth=", len(p)-1)
    print_grid([grids[i][0] for i in p[1:]])
```



### 2. 广度优先搜索

```python
# 广度优先 Breadth First Search 
def bfs(start, end):
    grids = [(start, -1)] # 保存全部布局, (布局, 父节点)
    queue = [0] # 队列，是grid的索引

    while len(queue)>0:
        grid_s = [x[0] for x in grids]
        if end in grid_s:
            target_idx = grid_s.index(end)
            print_result(grids, target_idx) # 输出结果
            return 1

        node = queue[0] # 先进先出
        queue = queue[1:] # 删除已出队列的元素

        for i in moves(grids[node][0]):
            if i not in grid_s: # 剔除已存在的布局
                grids.append((i, node))
                queue.append(len(grids)-1)
    return 0
```



### 3. 深度优先搜索

```python
def dfs(start, end, max_depth=5):
    grids = [(start, -1, 0)] # 保存全部布局, (布局, 父节点, 深度)
    stack = [0] # 堆栈，第二元素为深度

    while len(stack)>0:
        stack_s = [grids[x][0] for x in stack]
        if end in stack_s:
            target_idx = stack[stack_s.index(end)]
            print_result(grids, target_idx) # 输出结果
            return 1

        node = stack.pop() # 后进先出
        depth = grids[node][2]

        if depth>max_depth: # 大于最大深度，则反弹
            continue

        for i in moves(grids[node][0]):
            if i not in stack_s: # 剔除已存在的布局
                grids.append((i, node, depth+1))
                stack.append(len(grids)-1)
    return 0
```



### 4. 搜索

```python
start = [
    [7, 1, 3],
    [2, 4, 5],
    [8, 6, 0]
]

end = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

r = bfs(start, end)
print(r)

r = dfs(start, end, 15)
print(r)

```