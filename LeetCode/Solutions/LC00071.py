class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//", "/").replace("/", " ").split()
        path = [i for i in path if i != "."]
        while ".." in path:
            index = path.index("..")
            if index == 0: path.pop(0)
            else:
                path = path[:index-1]+path[index+1:]
        return "/" + "/".join(path)