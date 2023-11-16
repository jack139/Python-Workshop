from copy import deepcopy

'''
布局存储格式:
s = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 0]]
'''


# 在 s 找 x 的位置
def x_pos(s, x):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j]==x:
                return i, j
    return None


# 生成 s 所有可能的下一步布局
def moves(s):
    m = []
    row, col = x_pos(s, 0)

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


# 横向打印一组布局
def print_grid(ss):
    for i in range(3):
        l = []
        for n in range(len(ss)):
            l.append(''.join([str(x) for x in ss[n][i]]))
        print(' '.join(l))
    print()


# 从 target_idx 开始回溯历史布局
def find_history(grids, target_idx):
    p = [target_idx]
    while p[0]!=-1:
        p = [grids[p[0]][1]] + p
    return [grids[i][0] for i in p[1:]]


# 计算两个布局的差异
def grid_diff(s1, s2):
    diff = 0
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            if s1[i][j] != s2[i][j]:
                diff += 1
    return diff


# 计算两个布局的距离（需要移动的步数）
def grid_distance(s1, s2):
    dist = 0
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            i2, j2 = x_pos(s2, s1[i][j])
            dist += (abs(i-i2) + abs(j-j2))
    return dist


#############################################################


# 广度有限搜索 Breadth First Search 
def bfs(start, end):
    grids = [(start, -1)] # (布局, 父节点索引)
    queue = [0] # 队列（使用grids的索引）

    while len(queue)>0:
        grid_s = [x[0] for x in grids]

        if end in grid_s: # 是否已完成？
            target_idx = grid_s.index(end)
            history = find_history(grids, target_idx)
            return history, len(grids)

        node = queue[0] # FIFO 先进先出
        queue = queue[1:] # node 移出队列

        # 生成新布局
        for i in moves(grids[node][0]):
            if i not in grid_s: # 跳过 队列中的
                grids.append((i, node))
                queue.append(len(grids)-1)

    return [], len(grids)


# 深度优先搜索 Depth First Search 
def dfs(start, end, max_depth=5):
    grids = [(start, -1, 0)] # (布局, 父节点索引, 深度)
    stack = [0] # 栈（使用grids的索引）

    while len(stack)>0:
        stack_s = [grids[x][0] for x in stack]

        if end in stack_s: # 是否已完成？
            target_idx = stack[stack_s.index(end)]
            history = find_history(grids, target_idx)
            return history, len(grids)

        node = stack.pop() # LIFO 后进先出
        depth = grids[node][2]

        if depth>max_depth: # 是否超多最大深度？
            continue

        history = find_history(grids, node)

        # 生成新布局
        for i in moves(grids[node][0]):
            if i not in stack_s+history: # 跳过栈中的+历史路径的
                grids.append((i, node, depth+1))
                stack.append(len(grids)-1)

    return [], len(grids)


# 贪婪搜索 Greedy search
def greedy(start, end, cost_fn):
    grids = [(start, -1)]
    queue = [0]

    while len(queue)>0:
        grid_s = [x[0] for x in grids]

        if end in grid_s:
            target_idx = grid_s.index(end)
            history = find_history(grids, target_idx)
            return history, len(grids)

        # 选择代价最小的节点
        min_cost = 1e8
        p = 0
        for n, x in enumerate(queue):
            x_dist = cost_fn(grids[x][0], end) # 预估代价
            if x_dist < min_cost:
                min_cost = x_dist
                p = n

        node = queue[p]
        queue = queue[:p] + queue[p+1:]  # node 移出队列

        # 生成新布局
        for i in moves(grids[node][0]):
            if i not in grid_s:
                grids.append((i, node))
                queue.append(len(grids)-1)

    return [], len(grids)


# A* 搜索
def Astar(start, end, cost_fn):
    grids = [(start, -1, 0)] # (布局, 父节点索引, 深度)
    queue = [0]

    while len(queue)>0:
        grid_s = [x[0] for x in grids]

        if end in grid_s:
            target_idx = grid_s.index(end)
            history = find_history(grids, target_idx)
            return history, len(grids)

        # 选择代价最小的节点
        min_cost = 1e8
        p = 0
        for n, x in enumerate(queue):
            x_dist = cost_fn(grids[x][0], end) + grids[x][2] # 代价+深度
            if x_dist < min_cost:
                min_cost = x_dist
                p = n

        node = queue[p]
        queue = queue[:p] + queue[p+1:]
        depth = grids[node][2]

        # 生成新布局
        for i in moves(grids[node][0]):
            if i not in grid_s:
                grids.append((i, node, depth+1))
                queue.append(len(grids)-1)

    return [], len(grids)




# 测试
if __name__ == '__main__':

    start = [[7, 1, 3],
             [2, 4, 5],
             [8, 6, 0] ]

    end   = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0] ]

    print("BFS", "-"*80)
    r, size = bfs(start, end)
    print(f"total grids={size}\tdepth={len(r)}")
    print_grid(r)
    
    print("DFS", "-"*80)
    r, size = dfs(start, end, 15)
    print(f"total grids={size}\tdepth={len(r)}")
    print_grid(r)

    print("Greedy diff", "-"*80)
    r, size = greedy(start, end, grid_diff)
    print(f"total grids={size}\tdepth={len(r)}")
    print_grid(r)

    print("Greedy distance", "-"*80)
    r, size = greedy(start, end, grid_distance)
    print(f"total grids={size}\tdepth={len(r)}")
    print_grid(r)

    print("A-star diff", "-"*80)
    r, size = Astar(start, end, grid_diff)
    print(f"total grids={size}\tdepth={len(r)}")
    print_grid(r)

    print("A-star distance", "-"*80)
    r, size = Astar(start, end, grid_distance)
    print(f"total grids={size}\tdepth={len(r)}")
    print_grid(r)
