class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = collections.defaultdict(set)
        
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        
        wordListSet = set(wordList)
        
        n = len(beginWord)
        for w in [beginWord] + wordList:          # O(wordList length)
            for i in range(n):                    # O(wordLength individual)
                t1,t2 = w[:i],w[i+1:]
                for a in alpha:                   # O(26)
                    new_word = t1 + a + t2
                    if new_word in wordListSet and new_word != w:
                        graph[w].add(new_word)
        def bfs(dictionary,beginWord,endWord):
            explored = []
            queue = [[beginWord]]
            if beginWord == endWord:
                return
            while queue:
                path = queue.pop(0)
                node = path[-1]
                if node in dictionary:
                    neighbours = dictionary[node]
                else: neighbours = []
                for neighbour in neighbours:
                    newPath = list(path)
                    newPath.append(neighbour)
                    queue.append(newPath)
                    if neighbour == endWord:
                        return len(newPath)
                dictionary[node] = []
            return 0
        return(bfs(graph,beginWord,endWord))