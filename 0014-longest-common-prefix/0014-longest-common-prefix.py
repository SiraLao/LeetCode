class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            result = ""
        else:
            prefix = strs[0]
            for word in strs[1:]:
                while not word.startswith(prefix):
                    prefix = prefix[:-1]
                    if not prefix:
                        break
            result = prefix


        return result