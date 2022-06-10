a = "epidemiologist"
b = "refrigeration"
c = "supercalifragilisticexpialodocious"

astring=''
bstring=''
cstring=''

for i in a:
    if i in b and i in c:
        astring+=i
for i in b:
    if i in a and i in c:
        bstring+=i

for i in c:
    if i in a and i in b:
        cstring+=i

astring,bstring,cstring=sorted([astring,bstring,cstring],key=len)
print(astring, bstring,cstring)
a=astring
b=bstring
c=cstring


print(maxe)











