'''
QUESTION

Write a C program to implement the following game.
 The parent program P first creates two shared memory segments, and then
spawns two child processes C and D.
 One of the two shared memory segment is meant for communications
between P and C, and the other for communications between P and D.
Now, a loop runs as follows.
 In each iteration (also called round), P first randomly chooses one of the two
flags: MIN and MAX (the choice randomly varies from one iteration to
another).
 Each of the two child processes C and D generates a random positive integer
and sends that to P via its shared memory.
 P reads the two integers; let these be c and d.
o If P has chosen MIN, then the child who sent the smaller of c and d
gets one point.
o If P has chosen MAX, then the sender of the larger of c and d gets one
point.
o If c = d, then this round is ignored.
 The child process who first obtains five points wins the game.
 During each iteration of the game, P should print appropriate messages (like
P’s choice of the flag, the integers received from C and D, which child gets
the point, the current scores of C and D) in order to let the user know how
the game is going on.
 C and D exits after five iterations, then the parent process P also exits.
'''


from multiprocessing import Process,Value
import random
def C(n):n.value=random.randint(0,100)
def D(n):n.value = random.randint(0, 100)
if __name__ == '__main__':
    cPoints=0
    dPoints=0
    while cPoints<5 and dPoints<5:
        cValue=Value('i',0)
        dValue=Value('i',0)
        p1=Process(target=C,args=(cValue,))
        p2=Process(target=D,args=(dValue,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        ran = random.randint(0, 1) #0=MIN 1=MAx
        if (ran==0):#MEANS MIN FLAG IS CHOSEN
            if cValue.value<dValue.value:cPoints+=1
            elif cValue.value>dValue.value:dPoints+=1
        if (ran==1):#MEANS MAX FLAG IS CHOSEN
            if cValue.value<dValue.value:dPoints+=1
            elif cValue.value>dValue.value:cPoints+=1
        print(f'ran : {"MIN" if ran==0 else "MAX"}\ncValue : {cValue.value}\ndValue : {dValue.value}')
        print(f'cPoints : {cPoints}\ndPoints : {dPoints}\n')
    if dPoints==5:print('D Wins!!!')
    else:print('C Wins!!!')
