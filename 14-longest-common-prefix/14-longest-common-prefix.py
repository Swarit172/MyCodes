class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not str:
            return ""
        subs=min(strs,key=len) #shortest value of each item
        for i,ele in enumerate(subs):
            for left in strs:
                if (left[i] != ele):
                    return subs[:i] 
        return subs
        
            