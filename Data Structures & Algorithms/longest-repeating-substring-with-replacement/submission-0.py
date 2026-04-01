class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            # Add the new character to our window's tally
            current_char = s[right]
            count[current_char] = count.get(current_char, 0) + 1

            # Find the actual most frequent character in the CURRENT window
            current_max_freq = max(count.values())

            # If the window is invalid, physically shrink it using a while loop
            if (right - left + 1) - current_max_freq > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1
                
                # Because we removed a character, recalculate the true max frequency
                current_max_freq = max(count.values())

            # The window is guaranteed to be valid.
            # We simply check if this valid window beats our previous high score.
            current_window_size = right - left + 1
            max_length = max(max_length, current_window_size)

        return max_length