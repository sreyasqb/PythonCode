import time
# print(C,P)

f=open('input_data/a_an_example.in.txt','r')
lines=f.readlines()
C, P = lines[0].split()
C, P = int(C), int(P)
ind=1
# print(C,P)
Cdict={}
Pdict={}


for i in range(C):
    name,no_role=lines[ind].split()
    roles={}
    for j in range(int(no_role)):
        ind += 1
        role_name,level=lines[ind].split()
        level=int(level)
        roles[role_name]=level

    ind+=1
    Cdict[name]=roles




for i in range(P):
    name,days,score,bb,no_roles=lines[ind].split()
    days,score,bb,no_roles=int(days),int(score),int(bb),int(no_roles)

    roles={}
    for j in range(no_roles):
        ind += 1
        role_name,level=lines[ind].split()
        level=int(level)
        roles[role_name]=level

    ind+=1
    Pdict[name]={'days':days,'score':score,'bb':bb,'no_roles':no_roles,'roles':roles}

# print(Cdict)
# print(Pdict)

new_Cdict={}

for i in Cdict:
    for j in Cdict[i]:
        if j not in new_Cdict:
            new_Cdict[j]={Cdict[i][j]:[i]}
        else:
            if Cdict[i][j] not in new_Cdict[j]:
                new_Cdict[j][Cdict[i][j]]=[i]
            else:
                # print(new_Cdict[j])
                new_Cdict[j][Cdict[i][j]].append(i)


        # print(new_Cdict)



# print(new_Cdict)
# print(Pdict)
# maxi=0
# a=time.time()
# key=0
# for i in Pdict:
#     if Pdict[i]['score']>maxi:
#         maxi=Pdict[i]['score']
#         key=i
#
# print(maxi)
# print(time.time()-a)
# print(Pdict[key])
print(new_Cdict)
print(Pdict)