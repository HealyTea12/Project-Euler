from math import *
def main():

    f = open("problem8num.txt","r")
    number = int(f.read().replace('\n',''))
    size = int(log10(number))+1
    prod = 1
    res = 1
    dig13 = []
    for i in range(size):
        if(i<13):
            temp = number/(10**(size-1-i))
            print(temp)
            number -= temp*10**(size-1-i)
            if(temp == 0):
                temp = .000001
            prod *= temp
            dig13.append(temp)
        else:
            temp = number/(10**(size-1-i))
            print(temp)
            number -= temp*10**(size-1-i)
            if(temp == 0):
                temp = .000001
            prod *= temp
            prod /= dig13[0]
            del dig13[0]
            dig13.append(temp)


        if(prod > res):
            res = prod

    print(res)
if __name__ == "__main__":
    main()
