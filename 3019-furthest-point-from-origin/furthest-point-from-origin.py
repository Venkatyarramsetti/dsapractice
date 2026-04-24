class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        rc,lc,uc = 0,0,0
        for i in moves:
            if i == 'R':
                rc += 1
            elif i == 'L':
                lc += 1
            else:
                uc += 1
        return abs(rc-lc) + uc