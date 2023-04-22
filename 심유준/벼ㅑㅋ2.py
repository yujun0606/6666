'''num = int('02-1111-2222')
num_split = number('-')[0]
if num_split == '02':
    print('서울')
elif num_split == '031':
    print('경기도')
elif num_split == '032':
    print('인천')
else:
    print('그 외 번호')'''
'''time = '16:00'
if time[3 : ] != '00':
    print('입력한 시간이 정각이 아니다.')
else:
    print('입력한 시간은 정각이다.')'''

a = '010-1234-5678'
b = []
print(a.replace('-', ' '))
print(a.replace('-', ''))
b.append(a[0 : 3])
b.append(a[4 : 8])
b.append(a[9 : 14])
print(b)    
