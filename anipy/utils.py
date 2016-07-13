

def underscore_to_camelcase(value):
    first, *rest = value.split('_')
    return first + ''.join(word.capitalize() for word in rest)
