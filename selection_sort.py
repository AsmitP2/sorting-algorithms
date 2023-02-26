lst = [23, 66, 1, 38, 14, 8, 3, 57]

for j in range(len(lst)):
    minimum=j
    for i in range(j+1, len(lst)):
        if lst[i] < lst[minimum]:
            minimum = i
    print(lst[minimum])
    lst[minimum], lst[j] = lst[j], lst[minimum]
    print(lst)
