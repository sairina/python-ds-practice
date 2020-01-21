def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    new_dict = {}

    for num in nums: 
        if num in new_dict:
            new_dict[num] += 1
        else:
            new_dict[num] = 1

    start = 1
    mode = 0

    for key in new_dict:
        if new_dict[key] > start:
            start = new_dict[key]
            mode = key

    return mode