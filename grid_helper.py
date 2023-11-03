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

    if col < 2: # 左
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
def print_result(start, end, grids, parent):
    print("total grids=", len(grids))
    #print("target idx=", grids.index(end))
    p = [end]
    while p[0]!=start:
        _p = grids.index(p[0])
        p = [parent[_p]] + p
    #print("parents:", p)
    print_grid(p)


# 测试
def test():
    s = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 5]
    ]

    print_grid([s])

    s2 = moves(s)

    print_grid(s2)


if __name__ == '__main__':
    test()