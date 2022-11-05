class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(nums)-1
        if(target>nums[high]):
            return high+1
        
        while(low<=high):
            mid=(low+high)/2
            if (nums[mid]<target):
                low=mid+1
            else:
                if (nums[mid]==target and nums[mid-1]!=target):
                    return mid
                else:
                    high=mid-1
        return low
        