class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rec = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in rec:
                index = rec[diff]
                return [index,i]
            
            rec[nums[i]] = i