## 代码实现

### 1. 工具函数

```python
# 计算两个布局间的差异
def grid_diff(s1, s2):
    diff = 0
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            if s1[i][j] != s2[i][j]:
                diff += 1
    return diff

# 计算两个布局间的距离
def grid_distance(s1, s2):
    # 返回 x 的位置
    def x_pos(s, x):
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j]==x:
                    return i, j
        return None

    dist = 0
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            i2, j2 = x_pos(s2, s1[i][j])
            dist += (abs(i-i2) + abs(j-j2))
    return dist
```



### 2. 贪心算法

```python
def greedy(start, end, cost_fn):
    grids = [(start, -1)] # 保存全部布局, (布局, 父节点)
    queue = [0] # 队列，是grid的索引

    while len(queue)>0:
        grid_s = [x[0] for x in grids]
        if end in grid_s:
            target_idx = grid_s.index(end)
            print_result(grids, target_idx) # 输出结果
            return 1

        # 找出代价最小的节点
        min_cost = 1e8
        p = 0
        for n, x in enumerate(queue):
            x_dist = cost_fn(grids[x][0], end) #预期代价
            if x_dist < min_cost:
                min_cost = x_dist
                p = n

        node = queue[p] # 最小代价节点作为当前节点
        queue = queue[:p] + queue[p+1:]  # 删除已出队列的元素

        # 生成新布局
        for i in moves(grids[node][0]):
            if i not in grid_s: # 剔除已存在的布局
                grids.append((i, node))
                queue.append(len(grids)-1)
    return 0
```



### 3. A\*算法

```python
def Astar(start, end, cost_fn):
    grids = [(start, -1, 0)] # 保存全部布局, (布局, 父节点, 深度)
    queue = [0] # 队列，是grid的索引

    while len(queue)>0:
        grid_s = [x[0] for x in grids]
        #print_grid(grid_s)

        if end in grid_s:
            target_idx = grid_s.index(end)
            print_result(grids, target_idx) # 输出结果
            return 1

        # 找出代价最小的节点
        min_cost = 1e8
        p = 0
        for n, x in enumerate(queue):
            x_dist = cost_fn(grids[x][0], end) + grids[x][2] # 预期代价 + 已有的
            if x_dist < min_cost:
                min_cost = x_dist
                p = n

        node = queue[p] # 最小代价节点作为当前节点
        queue = queue[:p] + queue[p+1:]  # 删除已出队列的元素
        depth = grids[node][2]

        # 生成新布局
        for i in moves(grids[node][0]):
            if i not in grid_s: # 剔除已存在的布局
                grids.append((i, node, depth+1))
                queue.append(len(grids)-1)

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

r = greedy(start, end, grid_diff)
print(r)

r = greedy(start, end, grid_distance)
print(r)

r = Astar(start, end, grid_diff)
print(r)

r = Astar(start, end, grid_distance)
print(r)
```
