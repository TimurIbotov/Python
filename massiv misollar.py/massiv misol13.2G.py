N = int(input("N ="))
if N < 10:
    m = []
    for i in range(1,N+1):
        m.append(2**(i+1))
    print("M = ", m)
else:
    print("10 dan katta bo'lmasligi kerak")