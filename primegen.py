def main():
    upperlimit = 2000000
    primes = []
    actualprimes= []
    for i in range(upperlimit):
        primes.append(i)


    for i in range(len(primes)):
        if primes[i] != 1 and primes[i]!=0:
            prime = primes[i]
            actualprimes.append(primes[i])
            
            n=1
            while(prime*n<upperlimit):
                primes[prime*n]=1
                n+=1


    print(actualprimes)

    file = open("primes.txt","w")
    for prime in actualprimes:
        file.write(str(prime)+'\n')
main()
