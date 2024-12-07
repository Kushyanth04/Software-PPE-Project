from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        operations = 0
        monostack = [(0, 0)]
        for h in target:
            work = max(0, h - monostack[-1][0])
            while monostack and h >= monostack[-1][0]:
                _, prev_work = monostack.pop()
                operations += prev_work
            monostack.append((h, work))

        while monostack:
            operations += monostack.pop()[1]
        return operations