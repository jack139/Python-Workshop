from grid_helper import *


# 广度优先 Breadth First Search 
def bfs(start, end):
    grids = [(start, -1)] # 保存全部布局, (布局, 父节点)
    queue = [0] # 队列，是grid的索引

    while len(queue)>0:
        #print_grid(grids)

        queue_s = [grids[x][0] for x in queue]
        if end in queue_s:
            target_idx = queue[queue_s.index(end)]
            print_result(grids, target_idx) # 输出结果
            return 1

        node = queue[0] # 先进先出
        queue = queue[1:] # 删除已出队列的元素

        for i in moves(grids[node][0]):
            if i not in queue_s: # 剔除已存在的布局
                grids.append((i, node))
                queue.append(len(grids)-1)

    return 0



# 深度度优先 Depth First Search 
def dfs(start, end, max_depth=5):
    grids = [(start, -1, 0)] # 保存全部布局, (布局, 父节点, 深度)
    stack = [0] # 堆栈，第二元素为深度

    while len(stack)>0:
        #print_grid(grids)

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



if __name__ == '__main__':
    #test()


    '''
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

    end = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]


    r = bfs(start, end)
    print(r)
    print("*"*80)
    r = dfs(start, end, 15)
    print(r)
