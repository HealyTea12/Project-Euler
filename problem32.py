result = 0
count = 0
truth = [True] + [False]*9
panproducts = []
loopcounter = 0
for i in range(10000):
    for j in range(i,10000):
        loopcounter += 1
        string = str(i) + str(j) + str(i*j)
        if(len(string)> 9):
            break
        if(len(string) == 9):
            truth = [True] + [False]*9
            count = 0
            for char in string:
                if(truth[int(char)]) == False:
                    count += 1
                truth[int(char)] = True
            if(count == 9):
                panproducts.append(i*j)
                print(str(i))
                print(str(j))
                print(str(i*j))
panproducts = set(panproducts)
result = sum(panproducts)
print(result)
print(loopcounter)
