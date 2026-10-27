class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        mappa = {}
        for number, occurence in count.items():
            if occurence in mappa:
                mappa[occurence].append(number)
            else:
                mappa[occurence] = [number]
        sorted_mappa = sorted(mappa.items(), reverse=True)
        result = []
        for i in range(len(sorted_mappa)):
            for number in sorted_mappa[i][1]:
                result.append(number)
                if len(result) == k:
                    return result
        return result