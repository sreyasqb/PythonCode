def rabinKarp(string,pattern):
    n,m = len(string),len(pattern)
    sHash=0
    pHash=0
    for i in range(m):
        sHash += (ord(string[i]) - 64) * (10**(m-i-1))
        pHash += (ord(pattern[i]) - 64) * (10**(m-i-1)) 
    # print(sHash,pHash)
    for i in range(n-m):
        # print(f'sHash : {sHash} ,pHash : {pHash}')
        if sHash == pHash:
            print(f"INDEX : {i}")
        sHash = (sHash - (ord(string[i]) - 64) * (10**(m-1)))*10 + (ord(string[i+m])-64)    
    if sHash==pHash:
        print(f"INDEX : {n-m}")
    

rabinKarp('SNITCHES-END-UP-IN-DITCHES','CHES')
# rabinKarp("ABCDAB","AB")