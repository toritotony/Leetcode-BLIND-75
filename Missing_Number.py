class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        array = list(range(len(nums) + 1))
        for num in nums:
            if num in array:
                array.remove(num)
        return array[0] 

#################################################################

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return total_sum - actual_sum
