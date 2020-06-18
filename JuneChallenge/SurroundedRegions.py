# coding=utf-8
"""
June 17 Challenge - Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to
'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""


class SurroundedRegions(object):

    def __init__(self):
        self.circles = set()
        self.border = "border"
        self.visited = set()

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.circles = set()

        def get_circles(i, j):
            # print(i,j)
            if i in [0, len(board) - 1] or j in [0, len(board[0]) - 1]:
                self.circles.add(self.border)
            self.circles.add((i, j))
            self.visited.add((i, j))

            if i - 1 >= 0 and board[i - 1][j] == 'O' and (i - 1, j) not in self.visited:
                get_circles(i - 1, j)
            if i + 1 < len(board) and board[i + 1][j] == 'O' and (i + 1, j) not in self.visited:
                get_circles(i + 1, j)
            if j - 1 >= 0 and board[i][j - 1] == 'O' and (i, j - 1) not in self.visited:
                get_circles(i, j - 1)
            if j + 1 < len(board[0]) and board[i][j + 1] == 'O' and (i, j + 1) not in self.visited:
                get_circles(i, j + 1)

        def mark_circles():
            if self.border not in self.circles:
                for x, y in self.circles:
                    board[x][y] = 'X'
            else:
                self.visited.union(self.circles) - {self.border}

        for l, lst in enumerate(board):
            for n, num in enumerate(lst):
                if num == 'O' and (l, n) not in self.visited:
                    get_circles(l, n)
                    mark_circles()

        return board


"""
More efficient solution

def solve(self, board):
    
        if not board:
            return
        
        M, N = len(board), len(board[0])
        
        # O -> G, Os connected with boundaries
        def dfs(r, c):
            if not(0 <= r < M and 0 <= c < N) or board[r][c] != 'O':
                return
            board[r][c] = 'G'
            for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
                dfs(r + dr, c + dc)
        
        for i in xrange(M): 
            dfs(i, 0)
            dfs(i, N - 1)
        
        for j in xrange(N):
            dfs(0, j)
            dfs(M - 1, j)
        
        for i in xrange(M):
            for j in xrange(N):
                board[i][j] = 'O' if board[i][j] == 'G' else 'X'
"""
