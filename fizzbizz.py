def fizzbizz(n):
    for i in range(1,n+1):
        print(i)
    if n%3==0:
            print("fizz")
    elif n%5==0:
            print("bizz")
    elif n%15==0:
            print("fizzbizz")
    else :
               print(i)

if __name__=="__main__":
    n= int(input("enter a number :"))
    fizzbizz(n)