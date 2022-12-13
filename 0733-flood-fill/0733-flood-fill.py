class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direc = ((1, 0), (-1, 0), (0, 1), (0, -1))
        orig = image[sr][sc]
        queue = deque([(sr, sc)])
        visited = [[False for j in range(len(image[0]))] for i in range(len(image))]
        
        while queue:
            x, y = queue.popleft()
            if visited[x][y]:
                continue
            image[x][y] = color
            visited[x][y] = True
            for d in direc:
                new_x = x + d[0]
                new_y = y + d[1]
                if new_x < 0 or new_x > len(image) - 1 or new_y < 0 or new_y > len(image[0]) - 1:
                    continue
                if visited[new_x][new_y]:
                    continue
                elif image[new_x][new_y] == orig:
                    queue.append((new_x, new_y))
                
        return image