class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a_pointer = 0
        b_pointer = 0
        max_length = 0
        hash_set = set()
        
        while b_pointer < len(s):
            if s[b_pointer] not in hash_set:
                hash_set.add(s[b_pointer])
                b_pointer += 1
                max_length = max(len(hash_set), max_length)
            else:
                hash_set.remove(s[a_pointer])
                a_pointer += 1
                
        return max_length
