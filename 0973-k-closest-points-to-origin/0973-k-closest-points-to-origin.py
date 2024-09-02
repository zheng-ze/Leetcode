class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) <= k:
            return points
        
        def square_distance(point: [List[int]]) -> int:
            return point[0] * point[0] + point[1] * point[1]
        
        heap = []
        heapq.heapify(heap)
        
        for i in range(k):
            distance = square_distance(points[i])
            heapq.heappush(heap, (-distance, i))
        
        for i in range(k, len(points)):
            distance = square_distance(points[i])
            if heap[0][1] <= -distance:
                continue
            heapq.heappushpop(heap, (-distance, i))
        
        return list(map(lambda item: points[item[1]], heap))
