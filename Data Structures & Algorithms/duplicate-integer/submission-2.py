class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        collector = set()
        for i in nums:
            if i in collector:
                return True
            else:
                collector.add(i)
        return False
