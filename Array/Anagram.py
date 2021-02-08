# Method-1 :-

# def anagram(s1, s2):
# #   Removing the white spaces between words and lowering all the letters...
#     s1 = s1.replace(' ', '').lower()
#     s2 = s2.replace(' ', '').lower()
#
# #   Sorting the words...
#     return sorted(s1) == sorted(s2)
#
#
# if anagram('dog', 'god'):
#     print('Anagram')
# else:
#     print('Not Anagram')


# Method - 2:-

def anagram2(s1, s2):
    #   Removing the white spaces between words and lowering all the letters...
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Edge checking
    if len(s1) != len(s2):
        return 'Not Anagram'

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for i in count:
        if count[i] != 0:
            return 'Not Anagram'

    return 'Anagram'


print(anagram2('dog', 'god'))
