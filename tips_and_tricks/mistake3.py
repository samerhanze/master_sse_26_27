#%%
from datetime import datetime
listA = range(10000000)
setA = set(listA)
tupA = tuple(listA)

def calc(data, datatype):
    start = datetime.now()
    if data in datatype:
        print ("Found!")
    end = datetime.now()
    print (end-start)

#%%
#fast to locate in a set, then a tuple, then a list
calc(9999, listA)
calc(9999, tupA)
calc(9999, setA)
# %%
# slow to create a set, then a tuple, then a list
start = datetime.now()
listB = range(10000000)
end = datetime.now()
print (end-start)

start = datetime.now()
tupB = tuple(listB)
end = datetime.now()
print (end-start)

start = datetime.now()
setB = set(listB)
end = datetime.now()
print (end-start)
# %%
