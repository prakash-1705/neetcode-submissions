class Solution:
    def subset(self,nums,curr,index,result):
        if index == len(nums):
            result.append(curr[:])
            return
        curr.append(nums[index])
        self.subset(nums,curr,index+1,result)
        curr.pop()
        self.subset(nums,curr,index+1,result)
    def subsets(self, nums):
        curr=[]
        result=[]
        index=0
        self.subset(nums,curr,index,result)
        return result

        