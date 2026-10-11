class Solution:
    def isAnagram(self, s: str, t: str):
        s = sorted(s)
        t = sorted(t)
        if t == s:
            return True
        return False