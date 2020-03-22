def main():
    file = open("primes.txt")
    lines = file.readlines()
    l = len(lines)
    for i in range(l):
        print(l-i-1)
        if "5" in lines[l-i-1] or "0" in lines[l-i-1] or "2" in lines[l-i-1] or "4" in lines or "6" in lines or "8" in lines:
            del lines[l-i-1]

    dict = {}

    for line in lines:
        key = h(int(line))
        dict[key] = dict.get(key,0)+1

    
def h(number):
    pass

main()
