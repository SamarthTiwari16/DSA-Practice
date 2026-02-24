# Using build-in
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0
        for i in accounts:
            rich = max(rich, sum(i))
        return rich
    
# Without using built-in
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0
        for i in accounts:
            total = 0
            for j in i:
                total+=j
            if total > rich:
                rich = total
        return rich
