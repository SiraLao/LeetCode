class Solution:
    def isValid(self, s: str) -> bool:
        collection = {')': '(', ']': '[', '}': '{'}

        op = []
        result = True

        for i in s:
            if i in collection.values():
                op.append(i)
            elif i in collection:
                if not op or op[-1] != collection[i]:
                    return False
                op.pop()
            else:
                return False

        return not op