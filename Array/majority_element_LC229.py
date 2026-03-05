class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Phase1:
        cand1 = None
        cand2 = None
        count1 = 0
        count2 = 0
        for i in nums:
            if i == cand1:
                count1+=1
            elif i == cand2:
                count2+=1
            elif count1 == 0:
                cand1 = i
                count1 = 1
            elif count2 == 0:
                cand2 = i
                count2 = 1
            else:
                count1-=1
                count2-=1
        # Phase2:
        result = []
        for cand in [cand1, cand2]:
            if cand is not None and nums.count(cand)>n//3:
                result.append(cand)
        return result
