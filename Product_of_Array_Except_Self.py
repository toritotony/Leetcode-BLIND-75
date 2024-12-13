class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create output array size of input array all defaulted to 1
        # initialize prefix and postfix to calculate result value
        # for each value in input array, set current value of output array as prefix 
        # multiply current input array value by prefix and repeat
        # do the same with postfix, start at end and work your way into beginning
        # multiply prefix by postfix during postfix loop, return ouptut array
        result = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result