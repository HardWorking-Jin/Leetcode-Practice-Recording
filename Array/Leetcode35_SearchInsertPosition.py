class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1


        while left <= right:
            if target < nums[left]:
                return left

            if target > nums[right]:
                return right+1

            mid = (left + right) // 2
            print(left, right, mid)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid-1
                print(left, right)
            elif target > nums[mid]:
                left = mid+1
                print(left, right)



sol = Solution()

# Test Case1, the answer should be 0
nums1 = [1, 3, 5, 7]
target1 = 2

answer1 = sol.searchInsert(nums1, target1)
print(answer1)

# Test Case2, the answer should be 4
nums2 = [1, 3, 5, 6]
target2 = 7

answer2 = sol.searchInsert(nums2, target2)
print(answer2)

nums3 = [1]
target3 = 1

answer3 = sol.searchInsert(nums3, target3)
print(answer3)

