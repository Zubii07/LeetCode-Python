class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        dict = {}
        for i, num in enumerate(temp):
            if num not in dict:
                dict[num] = i

        ret = []

        for i in nums:
            ret.append(dict[i])

        return ret        
