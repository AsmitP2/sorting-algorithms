lst = [18, 4, 72, 43, 85, 14]

for j in range(len(lst)-1):
    for i in range(len(lst)-1-j):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
print(lst)