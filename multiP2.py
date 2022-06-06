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
