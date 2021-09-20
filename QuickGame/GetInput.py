import random
import os
import time

#Creating lists
real = []
answer = []
ques = []

#Creating variables

num1 = 0
opp = ''
num2 = 0

def getname():
    "This functon is to get inputs from the user"
    name  = input("Enter name: ")
    print("\n",end="")
    print("Hello ",name,"!!!")
    print("\n",end="")
    return name


def questions ():
    "This function is to produce 5 random questions"
    global num1
    global num2
    global opp
    global count
    global ans
    global realans
    global a
    count = 1
    while (count<6):
        num1 = random.randrange(0,10)
        opp = '+'
        num2 = random.randrange(0,10)
        a =[num1, opp, num2]
        ques.append(a)
        print(num1, opp, num2,  '?',end=" ")
        realans = str(num1 + num2)
        real.append(realans)
        ans = (input())
        answer.append(ans)
        count+=1
    return

def info ():
    'This function is to display  player performance'
    count = 0
    for a in ques:
        for j in a:
            print(j,end=" ")
        print("\t",'=',"\t",real[count],end="\t")
        print("(Answer: ",answer[count],")",end=" ")
        if (answer[count]==real[count]):
            print("[Correct]")
        else:
            print("[Incorrect]")
        count+=1
    return

def score():
    'This function is to calculate score'
    global score
    global totNum
    score = 0
    totNum = len(answer)
    for i in range (totNum):
        if (answer[i]==real[i]):
            score = score + 1
        else:
            pass
    return score

def perc():
    'This function is to calculate percentage score'
    global perc
    perc = 0
    perc = round(score/totNum*100)
    return perc
