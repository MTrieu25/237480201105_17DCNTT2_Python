i=0
for g in range(1,100):
    for c in range(1,100-g):
        if(g+c==36 and 2*g+4*c==100):
            i=i+1
            print('Cách',i,': với số gà là',g,'và số chó là',c)