import random
# N = int(input("N ="))
# S = 0
# for i in range(1,N):
#     if N % i == 0 :
#         S = S + i
# print(S)
# N = int(input("Nechta raqam kerak ----->"))
# mass = [91,90,95,94,93,50,33,97,98,99,71,88]
# mass_2 = []
# z = 0
# s = 0 
# y = 0
# for i in range(1,N+1):
#     x = random.randint(0,0 < 15)
#     z = random.randint(100,999)
#     s = random.randint(10,99)
#     y = random.randint(10,99)
#     print(i,"raqam")
#     print("+998" , mass[x], z, "-" , s  , "-" , y )
import random

# User input for how many numbers to generate
N = int(input("Nechta raqam kerak -----> "))
mass = [91, 90, 95, 94, 93, 50, 33, 97, 98, 99, 71, 88]

for i in range(1, N + 1):
    # Randomly select an index from the mass list
    x = random.randint(0, len(mass) - 1)  # Use the correct range for mass
    z = random.randint(100, 999)  # Generates a random three-digit number
    s = random.randint(10, 99)     # Generates a random number between 10 and 99
    y = random.randint(10, 99)     # Generates a random number between 10 and 99

    # Format the output
    print(i, "raqam")
    print("+998", mass[x], z, "-", s, "-", y)
