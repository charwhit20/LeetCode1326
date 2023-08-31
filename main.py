class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        # Enumerate ranges to keep track of i
        ranges = list(enumerate(ranges))
        # Sort by largest range, keep track of i value for range
        ranges.sort(key=lambda x: x[1], reverse=True)
        taps = []
        # clean 0 taps out of ranges, process bounds and append to new taps array
        # x = index, y = value of tap
        for x, y in ranges:
            # if value of tap is 0, break, tap is useless, all further taps are useless
            if y == 0:
                break
            # else, process ranges
            taps.append([x - y, x + y])
        # Create array for all points of garden
        #print(ranges)
        #print(taps)
        # Check right index overlapping or single on furthest right point, set left index to True
        # How to iterate through ranges? while garden unwatered -> for x in ranges process bounds
        # No reason to process bounds multiple times, iterate trhough ranges, create bounds array in same sorting
        totalTaps = 0
        while n > 0:
            # for x in taps, if right range is greater than or equal to n, prevN = n, n = left range, pop x, break
            furthestLeft = n
            for x, y in enumerate(taps):
                if y[1] >= n and y[0] < furthestLeft:
                    furthestLeft = y[0]
            if furthestLeft == n: break
            n = furthestLeft
            totalTaps += 1
        if n <= 0: return totalTaps
        return -1

test = Solution()

# Should output 1
print(test.minTaps(5, [3,4,1,1,0,0]))

# Should output -1
print(test.minTaps(3, [0,0,0,0]))

# Should output 3
print(test.minTaps(7, [1,2,1,0,2,1,0,1]))

# Should output 3
print(test.minTaps(17, [0,3,3,2,2,4,2,1,5,1,0,1,2,3,0,3,1,1]))
