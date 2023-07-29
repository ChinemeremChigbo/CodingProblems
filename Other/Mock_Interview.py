""""
aaabbcca -> [('a', 3), ('b', 2), ('c', 2), ('a', 1)]
"""

"""
group_char
group_count

iterate over the elements of the string
    if it equals group char then increase count by 1
    if we reach the end or the char is different, then append (char, count), and reset to 0
"""


def compress(string: str) -> list(tuple):
    compressed = []

    if not string:
        return compressed
    count = 0
    group_char = string[0]
    for letter in string:
        if letter != group_char:
            compressed.append((letter, count))
            group_char = letter
            count = 1
        else:
            count += 1
    # compressed.append((group_char, count))
    return compressed

"""
aaabbcc -> [('a', 3), ('b', 2)]
"" -> []
ceee -> [('c', 3('d', 2)]
...
"""

class Solution():
    def __init__(self) -> None:
        self.count = 0
        self.group_char = ""
        self.start = True
        self.strings = {}
        self.contig_start = 0

    def combine(self):
        compressed = []

        if not string:
            return compressed
        
        curr_id = self.contig_start
        while curr_id in self.strings:
            curr_string = self.strings[curr_id]
            curr_id += 1
            for letter, count in curr_string: 
                if letter != self.group_char:
                    compressed.append((letter, self.count))
                    self.group_char = letter
                    self.count = count
                else:
                    self.count += count

            del self.strings[curr_id]
        
        self.contig_start = curr_id + 1
        return compressed

    def compress(self, id: int, string: str) -> list(tuple):
        compressed = []

        if not string:
            return compressed

        if self.start:
            self.group_char = string[0]
            self.start = False

        for letter in string:
            if letter != self.group_char:
                compressed.append((letter, self.count))
                self.group_char  = letter
                self.count = 1
            else:
                self.count += 1
        compressed.append((self.group_char, self.count))
        self.count = 0

        if id == self.contig_start:
            self.strings[id] = compressed
            return combine(self.strings)
        else:
            self.strings[id] = compressed

        return compressed

"""
1 aabb -> [] -> [('a', 2), ('b', 2)]
2 bccc -> [] ["b, 1,  c3]
0 aaa -> [('a', 5), ('b', 3)] -> ["a", 3]
3 cbb -> [('c', 4)]
...
"""