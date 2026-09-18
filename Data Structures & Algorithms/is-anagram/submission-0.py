class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # save each letter in s in map
        # save each letter in t in map
        # .equals on both of them

        sMap = {}
        tMap = {}
        for char in s:
            sMap[char] = sMap.get(char, 0) + 1
        for char in t:
            tMap[char] = tMap.get(char, 0) + 1
        
        return sMap == tMap