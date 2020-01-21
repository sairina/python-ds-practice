def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversed_str = ''
    phrase_list = list(phrase)
    phrase_list.reverse()
    return reversed_str.join(phrase_list)