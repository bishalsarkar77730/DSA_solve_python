s = "abcabcbb"
length = []
max_length = len(length)
for char in s:
    if char not in length:
        length.append(char)
        if max_length < len(length):
            max_length = len(length)
    else:
        del length[:length.index(char) + 1]
        length.append(char)
print(max_length)


#  Leet Code Solution
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         length = []
#         max_length = len(length)
#         for char in s:
#             if char not in length:
#                 length.append(char)
#                 if max_length < len(length): max_length = len(length)
#             else:
#                 del length[:length.index(char) + 1]
#                 length.append(char)
#         return max_length
