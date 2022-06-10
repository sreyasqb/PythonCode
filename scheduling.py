class Process:
    def __init__(self,number,bt):
        self.number=number
        self.bt=bt
    def __str__(self):
        return f"P{self.number}"
def print_process(process_list):
    time=0
    for process in process_list:
        print(' '*(process.bt//2),process,(process.bt//2)*' ',sep='',end='')
    print()
    print(time, end='')
    for process in process_list:
        print(process.bt*'-',time+process.bt,end='',sep='')
        time+=process.bt
    wt=0
    awt=0
    print('\n\nID\tBT\tWT\tTT')
    for process in process_list:
        print(process,process.bt,wt,process.bt+wt,sep='\t')
        wt+=process.bt
        awt+=wt
    print('average time = ',round((awt-wt)/len(process_list),2))

def f_come_f_serve(process_list):
    print_process(process_list)
f_come_f_serve([Process(1,2),Process(2,4),Process(3,6)])
def shortest_job_first(process_list):
    process_list.sort(key=lambda process:process.bt)
    print_process(process_list)
#shortest_job_first([Process(1,7),Process(2,6),Process(3,2),Process(4,2)])
def round_robin(process_list,tq):
    time,n,leng=0,0,len(process_list)
    while n!=leng-1:
        for process in process_list:
            if process.bt>=tq:
                process.bt-=tq
                time += tq
            elif process.bt!=0:
                time+=process.bt
                process.bt = 0
                n+=1
            else:
                break
            # new_list.append(Process(process.number,time))
            print(process, time)
    # print_process(new_list)
#round_robin([Process(1,7),Process(2,6),Process(3,2),Process(4,2)],3)



# print(Process(1,3))