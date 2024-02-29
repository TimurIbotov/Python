A = [9,[1,2,"B",5],10,7]
for i in A:
    # print(i)
    for j in A[1]:
        if j == "B":
            print(A)
            print(j)