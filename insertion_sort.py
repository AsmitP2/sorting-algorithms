lst = [23, 66, 1, 38, 14, 8, 3, 57]

for i in range(1, len(lst)):
    element = lst[i]
    j = i-1
    while (element<lst[j] and j >=0):
        lst[j+1] = lst[j]
        j-=1
    lst[j+1] = element

print(lst)