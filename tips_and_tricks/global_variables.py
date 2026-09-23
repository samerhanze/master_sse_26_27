#%%
# X is a global variable
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#%%
# There are two x's, the global x and the local x
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#%%
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#%%
#Also, use the global keyword if you want to change a global variable inside a function
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)