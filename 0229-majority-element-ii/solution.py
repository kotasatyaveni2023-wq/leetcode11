class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        limit = len(nums) // 3
        ans = []

        for key, value in freq.items():
            if value > limit:
                ans.append(key)

        return ans

        
