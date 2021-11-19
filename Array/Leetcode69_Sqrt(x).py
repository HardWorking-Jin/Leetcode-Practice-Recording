class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x+1

        while left < right:
            mid = (left+right)//2
            if mid*mid > x:
                right = mid
            elif mid*mid < x:
                left = mid+1
            else:
                return mid
        return left-1

sol = Solution()

# Test Case1, answer should be 1
x1 = 1
answer1 = sol.mySqrt(x1)
print(answer1)

# Test Case2, answer should be 2
x2 = 5
answer2 = sol.mySqrt(x2)
print(answer2)

# Test Case3, answer should be 3
x3 = 11
answer3 = sol.mySqrt(x3)
print(answer3)

# Test Case4, answer should be 0
x4 = 0
answer4 = sol.mySqrt(x4)
print(answer4)


