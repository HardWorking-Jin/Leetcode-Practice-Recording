class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(nums, target):
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = left+(right-left)//2
                if nums[mid] > target:
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    return mid
            return -1
        index = binarySearch(nums, target)
        if index == -1:
            return [-1, -1]
        left = index
        right = index
        while left-1 >= 0 and nums[left-1] == target:
            left -= 1
        while right+1 < len(nums) and nums[right+1] == target:
            right+= 1
        return [left, right]

sol = Solution()
nums1 = [5,7,7,8,8,10]
target1 = 8
x = sol.searchRange(nums1, target1)
print(x)