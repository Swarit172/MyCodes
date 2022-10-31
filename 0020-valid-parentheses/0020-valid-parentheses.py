class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = ['N']
        dict = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in dict.keys():
                if stack.pop() != dict[i]:
                    return False
            else:
                stack.append(i)
                
        return len(stack) == 1