class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(index, open_count, close_count):
            if len(index) == 2*n:
                result.append(index)
                return
            if open_count < n:
                backtrack(index+'(', open_count+1, close_count)
            if close_count < open_count:
                backtrack(index+')', open_count, close_count+1)
        backtrack("", 0, 0)
        return result
