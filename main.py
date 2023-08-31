class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        tapReach = [0] * (n + 1)
        for x, y in enumerate(ranges):
            left, right = max(0, x-y), min(n, x+y)
            tapReach[left] = max(tapReach[left], right)
        totalTaps = curIndex = nextIndex = 0
        for i in range(n + 1):
            if i > nextIndex: return -1
            if i > curIndex:
                totalTaps += 1; curIndex = nextIndex
            nextIndex = max(nextIndex, tapReach[i])
        return totalTaps
