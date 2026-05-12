# Here in title function it converts the first letter of every word in a string into cpital letter
s= str(input("Enter the string: "))
res=[]
n= len(s)
for i in s.split():
    res.append(i[0].upper()+i[1:].lower())

print(" ".join(res)) 