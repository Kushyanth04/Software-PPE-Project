from typing import List


class Solution:

    def minFlips(self, mat: List[List[int]]) -> int:
        global n_0, target, curr_steps, answer

        m = len(mat)
        n = len(mat[0])
        
        n_0 = 0 
        target = n * m

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    n_0 += 1

        if n_0 == target:
            return 0

        curr_steps = 0
        answer = float('inf')

        def flip(i, j):
            global n_0, target, curr_steps

            mat[i][j] = 1 - mat[i][j]
            
            if mat[i][j] == 0: n_0 += 1
            else: n_0 -= 1

            if i+1 < m:
                mat[i+1][j] = 1 - mat[i+1][j]
                if mat[i+1][j] == 0: n_0 += 1
                else: n_0 -= 1

            if j+1 < n:
                mat[i][j+1] = 1 - mat[i][j+1]
                if mat[i][j+1] == 0: n_0 += 1
                else: n_0 -= 1

            if i-1 >= 0:
                mat[i-1][j] = 1 - mat[i-1][j]
                if mat[i-1][j] == 0: n_0 += 1
                else: n_0 -= 1

            if j-1 >= 0:
                mat[i][j-1] = 1 - mat[i][j-1] 
                if mat[i][j-1] == 0: n_0 += 1
                else: n_0 -= 1

        def next_pos(i, j):
            if j+1 < n:
                return (i, j+1)
            elif i+1 < m:
                return (i+1, 0)
            else:
                return (-1, -1)

        def backtrack(curr_pos):
            global n_0, target, curr_steps, answer

            if n_0 == target:
                answer = min(answer, curr_steps)
                return 

            if curr_pos == (-1, -1):
                return

            i = curr_pos[0]
            j = curr_pos[1]

            next_p = next_pos(i, j)

            # test not flipping curr_pos
            backtrack(next_p)

            # test flipping curr_pos
            flip(i, j)
            curr_steps += 1

            backtrack(next_p)

            curr_steps -= 1            
            flip(i, j)


        backtrack( (0,0) )

        if answer == float('inf'):
            return -1

        return answer