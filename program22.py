#WAP to print the following series and find the sum: xx+xx+xx..... upto nth terms 

x=int(input("enter any number: "))
n=int(input("enter the number of terms: "))
s=0
for i in range(1,n+1):
    t=x*10+x
    print(t,end="")
    if(i<n):
        print("+",end="")
    s=s+t
print("=",end="")


