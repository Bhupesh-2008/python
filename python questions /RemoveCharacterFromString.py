s= str(input("Enter the string: "))
remove= str(input("Enter the character to remove from the given string: "))
result=""
for char in s:
    if(char==remove): continue
    else: result+=char

print("Final string after removing is:",result)