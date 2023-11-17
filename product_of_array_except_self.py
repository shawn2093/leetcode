class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prevprod = 1
        nextprod = 1
        prod_list = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prod_list[i] = prevprod
            else:
                prevprod *= nums[i-1]
                prod_list[i] = prevprod
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1:
                nextprod *= nums[i+1]
                prod_list[i] *= nextprod
        return(prod_list)