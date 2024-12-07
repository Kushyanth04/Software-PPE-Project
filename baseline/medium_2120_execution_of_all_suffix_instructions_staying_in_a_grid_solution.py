from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        l = len(s)
        ans = [0] * l

        for i in range(l):
            cnt = 0
            y, x = startPos

            for c in s[i:]:
                if c == "U":
                    y -= 1
                elif c == "D":
                    y += 1
                elif c == "R":
                    x += 1
                else:
                    x -= 1

                if x >= n or y >= n or x < 0 or y < 0:
                    break
                cnt += 1

            ans[i] = cnt
        
        return ans