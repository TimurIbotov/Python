A  = float(input("A ="))
N = int(input("N ="))
i = 0
S = 1
while i <N:
    z = (A - i * N)
    S = S * z
    i += 1
print("S =", S)