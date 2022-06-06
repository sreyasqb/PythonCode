'''
QUESTION

Implement a C program that creates a shared memory region and fills it with
set of n integers (say n=10). The program should
 Create 2 Child processes
 The Child Process-1 will find the minimum of the numbers from the shared
memory region and store it in minimum shared variable.
 The Child Process-2 will find the average of the numbers from the shared
memory region and store it in the average shared variable.
 The Parent process will wait for the child processes to complete and then print
the minimum and average on the screen.
'''

from multiprocessing import Process,Value,Array
import os

l=[5,2,3,4,6,7,8,9,10]

def min(n):
    print(f'Process 1 id : {os.getpid()}')
    m=l[0]
    for i in l:
        if i<m:m=i
    n.value=m

def avg(n):
    print(f'Process 2 id : {os.getpid()}')
    s=0
    for i in l:
        s+=i
    n.value=s/len(l)
if __name__ == '__main__':
    _min=Value('i',0)
    _avg=Value('d',0.0)
    arr=Array('i',range(10))
    p1=Process(target=min,args=(_min,))
    p2=Process(target=avg,args=(_avg,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('done')
    print('min : ',_min.value)
    print('avg : ',_avg.value)

