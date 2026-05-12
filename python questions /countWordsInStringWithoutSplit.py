s= str(input("Enter the string: "))
cnt=1
for char in s:
    if(char==' '):
        cnt+=1
    
print("No of Words in",s,"are",cnt)