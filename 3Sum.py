class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
               
        nums.sort()
        
        # [-4,-1, -1, 0,1,2]
        
        if len(nums)<3:
            return []
        if len(nums)==3:
            if sum(nums)==0:
                return [nums]
            else:
                return []
        
        ans=[]
        for p1 in range(len(nums)-1):
            if nums[p1]>0:
                break
            p2=p1+1
            p3=len(nums)-1
            while p2<p3:
                
                if p1-1>=0:
                    if nums[p1]==nums[p1-1]:
                        break
                if nums[p2]+nums[p3]+nums[p1]== 0:
                    if ans.count([nums[p1],nums[p2],nums[p3]])==0:
                        ans.append([nums[p1],nums[p2],nums[p3]])
                    p2=p2+1
                    p3=p3-1
                elif nums[p2]+nums[p3]>(nums[p1]*-1):
                    p3=p3-1
                else:
                    p2=p2+1
                    
        return ans
