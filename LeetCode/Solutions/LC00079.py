class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # dfs
        m = len(board)
        n = len(board[0])
        w = len(word)
        self.found = False
        def dfs(i,j,visited,count):
            if count < w and (i,j) not in visited:
                letter = word[count]
                neighbours = [(a,b) for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if a > -1 and a < m and b > -1 and b < n and (a,b) not in visited and board[a][b] == letter]
                for a,b in neighbours:
                    visited.add((i,j))
                    dfs(a,b,visited,count+1)
                    visited.remove((i,j))
            else:
                self.found = True
                return
        for i,row in enumerate(board):
            for j, l in enumerate(row):
                if l == word[0]:
                    dfs(i,j,set(),1) 
                    if self.found == True:
                        return True
        return False