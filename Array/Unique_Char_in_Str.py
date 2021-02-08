# Python built-in methods...

def uni_char(s):
    return len(set(s)) == len(s)


print(uni_char('abcdefsa'))  # False
print(uni_char('abcdefs'))  # True


# Using Algorithms...
def uni_char2(s):
    chars = set()

    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True


print(uni_char2('abcdefs'))     # True
print(uni_char2('abcdefa'))     # False


# class Solution:
#     def remove_duplicate(self, A, N):
#
#     # code here
#     i = 0
#     if N == 0 or N == 1:
#         return N
#     for j in range(N - 1):
#         if (A[j] != A[j + 1]):
#             A[i] = A[j]
#             i += 1
#
#     A[i] = A[N - 1]
#     i += 1
#     return i