# Input = 4
# output = 4+3+2+1+0 = 10

def rec_sum(n):
    # Base Case
    if n==0:
        return 0

    # Recursive Case
    else:
        return n + rec_sum(n-1)

print(rec_sum(4))       # 10