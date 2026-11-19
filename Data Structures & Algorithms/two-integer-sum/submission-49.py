class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = []
        for i, num in enumerate(nums):
            indexed_nums.append((num,i))
        indexed_nums.sort()

        left = 0 
        right = len(indexed_nums) - 1
        total = 0
        while left<right:
            total = indexed_nums[left][0]+indexed_nums[right][0] 
            if total == target:
                return sorted([indexed_nums[left][1],indexed_nums[right][1]])
            elif total > target:
                right-=1
            else: 
                left+=1
            
            
