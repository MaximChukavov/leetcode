class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        i, j = 0, len(nums) - 1

        while i < len(nums) and j >= 0:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j -= 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j -= 2
        return nums
