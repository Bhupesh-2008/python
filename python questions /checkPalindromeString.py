s= str(input("Enter the string you want to check is whether a palindrome or not: "))
n=len(s)
for i in range(n//2):
    if s[i]!= s[n-i-1] :
        print(s,"is not a palindrome.")
        break
else: print(s,"is a palindrome.")