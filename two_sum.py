class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. brute force
        # x = len(nums)
        # for i in range(x):
        #     for j in range(i + 1, x):
        #         if (nums[i] + nums[j] == target):
        #             return ([i, j])
        # return ([])

        # 2. hashmap solution
        # hashmap = {}
        # for i in range(len(nums)):
        #     found = target - nums[i]
        #     if nums[i] in hashmap:
        #         return (hashmap[nums[i]], i)
        #     hashmap[found] = i

        # 3. array
        # hashmap = []
        # for i in range(len(nums)):
        #     found = target - nums[i]
        #     if nums[i] in hashmap:
        #         return (hashmap.index(nums[i]), i)
        #     hashmap.append(found)