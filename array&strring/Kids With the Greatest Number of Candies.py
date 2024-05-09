def kidsWithCandies( candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    max_candies = max(candies)
    result = []
    for candy_count in candies:
        result.append(candy_count + extraCandies >= max_candies)
    return result
candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies,extraCandies))