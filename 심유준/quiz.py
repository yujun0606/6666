'''a = ['starbucks', 'twosomeplace', 'hollys', 'megacoffe']
for i in a:
    #print(i)
    print(i,len(i))'''
'''i = 3
while i <= 5:
    i = i + 1
    l = 1
    while l <= 9:
        print(f'{i} * {l} = {i * l}')
        l = l + 1'''
score = [100, 75, 90, 50, 85]
grade = []

'''for i in score:
    if i >= 90:
        grade.append('A')
    elif i >= 80:
        grade.append('B')
    elif i >= 70:
        grade.append('C')
    else:
        grade.append('F')
print(score)
print(grade)'''
i = 0
while i < len(score):
    if score[1] >= 90:
        grade.append('A')
    elif score[1] >= 80:
        grade.append('B')
    elif score[i] >= 70:
        grade.append('C')
    else:
        grade.append('F')
    i = i + 1
print(grade)
        
    
        
    
    
    
    
