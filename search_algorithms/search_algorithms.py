def binary_search(a_list, item):
    """Performs iterative binary search to find the position of an integer in a given, sorted, list.
    a_list -- sorted list of integers
    item -- integer you are searching for the position of
    """

    first = 0
    last = len(a_list) - 1

    while first <= last:
        i = (first + last) // 2

        if a_list[i] == item:
            return '{item} found at position {i}'.format(item=item, i=i)
        elif a_list[i] > item:
            last = i - 1
        elif a_list[i] < item:
            first = i + 1
        else:
            return '{item} not found in the list'.format(item=item)






def binary_search2(value, items, low=0, high=None):
    """
    Binary search function.
    Assumes 'items' is a sorted list.
    The search range is [low, high)
    """

    high = len(items) if high is None else high
    pos = low + (high - low) / len(items)

    if pos == len(items):
        return False
    elif items[pos] == value:
        return pos
    elif high == low:
        return False
    elif items[pos] < value:
        return binary_search(value, items, pos + 1, high)
    else:
        assert items[pos] > value
        return binary_search(value, items, low, pos)
    
    
    
    
    
    
    
    
    
    
    
    
    
   # Linear Search
def linear_search(data, target):	
	for i in range(len(data)):
		if data[i] == target:
			return True
	return False

# Iterative Binary Search 
def binary_search_iterative(data, target):
	low = 0
	high = len(data) - 1

	while low <= high:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return False 

# Recursive Binary Search 
def binary_search_recursive(data, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binary_search_recursive(data, target, low, mid-1)
		else:
			return binary_search_recursive(data, target, mid+1, high) 
    
    
