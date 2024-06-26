from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for cord in points:
            distance = cord[0]**2 + cord[1]**2
            setCord = (cord[0], cord[1])
            # Use negative distance to simulate a max heap
            heapq.heappush(heap, (-distance, setCord))

            if len(heap) > k:
                heapq.heappop(heap)
    
        closest = []
        while heap:
            dist, cord = heapq.heappop(heap)
            closest.append([cord[0], cord[1]])

        return closest
