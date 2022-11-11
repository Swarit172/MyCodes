class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not str:
            return ""
        sub=min(strs,key=len) #shortest value of each item
        for i,ele in enumerate(sub):
            for left in strs:
                if (left[i] != ele):
                    return sub[:i] 
        return sub
        
            