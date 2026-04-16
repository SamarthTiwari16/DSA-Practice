num = "52"      # Output: "5"

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for ch in range(len(num)-1, -1, -1):
            if int(num[ch]) % 2 == 1:
                return num[:ch+1]
        return ""
