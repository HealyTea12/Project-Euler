def main():
    file = open("primes.txt")
    lines = file.readlines()
    sum = 0
    for line in lines:
        sum+= int(line)
        print(sum)
main()
