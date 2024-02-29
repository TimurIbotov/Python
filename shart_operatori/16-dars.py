# import re

# s = "My first Regulat Expression"

# x = re.search("first", s)

# if x:
#     print(x)

# import re


# s = "My 1 Regulat 2 Expression"

# x = re.findall("[0-9]+", s)

# print(x)


import re


s = "My 1 Regulat 2 Expression"

x = re.sub("[0-9]+", "raqam", s)

print(x)