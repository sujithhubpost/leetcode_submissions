class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        # Creating a set to store the last positions of occurrence
        seen = {}
        maximum_length = 0
        # starting the initial point of window to index 0
        start = 0
        for end, char in enumerate(string):
            if char in seen:
                start = max(start, seen[char] + 1)
            seen[char] = end
            maximum_length = max(maximum_length, end-start + 1)
        return maximum_length