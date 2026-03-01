items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver" # Output: 1

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == 'type':
            idx = 0
        elif ruleKey == 'color':
            idx = 1
        else:
            idx = 2
        count = 0
        for item in items:
            if item[idx] == ruleValue:
                count+=1
        return count