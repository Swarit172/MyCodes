class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start=0
        end=x
        while(start+1<end):
            mid=(start+end)//2
            if (mid*mid==x):
                return int(mid)
            elif (mid*mid<x):
                start=mid
            else:
                end=mid
                
        if(end*end==x):
            return int(end)
        else:
            return int(start)
        