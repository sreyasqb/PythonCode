import pandas as pd
import random as r
from openpyxl.workbook import Workbook
import numpy as np
import itertools

#TASK ATTRIBUTES
t_id,t_budget,t_quality,t_skill=[],[],[],[]
s=[]
for k in range(65,91):
    s.append(chr(k))
print(s)
for i in range(1,11):
    t_id.append(i)
    t_budget.append(round(r.uniform(1.0, 2.0), 1))
    t_quality.append(round(r.uniform(0.1, 1.0), 1))
    t=r.randrange(1,5)
    for t1 in range(0,t):
        if t1==0:
            t_skill.insert(i-1,[r.choice(s)])
        else:
            t_skill[i-1].append(r.choice(s))

print(t_skill)
print(len(t_skill))

#WORKER ATTRIBUTES
w_id,w_payment,w_quality,w_preflist,w_skill=[],[],[],[],[]
l = list(range(1,11))
n=0
for j in range(1,31):
    w_id.append(j)
    w_payment.append(r.randrange(50,101))
    w_quality.append(round(r.uniform(0.1, 1.0), 1))
    r.shuffle(l)
    w_preflist.append(l[:])
    w = r.randrange(1, 5)
    for w1 in range(0, w):
        if w1 == 0:
            w_skill.insert(j - 1, [r.choice(s)])
        else:
            w_skill[j - 1].append(r.choice(s))

w_proff=[]
m=[]
print(w_skill)
for q in range(len(w_skill)):
    m.append(len(w_skill[q]))
print(m)
v=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
for m1 in m:
    while True:
        pick = r.sample(v, m1)
        if sum(pick) == 1.0:
            break
    result = pick
    w_proff.append(result)
print(w_proff)

print(len(w_preflist))
df1 = pd.DataFrame({'TASK ID': t_id,'TASK BUDGET' : t_budget,'SKILL REQUIREMENT': t_skill})
df2 = pd.DataFrame({'WORKER ID': w_id,'WORKER QUALITY' : w_quality,'SKILLS OFFERED': w_skill,'PROFFECIENCY LIST': w_proff})
df3=pd.DataFrame({'PREFERENCE LIST(TASK)': w_quality})
df4=pd.DataFrame({'PREFERENCE LIST(WORKERS)': w_preflist})
print("TASK SET")
print(df1,"\n")
print("WORKER SET")
print("\n",df2,"\n")
print(df4)
w_quality.sort()
# print(w_quality)

w=df3.to_dict('dict')
# print(w)
vals=w.values()
for g in vals:
    print(g)
g1=g.items()
# print(g1,type(g1))
sorted=(sorted(g1, key=lambda x: x[1]))
# print(sorted)


def Convert(sorted, di):
    di = dict(sorted)
    print(di)
    di_1=di.keys()
    print(di_1)
    t_preflist=[x + 1 for x in di_1]
    #print("====",x1)
    t_preflist.reverse()
    print("\n\nPREFERENCE LIST OF CROWDSOURCERS:\n",t_preflist)
    global df5
    df5 = pd.DataFrame({'PREFERENCE LIST(TASKS)': t_preflist})
    # if 0 in t_preflist:
    #     print("======you")
    # else:
    #     print("===no you")
dictionary = {}
Convert(sorted, dictionary)



#.xlsx file
file_name = 'task_dataset.xlsx'
file1_name = 'worker_dataset.xlsx'
file2_name = 'worker_preference.xlsx'
file3_name = 'task_preference.xlsx'
df1.to_excel(file_name)
df2.to_excel(file1_name)
df4.to_excel(file2_name)
df5.to_excel(file3_name)
#.txt file
numpy_array1 = df1.to_numpy()
numpy_array2 = df2.to_numpy()
numpy_array3 = df4.to_numpy()
numpy_array4 = df5.to_numpy()
np.savetxt("tsk_dataset.txt", numpy_array1, fmt = "%s")
np.savetxt("wrkr_dataset.txt", numpy_array2, fmt = "%s ")
np.savetxt("wrkr_pref.txt", numpy_array3, fmt = "%s")
np.savetxt("tsk_pref.txt", numpy_array4, fmt = "%s")