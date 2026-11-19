class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s)!=len(t):
            return False

        freq_counter = defaultdict(int)

        for i in range(len(s)):
            freq_counter[s[i]] += 1
            freq_counter[t[i]] -= 1

        return all(val == 0 for val in freq_counter.values())
