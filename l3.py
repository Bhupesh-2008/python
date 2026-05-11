n= int(input("Enter the number , the sum of whose series you want to calculate: "))
res=0.0
fac=1
for i in range(1, n+1):
    fac= fac*i
    res+= float(i)/fac

print (res)