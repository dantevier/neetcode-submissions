class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sortedS=sorted(s)
        sortedT= sorted(t)
        mappaS = {}
        mappaT = {}
        for letteraS, letteraT in zip(sortedS, sortedT):
            mappaS[letteraS] = 1 + mappaS.get(letteraS, 0)
            mappaT[letteraT] = 1 + mappaT.get(letteraT, 0)
        return mappaS == mappaT
