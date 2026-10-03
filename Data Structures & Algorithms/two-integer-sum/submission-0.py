class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmp={}
        
        for i,n in enumerate(nums):
            comp = target - n
            if comp in hashmp:
                return [hashmp[comp],i]
            hashmp[n]=i