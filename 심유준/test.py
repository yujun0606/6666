'''num = [[1, 2], [3, 4], [5, 6]]
num1 = []
for i in num:
    for j in i:
        num1.append(j)
print(num1)'''

'''for i in range(9, 1, -2):
    for j in range(i, i - 4, -1):
        print(j, end=' ')
    print()'''


'''def triple_one(nums):
    result = []
    for i in nums:
        if i % 3 == 1:
            result.append(i)
    return result
a = [5, 27, 10, 4, 9, 11, 16, 23, 28]
print(triple_one(a))'''


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(7))    

def fib(n):
    if n < 0:
        print('오류')
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(5))
