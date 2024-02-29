# from datetime import date, datetime

# d = datetime.now()

# print( str(d.year) + "-" + str(d.month) +"-" + str(d.day) ) 

from datetime import date, datetime

d = datetime.now()

print (d.strftime("%Y-%m-%d-%I"))

# %A xafta kuni 
# %w xafta kun sana bilan
# %d kun
# %B kaysi oy
# %m kaysi oy sana bilan
# %Y yil 
# %H soat 00-23
# %I soat 00-12
# %P AM/Pm