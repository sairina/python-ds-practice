def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lst = list(phrase)
    new_lst = []
    empty = ''
    for letter in lst:
        if letter.lower() == to_swap.lower():
            if letter == letter.upper():
                letter = letter.lower()
            else:
                letter = letter.upper()
        new_lst.append(letter)
    
    return empty.join(new_lst)

    
