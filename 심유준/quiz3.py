'''a = ['hello.py', 'HW1.hwp', 'python.docx']
for i in a:
    b = i.split('.')[0]
    print(b)
a = [1, 1, 1, 1, 2, 2, 2, 'p', 'p', 'a', 'p', 2, 2, 1, 1]
b = set(a)
c = list(b)
print(c)'''
sum = 0
sum_1 = 0
for i in range(1, 101):
    if i %2 == 0:
        sum = sum + i
    else:
        sum_1 = sum_1 + i
print(f'짝수의 합 : {sum}')
print(f'홀수의 합 : {sum_1}')

sum = 0
sum_1 = 0
i = 1
while i < 101:
    if i %2 == 0:      
        sum = sum + i
    else:
        sum_1 = sum_1 + i
    i = i + 1
print(f'짝수의 합 : {sum}')
print(f'홀수의 합 : {sum_1}')


    
    


