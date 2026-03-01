class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        for ch in alphabets:
            if ch not in sentence:
                return False
        return True
