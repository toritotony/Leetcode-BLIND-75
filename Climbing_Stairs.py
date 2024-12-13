class Solution:
    def climbStairs(self, n: int) -> int:
        m = 0
        array = [0,1]
        while m < n:
            array = [array[1], (array[0] + array[1])]
            m += 1
        return array[1]