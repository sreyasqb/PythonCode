def naiveMethod(string : str,pattern : str):
    n,m = len(string),len(pattern)
    for i in range(n-m+1):
        flag = True
        for j in range(m):
            if string[i+j] != pattern[j]:
                flag = False
                break
        if flag:
            print(i)
# naiveMethod('SNITCHES-GET-STICHES','CHES')

def naiveMethodPythonic(string,pattern):
    n,m = len(string),len(pattern)
    for i in range(n-m+1):
        if string[i:m+i] == pattern:
            print(i)
naiveMethodPythonic('SNITCHES-GET-STICHES','CHES')




