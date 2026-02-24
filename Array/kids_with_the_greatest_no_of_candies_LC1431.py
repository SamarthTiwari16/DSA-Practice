class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        maxi = candies[0]
        for i in range(n):
            if candies[i]>maxi:
                maxi = candies[i]
        result = []
        for i in range(n):
            if candies[i] + extraCandies >= maxi:
                result.append(True)
            else:
                result.append(False)
        return result
