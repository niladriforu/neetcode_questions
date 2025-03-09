from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        curr_length = 0
        left = 0
        for right in range(len(s)):
            frequency[s[right]] += 1
            max_frequency = max(frequency.values())
            curr_length = right - left + 1
            if curr_length - max_frequency > k:
                frequency[s[left]] -= 1
                left += 1
            curr_length = max(curr_length, right - left + 1)
        return curr_length

