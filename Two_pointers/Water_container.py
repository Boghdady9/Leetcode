height = [1,8,6,2,5,4,8,3,7]
maxwater, start, end = 0, 0, len(height) - 1  # Initialize maxwater and two pointers
while start < end:  # Iterate until the two pointers meet or cross each other
    maxwater = max(maxwater, (end - start) * min(height[start], height[end]))  # Calculate the current area and update maxwater
    if height[start] < height[end]:  # Move the pointer with smaller height towards the other pointer
        start += 1
    else:
        end -= 1
