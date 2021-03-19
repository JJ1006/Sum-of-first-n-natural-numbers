
def SumofNumbers(n):
    sum = 0
    for i in range(1,n+1):
        sum=i+sum
    return sum

n=int(input("\nPlease enter the number : \n"))    
y=SumofNumbers(n)
print(y)