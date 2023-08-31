class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        # Create array for max length a tap can reach, intialize at 0
        # Each index of tapReach will indicate the further position reachable from that position
        tapReach = [0] * (n + 1)
        for x, y in enumerate(ranges):
            # These 2 lines remove values out of garden bounds
            left = max(0, x-y)
            right = min(n, x+y)
            # Updates furthest reach for the position at the left index -> [0,1] -> [0,2], [2,3] - > [2,5], etc
            tapReach[left] = max(tapReach[left], right)

        totalTaps = 0
        curIndex = 0
        nextIndex = 0
        for i in range(n + 1):
            # if current index has exceeded the furthest possible reach, then the garden is unwaterable
            if i > nextIndex:
                return -1
            # else if the current index has exceed the current reach, then jump to the next highest point
            if i > curIndex:
                totalTaps += 1
                curIndex = nextIndex
                nextIndex = max(nextIndex, tapReach[i])
        return totalTaps
