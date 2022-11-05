class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a=[]
        # for i in nums:
        #     if i in a:
        #         continue
        #     else:
        #         a.append[i]
        # return len(a)
        x = 1
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[x] = nums[i+1]
                x+=1
        return(x)