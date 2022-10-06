# sizes -> list, requirment -> int
def numberUmbrellas(sizes, requirement):
    # dp[people needed to be handle] = min number of Umbrellas to use
    dp = [requirement+1]*(requirement+1)
    dp[0] = 0 # initialize

    # recursion
    for r in range(1, requirement+1):
        for s in sizes:
            if r - s >= 0:
                dp[r] = min(dp[r], 1+dp[r-s])

    return dp[requirement] if dp[requirement] != requirement+1 else -1

print(numberUmbrellas([3,5], 6))
