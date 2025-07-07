def median(numbers):
    """
    Calculate the median of a list of numbers.
    
    :param numbers: List of numbers
    :return: Median value
    """
    if not numbers:
        return None
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2
    
my_list = [3,4, 1, 4, 2, 5]
print("The median is:", median(my_list))