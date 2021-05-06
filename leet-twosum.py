#finds the index of the two numbers (from the passed list) whose sum results in the target.

class Solution:
    def twoSum(self, nums=None ,target=0):
        if nums is None :
            nums = []
        else :
            self.nums = nums
        self.seen = {}
    
        for i,value in enumerate(self.nums):
            remaining = target - value #self.nums[i] or values is the same thing

            if remaining in self.seen:
                return[self.seen[remaining],i]
            else:
                self.seen[value] = i
                

a = Solution()
print(a.twoSum([3,3],6))
print(a.twoSum([2,7,11,15],9))
print(a.twoSum([3,2,4],6))