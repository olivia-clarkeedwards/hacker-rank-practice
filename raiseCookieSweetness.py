import heapq

def sweeten(min_sweetness, cookies, count = 0):
    heapq.heapify(cookies)

    while cookies[0] < min_sweetness:
        if len(cookies) == 1:
            return -1
        least_sweet = heapq.heappop(cookies)
        second_least_sweet = heapq.heappop(cookies)
        heapq.heappush(cookies, least_sweet + (2 * second_least_sweet))
        count += 1
          
    return count 


print(sweeten(9, [2, 7, 3, 6, 4, 6]))
    

