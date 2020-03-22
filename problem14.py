def main():
    upperbound = 1000000
    record = 0
    result = 0
    for i in range(1,upperbound):
        print(i/10)
        n=i
        c=0
        while(n!=1):
            if(n%2==0):
                n/=2
            else:
                n=3*n+1
            c+=1
        if(c>record):
            record = c
            result = i
    print(result)
main()
