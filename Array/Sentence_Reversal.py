# Python tricks :-

def reverse(sen):
    print(" ".join(sen.split()[::-1]))


reverse("    This is     the best     ")


def reverse1(sen):
    print(" ".join(reversed(sen.split())))


reverse1("hii john,    how are you doing    ?")

# Algorithms :-


def reverse2(sen):

    words = []
    length = len(sen)
    spaces = [' ']

    i = 0

    while i < length:

        if sen[i] not in spaces:
            word_start = i

            while i < length and sen[i] not in spaces:
                i += 1
            words.append(sen[word_start:i])
        i += 1

    return words


def final_rev(words):
    length = len(words)
    s = length

    rev_words = [None]*length
    for i in words:
        s = s - 1
        rev_words[s] = i
    return " ".join(rev_words)


print(final_rev(reverse2('hello jim,   how are you  ?')))
