class Solution:
    def singleNumber(self, nums: List[int]) -> int:



        counts = {}

        for num in nums:
             counts[num] = counts.get(num,0) + 1
        return next((k for k, v in counts.items() if v == 1))
    