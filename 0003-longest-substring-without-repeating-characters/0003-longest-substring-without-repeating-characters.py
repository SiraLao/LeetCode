class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        s_l = len(s)

        for index, i in enumerate(s):
            n = index + 1

            loop_longest = i
            while n < s_l:
                if s[n] not in loop_longest:
                    loop_longest += s[n]
                else:
                    break
                n+=1
            if len(loop_longest) > len(longest):
                longest = loop_longest

        return len(longest)