class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        Scount = Counter(s)
        Tcount = Counter(t)
        return Scount == Tcount