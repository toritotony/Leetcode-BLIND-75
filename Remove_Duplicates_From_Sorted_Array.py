class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0      

        k = 1       

        for i in range(k, len(nums)):  # since it's in order we can compare to previous one and only add when its new
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1    

        return k