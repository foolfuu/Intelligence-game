import random
import os

emt = 0
number1 = 0
number2 = 0
while True:
    try:
        os.system("cls")
        print("welcome to game!")
        print("emt = {}".format(emt))
        number1 = random.randint(10,100)
        number2 = random.randint(10,100)
        print("{}  +  {} = ".format(number1,number2))
        av = ["1:","2:","3:","4:"]
        a1 = []
        a2 = []
        a1.append(number2+number1)
        for i in range(3): a1.append(random.randint(10,100))
        for i in range(len(a1)):
            x = random.randint(0,len(a1)-1)
            a2.append(a1[x])
            a1.pop(a1.index(a1[x]))
        
        for i in range(len(av)):
            print(av[i],a2[i])
        
        dfg = int(input('Enter: '))
        if dfg <= 4:
            if a2[dfg-1] == number1+number2: emt += 1
            else: emt -= 1
        else: emt -= 1
        
        
        
        
        
        
        
    except ValueError:
        os.system("cls")
        emt -= 1
