class Solution:
    def reverse(self, x: int) -> int:
        strx = str(x)
        
        if strx[0] == '-':
            rev = strx[1:]
            rev = rev[::-1]
            rev = '-'+rev
        else:
            rev = strx[::-1]
        revint = int(rev)
        if revint < -2**31 or revint > 2**31 - 1:
            return 0
        return revint