from math import *

result = 0
for i in range(100000000):
    string = str(i)
    facsum = 0
    for j in range(len(string)):
        facsum += factorial(int(string[j]))
    if(facsum == i):
        print(i)
        result += i
print(result)
# result = 40733
