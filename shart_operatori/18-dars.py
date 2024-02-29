# def sum(*items):
#     print(items)

# x = sum(1, 8)

# print(x)

# def sum(*items):
#     s = 0
#     for item in items:
#         s += item
#     return s
    
# x = sum(1, 8, 15, 20)

# print(x)

def sum(**items):
    for key, value in items.items():
        print(key, value)
    
x = sum(a=1, b=8, s=15, d=20)

print(x)