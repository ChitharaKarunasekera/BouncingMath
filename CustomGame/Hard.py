#Module for Level 'Hard'
import random
import datetime

ques = []
answer = []
real = []

def details():
    "This function is to get user infromation"
    global num
    global name
    name = input("Type your name: ")
    num = int(input("Number of questions you want: "))
    print("\n",end="")
    print("Hello ",name,"!!!")
    return name,num

def questions():
    "This function is to produce questions in hard level"
    global num1
    global num2
    global num
    global opp
    global a
    global ans
    global realans
    
    operators =['-','+','x']
    print("\n",end="")
    for i in range (num):
        num1 = random.randrange(0,100)
        num2 = random.randrange(0,100)
        opp = random.choice(operators)
        a = [num1, opp, num2]
        ques.append(a)
        print(num1, opp, num2, '?',end=" ")
        ans = (input())
        answer.append(ans)
        if(opp == '+'):
            realans = str(num1 + num2)
            real.append(realans)
        elif(opp == '-'):
            realans = str(num1-num2)
            real.append(realans)
        elif(opp == 'x'):
            realans = str(num1*num2)
            real.append(realans)
    print("\n",end="")
    return 

def performance ():
    'This function is to display  player performance'
    count = 0
    for a in ques:
        for j in a:
            print(j,end=" ")
        print("\t",'=',"\t",real[count],end=" ")
        print("(Answer: ",answer[count],")",end=" ")
        if(answer[count]==real[count]):
            print("[Correct]")
        else:
            print("[Incorrect]")
        count+=1
    print("\n",end="")
    return
        
def  score():
    "This function is to calculate the score score"
    global score
    global totNum
    score = 0
    i = 0
    totNum = len(real)
    while(i<totNum):
        if(answer[i]==real[i]):
            score = score + 1
            i+=1
        else:
            i+=1
    return score

def percScore():
    'This function is to calculate percentage score'
    global perc
    perc = 0
    perc = round(score/totNum*100)
    return perc

def clock():
    "this function is to get the current time from computer stettings"
    global time
    global date
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    return time,date
