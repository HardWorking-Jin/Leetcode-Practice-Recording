class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        j = 0
        size = len(fruits)
        basket = {}
        res = 0
        
        for i in range(size):
            if fruits[i] in basket: # Add new tree into dictionary and count the number
                basket[fruits[i]] += 1
            else:
                basket[fruits[i]] = 1
            
            
            while len(basket) >2: # delete previous tree until there are only 2 trees
                basket[fruits[j]] -= 1
                if basket[fruits[j]] == 0:
                    del basket[fruits[j]]
                j += 1
            
            res = max(res, i-j+1) # after updating tree until only 2 species in basket, compare new array length with recorded the largest
        
        return res

sol = Solution()

# Test case1, answer should be 5
fruits1 = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
ans1 = sol.totalFruit(fruits1)
print(ans1)
