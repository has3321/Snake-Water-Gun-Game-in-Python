'''
Assume these valuses First

1 is for snake
0 is for Gun
-1 for water 

'''

import random

computer=random.choice(["s","w","g"])
print(f"Computer chose: {computer}")

you=input("Enter your choice plz in string format ")

yourdict={"s" : 1 , "w" : -1, "g" : 0}

younum=yourdict[you]
computernum=yourdict[computer]

if (computernum== younum):
    print("Match Draw")
    
else:
    
    if  (computernum==-1 and younum==1):
        print("you win")
        
    elif (computernum==-1  and younum==0):
        print("you lose ")
        
    elif (computernum==1 and younum==-1):
        print("you lose")
        
    elif (computernum==1 and younum==0):
        print("you win")
        
    elif (computernum==0 and younum==-1):
        print("you win")
        
    elif (computernum==0 and younum==1):
        print("you lose")
        
    else:
        print("something went wrong")

