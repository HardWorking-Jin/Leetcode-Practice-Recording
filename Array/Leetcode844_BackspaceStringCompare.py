class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def manipulateString(string):
            new_string = []
            for char in string:
                if char != '#':
                    new_string.append(char)
                elif new_string:
                        new_string.pop()
            return new_string
        
        new_s = manipulateString(s)
        new_t = manipulateString(t)
        
        if new_s == new_t:
            return True
        else:
            return False

sol = Solution()

# Test Case1, answer should be True
s1 = "ab#c"
t1 = "ad#c"
ans1 = sol.backspaceCompare(s1, t1)
print(ans1)

# Test Case2, answer should be True
s2 = "ab##"
t2 = "c#d#"
ans2 = sol.backspaceCompare(s2, t2)
print(ans2)

# Test Case3, answer should be True
s3 = "a##c"
t3 = "#a#c"
ans3 = sol.backspaceCompare(s3, t3)
print(ans3)

# Test Case4, answer should be False
s4 = "a#c"
t4 = "b"
ans4 = sol.backspaceCompare(s4, t4)
print(ans4)
