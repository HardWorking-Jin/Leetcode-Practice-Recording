class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid+1
        return -1


# Test Case1, the answer should be 4
nums1 = [-1,0,3,5,9,12]
target1 = 9

# Test Case2, the answer should be -1
nums2 = [-1,0,3,5,9,12]
target2 = 2

sol = Solution()

answer1 = sol.search(nums1, target1)
print(answer1)

answer2 = sol.search(nums2, target2)
print(answer2)