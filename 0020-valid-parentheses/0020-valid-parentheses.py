class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in dict:
                if stack and stack[-1]==dict[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        return True if not stack else False