# Given an integral number N.The task is to find the count of digits present in this number.

#Solution 1 : TC- O(n)

num = 12345
count = 0
while(num != 0):
    num = int(num/10)
    count += 1
print(count)


#Solution 2 : TC - O(1)

