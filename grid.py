from grid_helper import *


# 广度优先 Breadth First Search 
def bfs(start, end):
    grids = [(start, -1)] # 保存全部布局, (布局, 父节点)
    queue = [0] # 队列，是grid的索引

    while len(queue)>0:
        grid_s = [x[0] for x in grids]
        #print_grid(grid_s)

        if end in grid_s:
            target_idx = grid_s.index(end)
            print_result(grids, target_idx) # 输出结果
            return 1

        node = queue[0] # 先进先出
        queue = queue[1:] # 删除已出队列的元素

        # 生成新布局
        for i in moves(grids[node][0]):
            if i not in grid_s: # 剔除已存在的布局
                grids.append((i, node))
                queue.append(len(grids)-1)

    return 0



# 深度度优先 Depth First Search 
def dfs(start, end, max_depth=5):
    grids = [(start, -1, 0)] # 保存全部布局, (布局, 父节点, 深度)
    stack = [0] # 堆栈，第二元素为深度

    while len(stack)>0:
        stack_s = [grids[x][0] for x in stack]
        #print_grid(stack_s)

        if end in stack_s:
            target_idx = stack[stack_s.index(end)]
            print_result(grids, target_idx) # 输出结果
            return 1

        node = stack.pop() # 后进先出
        depth = grids[node][2]

        if depth>max_depth: # 大于最大深度，则反弹
            continue

        # 历史路径
        history = find_history(grids, node)

        # 生成新布局
        for i in moves(grids[node][0]):
            if i not in stack_s+history: # 剔除已存在的布局
                grids.append((i, node, depth+1))
                stack.append(len(grids)-1)

    return 0



# 贪心算法 greedy
def greedy(start, end, cost_fn):
    grids = [(start, -1)] # 保存全部布局, (布局, 父节点)
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
            x_dist = cost_fn(grids[x][0], end) # 预期代价
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



# A*算法
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


if __name__ == '__main__':
    #test()



    start = [
        [7, 1, 3],
        [2, 4, 5],
        [8, 6, 0]
    ]
    '''
    start = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    '''
    end = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]


    print("BFS", "-"*80)

    r = bfs(start, end)
    print(r)

    print("DFS", "-"*80)

    r = dfs(start, end, 15)
    print(r)

    print("Greedy diff", "-"*80)

    r = greedy(start, end, grid_diff)
    print(r)

    print("Greedy distance", "-"*80)

    r = greedy(start, end, grid_distance)
    print(r)

    print("A-star diff", "-"*80)

    r = Astar(start, end, grid_diff)
    print(r)

    print("A-start distance", "-"*80)

    r = Astar(start, end, grid_distance)
    print(r)

