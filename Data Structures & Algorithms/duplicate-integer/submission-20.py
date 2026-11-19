class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        if not nums:
            return False
        uniqueSet = set()
        for number in nums:
            if number in uniqueSet:
                return True
            uniqueSet.add(number)
        return False