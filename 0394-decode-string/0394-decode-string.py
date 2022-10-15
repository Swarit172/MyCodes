class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                sstr=""
                while stack[-1]!="[":
                    sstr=stack.pop() + sstr
                stack.pop()
                
                k=""
                while stack and stack[-1].isdigit():
                    k=stack.pop() + k
                stack.append(int(k)* sstr)
        return "".join(stack)
        