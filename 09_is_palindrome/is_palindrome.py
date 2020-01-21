def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
   
    lower_case_phrase = phrase.lower()
    lower_case_phrase = lower_case_phrase.replace(" ", "")

    lower_case_list = list(lower_case_phrase)
    lower_case_list.reverse()
    new_phrase = ''.join(lower_case_list)

    if lower_case_phrase == new_phrase:
        return True
    
    return False


