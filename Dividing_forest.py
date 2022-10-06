# 1 -> pineTree
# 2 -> poplarTree * at least one poplarTree
# 3 -> willowTree

input_forest = [[1,2,3], [2,1,2], [3,1,1]]
input_number = 3

def ways(forest, number):

    # divide into k parts -> need k-1 cuts
    k = number - 1

    # at (cur_i, cur_j) still have k times to cut
    def dp(cur_i, cur_j, k):
        if (cur_i, cur_j, k) in memo:
            return memo[(cur_i, cur_j, k)]

        # Base line - when use k cuts (check whether has poplar tree or not)
        if k == 0:
            if pre_sum[cur_i][cur_j] > 0:
                return 1
            else:
                return 0

        ans = 0

        for i in range(cur_i + 1, m):
            if pre_sum[cur_i][cur_j] - pre_sum[i][cur_j] > 0:
                ans += dp(i, cur_j, k-1)

        for j in range(cur_j+1, n):
            if pre_sum[cur_i][cur_j] - pre_sum[cur_i][j] > 0:
                ans += dp(cur_i, j, k-1)

        memo[(cur_i, cur_j, k)] = ans

        return ans

    memo = {}

    m = len(forest)
    n = len(forest[0])

    pre_sum = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            #cur_sum = right + left - down
            pre_sum[i][j] = pre_sum[i][j+1] + pre_sum[i+1][j] - pre_sum[i+1][j+1] + (1 if forest[i][j] == 2 else 0)

    return dp(0,0,k-1) % (10**9 + 7)

print(ways(input_forest, input_number))