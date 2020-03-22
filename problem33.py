num = 1
den = 1
for i in range(1,10):
    for j in range(i+1,10):
        for k in range(1,10):
            if((10*i+j)/float((10*j+k))==i/float(k)):
                num *= i
                print(10*i+j)
                den *= k
                print(10*j+k)
print(num)
print(den)
# result = 1/100 
