class Solution:
    def maxArea(self, height: List[int]) -> int:
        prevol = 0
        L, R = 0, len(height) - 1
        while L < R:
            width = R - L
            volcalc = min(height[L], height[R]) * width
            prevol = max(prevol, volcalc)
            if height[L] <= height[R]:
                L += 1
            else:
                R -= 1
        return prevol