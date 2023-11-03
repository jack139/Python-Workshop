from grid_helper import *


# 广度优先 Breadth First Search 
def bfs(start, end):
    grids = [start] # 保存全部布局
    parent = [-1] # 保存对应的父节点
    queue = [(start, 0)] # 队列，第二元素为深度

    while len(queue)>0:
        #print_grid(grids)

        if end in grids:
            print_result(start, end, grids, parent) # 输出结果
            return 1

        node, depth = queue[0] # 先进先出
        queue = queue[1:] # 删除已出队列的元素

        #print("depth=", depth)

        new_leafs = [] # 当前node产生的新布局

        for i in moves(node):
            if i not in grids: # 剔除已存在的布局
                new_leafs.append(i)

        # 新布局加入队列 和 父节点
        grids += new_leafs 
        parent += [node]*len(new_leafs)
        queue += zip(new_leafs, [depth+1]*len(new_leafs)) # 新布局入栈

    return 0



# 深度度优先 Depth First Search 
def dfs(start, end, max_depth=5):
    grids = [start]
    parent = [-1]
    stack = [(start, 0)] # 堆栈，第二元素为深度

    while len(stack)>0:
        #print_grid(grids)
        #print_grid([i[0] for i in stack])

        if end in grids:
            print_result(start, end, grids, parent) # 输出结果
            return 1

        node, depth = stack.pop() # 后进先出

        #print("depth=", depth)

        if depth>max_depth: # 大于最大深度，则反弹
            continue

        new_leafs = []

        for i in moves(node):
            if i not in grids:
                new_leafs.append(i)

        grids += new_leafs
        parent += [node]*len(new_leafs)
        stack += zip(new_leafs, [depth+1]*len(new_leafs)) # 新布局入栈

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


    r = dfs(start, end, 5)
    print(r)

    print("*"*80)

    r = bfs(start, end)
    print(r)
