"""
HW05 — Water Sensor: Streaming Median
"""

import heapq

def streaming_median(nums):
    if not nums:
        return []

    low = []   # max heap (store as negatives)
    high = []  # min heap
    medians = []

    for num in nums:
        # Step 1: Push to the correct heap
        if not low or num <= -low[0]:
            heapq.heappush(low, -num)  # push into max heap
        else:
            heapq.heappush(high, num)  # push into min heap

        # Step 2: Balance the heaps (size difference ≤ 1)
        if len(low) > len(high) + 1:
            heapq.heappush(high, -heapq.heappop(low))
        elif len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))

        # Step 3: Calculate median
        if len(low) == len(high):
            median = (-low[0] + high[0]) / 2.0
        else:
            median = -low[0]

        medians.append(median)

    return medians
