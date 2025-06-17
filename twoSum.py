class Solution:
    def twoSun(self, nums, target):
        for i in range(len(nums)):
            for j in  range(len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

s = Solution()

print(s.twoSun(nums = [1,2,3,4,5], target= 9))
