import re
s='''
Hello_&ALL
'''
patern=re.compile(r'[a-zA-Z_]{1,}')
matches=patern.finditer(s)
for match in matches:
    print(match)