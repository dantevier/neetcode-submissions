class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            anagram_map[tuple(sorted(word))].append(word)
        return [list_of_word for list_of_word in anagram_map.values()]