class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum1 = 0
        count = 0
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                sum1 += i
                count += 1  # move count increment inside the condition
        if count == 0:
            return 0
        else:
            average = sum1 // count  # move this here, after count is finalized
            return average

        
