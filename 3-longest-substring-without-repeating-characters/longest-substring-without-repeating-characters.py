class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_occurrence = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            if s[right] in last_occurrence and last_occurrence[s[right]] >= left:
                left = last_occurrence[s[right]] + 1
            last_occurrence[s[right]] = right
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
        return max_length
            