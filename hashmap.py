def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # If a duplicate character is found, move the left pointer
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add the current character to the set
        char_set.add(s[right])
        
        # Update the maximum length
        max_len = max(max_len, right - left + 1)

    return max_len

# Example usage
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

print(length_of_longest_substring(s1))  # Output: 3 ("abc")
print(length_of_longest_substring(s2))  # Output: 1 ("b")
print(length_of_longest_substring(s3))  # Output: 3 ("wke")
