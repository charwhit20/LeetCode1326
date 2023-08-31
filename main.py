class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        # since you are sorting by furthest left anyways, why not just convert ranges to actual ranges, then sort it
        # by the left index, iterate from the left when finding valid taps, break upon first encounter
        #ranges.sort(key=lambda x: x[1], reverse=True)
        taps = []
        for x, y in enumerate(ranges):
            # instead of break, continue, since it is not sorted
            if y == 0:
                continue
            taps.append([x - y, x + y])
        #msort from left index
        taps.sort(key=lambda x: x[0])
        totalTaps = 0
        while n > 0:
            prevN = n
            for x in range(len(taps)):
                if taps[x][1] >= n:
                    n = taps[x][0]
                    totalTaps += 1
                    break
            # if no tap found, break look
            if prevN == n:
                break
        if n <= 0: return totalTaps
        return -1
