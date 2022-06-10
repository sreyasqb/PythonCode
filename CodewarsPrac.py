# def balanced_parens(n, k):
#     if n == 2:
#         return ["(())", "()()"]
#     s="("*(n-1)+")"*(n-1) #((())) , (()()) ,()(()),(())()
#     l=[]
#     for i in range((n-1)//2,n+1):
#         temp=s[:i+1]+"()"+s[i+1:]
#         print(i)
#         l.append(temp)
#     return l
# print(balanced_parens(3,1))
# def rgb(r,g,b):
#     if r>255:r=255
#     if g > 255: g = 255
#     if b > 255: b = 255
#     if r<0:r=0
#     if g < 0: g = 0
#     if b < 0: b = 0
#     rs=(2-len(hex(r)[2:]))*'0'+hex(r)[2:]
#     gs = (2-len(hex(g)[2:]))*'0'+hex(g)[2:]
#     bs=(2-len(hex(b)[2:]))*'0'+hex(b)[2:]
#     return (rs+gs+bs).upper()
# print(rgb(255,300,255))
# def is_merge(s, part1, part2):
#     if len(part1)+len(part2)!=len(s):
#         return False
#     for i in range(len(s)):
#         if s[i] in part1:
#             part1=part1[1:]
#         elif s[i] in part2:
#             part2=part2[1:]
#         else:
#             return False
#     return True
# print(is_merge("codewars","cdw","ars"))
def move_zeros(array):
    a=array.count(0)
    for i in range(a):
        array.remove(0)
    return array+[0]*a
print(move_zeros([1,2,0,0,1,2]))





