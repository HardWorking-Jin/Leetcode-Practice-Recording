class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid+1

        return right



sol = Solution()

# Test Case1, the answer should be 1
nums1 = [1, 3, 5, 7]
target1 = 2

answer1 = sol.searchInsert(nums1, target1)
print(answer1)

# Test Case2, the answer should be 4
nums2 = [1, 3, 5, 6]
target2 = 7

answer2 = sol.searchInsert(nums2, target2)
print(answer2)

# Test Case3, the answer should be 0
nums3 = [1]
target3 = 1

answer3 = sol.searchInsert(nums3, target3)
print(answer3)

