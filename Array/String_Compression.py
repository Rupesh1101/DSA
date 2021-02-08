# run-length compression algorithm....
def compress(s):
    r = ""
    length = len(s)

    if len(s) == 0:
        return ""

    if len(s) == 1:
        return s+"1"

    last = s[0]
    count = 1

    i = 1
    while i < length:

        if s[i] == s[i-1]:
            count += 1
        else:
            r = r + s[i-1] + str(count)
            count = 1
        i += 1
    r = r + s[i-1] + str(count)

    return r


print(compress('AAaa'))
print(compress('AAAABBBCCCcc'))
