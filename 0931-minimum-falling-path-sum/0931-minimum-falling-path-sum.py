class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        mem = [[-1 for i in range(len(matrix))] for j in range(len(matrix))] 
        print(mem)
        
        def valid(arr, x, y):
            if x < 0 or x >= len(arr) or y < 0 or y >= len(arr):
                return False
            return True
        
        def findMin(x, y, arr):
            
            if valid(arr, x, y):
                if mem[x][y] != -1:
                    return mem[x][y]
                elif x == len(arr) - 1:
                    mem[x][y] = arr[x][y]
                    return arr[x][y]
                mem[x][y] = arr[x][y] + min(findMin(x + 1, y, arr), findMin(x+1, y-1, arr), findMin(x+1, y+1, arr))
                return mem[x][y]
            else:
                return 10000000
        
        minimum = 10000000
        for i in range(len(matrix)):
            temp = findMin(0, i, matrix)
            minimum = min(minimum, temp)
        
        return minimum