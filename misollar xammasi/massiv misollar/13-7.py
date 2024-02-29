a = [19,32,788,43,53,56,786,34,23]
n = len(a)
qadam = 0
for i in range(n-1):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            qadam += 1
print(a)
print(qadam)