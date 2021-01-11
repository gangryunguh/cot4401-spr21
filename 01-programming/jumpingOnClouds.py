def jumpingOnCloudsNaive(c):

    def jumps(index):
        if index <= 0:
            return 0

        if c[index] == 1:
            return 10**5

        return min(1+jumps(index-1), 1+jumps(index-2))

    return jumps(len(c)-1)

def jumpingOnCloudsBottomUp(c):

    dp = [0] * len(c)
    dp[1] = 1 if c[1] == 0 else 10**5

    for i in range(2,len(c)):
        if c[i]:
            dp[i] = 10**5
        else:
            dp[i] = min(1+dp[i-1],1+dp[i-2])
    return dp[len(c)-1]

def jumpingOnCloudsTopDown(c):

    dp = dict()
    def jumps(index):
        if index <= 0:
            return 0
        elif c[index]:
            return 10**5
        elif index in dp:
            return dp[index]
        else:
            dp[index] = min(1 + jumps(index - 1), 1 + jumps(index - 2))
            return dp[index]
    return jumps(len(c)-1)

c = [0, 0, 1, 0, 0, 1, 0]
result = jumpingOnCloudsNaive(c)
print(result)

c = [0, 0, 0, 1, 0, 1, 0]
result = jumpingOnCloudsNaive(c)
print(result)


c = [0, 0, 1, 0, 0, 1, 0]
result = jumpingOnCloudsBottomUp(c)
print(result)

c = [0, 0, 0, 1, 0, 1, 0]
result = jumpingOnCloudsBottomUp(c)
print(result)

c = [0, 0, 1, 0, 0, 1, 0]
result = jumpingOnCloudsTopDown(c)
print(result)

c = [0, 0, 0, 1, 0, 1, 0]
result = jumpingOnCloudsTopDown(c)
print(result)