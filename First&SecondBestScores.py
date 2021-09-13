list = [12,25]



list.sort(reverse=True)
result = []
if len(list) <= 2:
    print('list phai nhieu hon 2 phan tu')
    exit()
else:
    result.append(list[0])
    result.append(list[1])
    print(result)

