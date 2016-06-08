s = str(input("enter string:"))
t = list(s)
t[::2],t[1::2] = t[1::2],t[::2]
''.join(t)
print(t)
