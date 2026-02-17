class Solution:
    def readBinaryWatch(self, t: int) -> List[str]:
        l = []
        for i in range(12):
            for j in range(60):
                if bin(i).count("1") + bin(j).count("1") == t:
                    l.append(f"{i}:{j:02d}")
        return l