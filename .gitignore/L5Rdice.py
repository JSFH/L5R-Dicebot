import random as random



def roll(x,y): #X and Y are chosen for the XkY format of 'roll X and keep Y results'.
    collection=[ ]
    for i in range (x):
        p= random.randrange(1, 11, 1) #range of 1-10, d10 rolls
        while (p%10==0): #L5R d10s explode on 10 indefinitely. Keeps going as long as result is 10.
            p+=random.randrange(1,11,1)
        collection.append(p)
    collection.sort()
    collection.reverse()#largest-to-smallest is more readable and convenient. 
    print (collection) #prints the collection for proofing and in case people DON'T want to keep the largest Y.
    p=0
    for i in range(y): #the 'keep' part of roll-and-keep
        p+=collection.pop(0)
    print('Sum:',p)
    
    

    

random.seed()	
x=0
y=0
while (x!='q' and y!='q'):
    print('Input desired roll.\n')
    x=int(input())
    while (x > 10 or x<1):
        print('Please input reasonable value.\n')
        x=int(input())
    print('k')
    y=int(input())
    while(y>10 or y<1 or y>x):
        print('Please input reasonable value.\n')
        print(str(x)+'k_')
        y=int(input())
    result=roll(x,y)


    
