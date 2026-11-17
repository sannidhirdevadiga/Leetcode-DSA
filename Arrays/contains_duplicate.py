class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


nums = [1, 2, 3, 1]

solution = Solution()
print(solution.containsDuplicate(nums))