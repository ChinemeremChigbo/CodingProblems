class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = [matrix[0][0]]
        right = True
        down = False
        left = False
        up = False
        count = 0
        i = 0
        j = 0
        widthLeft = 0
        widthRight = len(matrix[0])
        heightTop = 0
        heightBottom = len(matrix)
        while count < len(matrix)*len(matrix[0])-1:
            if right:
                if i<widthRight-1:
                    i += 1
                    order += [matrix[j][i]]
                    count += 1
                else:
                    heightTop += 1
                    right = False
                    down = True
            elif down:
                if j<heightBottom-1:
                    j += 1
                    order += [matrix[j][i]]
                    count += 1
                else:
                    widthRight -= 1
                    down = False
                    left = True   
            elif left:
                if i>widthLeft:
                    i -= 1
                    order += [matrix[j][i]]
                    count += 1
                else:
                    heightBottom -= 1
                    left = False
                    up = True
            elif up:
                if j>heightTop:
                    j -= 1
                    order += [matrix[j][i]]
                    count += 1
                else:
                    widthLeft += 1
                    up = False
                    right = True
            
        return order