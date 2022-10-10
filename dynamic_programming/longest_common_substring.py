
# ind=[]
# def longestCommonSubsequenceString(a,b):
#     global ind
#     if a=="" or b=="":
#         return 0
#     if a[-1]==b[-1]:
#         if len(a)-1 not in ind:
#             ind.append(len(a)-1)
#         return 1+longestCommonSubsequenceString(a[:-1],b[:-1])
#     elif a[-1]!=b[-1]:
#         return max(longestCommonSubsequenceString(a[:-1],b),longestCommonSubsequenceString(a,b[:-1]))



a,b="ADHJB","ADHEB"
# print(longestCommonSubsequenceString(a,b))
# print("".join([a[i] for i in sorted(ind)]))

def longestCommonSubsequenceLength(a,b):
    if a=="" or b=="":
        return 0
    if a[-1]==b[-1]:
        return 1+longestCommonSubsequenceLength(a[:-1],b[:-1])
    elif a[-1]!=b[-1]:
        return max(longestCommonSubsequenceLength(a[:-1],b),longestCommonSubsequenceLength(a,b[:-1]))
print(longestCommonSubsequenceLength(a,b))