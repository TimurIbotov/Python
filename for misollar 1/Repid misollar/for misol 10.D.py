N = int(input("N ="))
S = 0 
for i in range(1, N+ 1):
    S = ((-1)**i) / ((2 * i + 1)*i)
print("S =", S)