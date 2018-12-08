def test_char(character):
    if len(character) == 1:
        return character in ['a','e','i','o','u']
    else:
        raise ValueError('Length of the input can only be 1')

print(test_char('s'))
print('\n')
print(test_char('2'))
print('\n')
print(test_char('a')) 