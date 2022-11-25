import numpy as np
from collections import Counter
from itertools import groupby
def _ycc(arr): # in (0,255) range
    if len(arr)==1:
        r,g,b=0,0,0
    else:  
        r,g,b=arr  
    y = .299*r + .587*g + .114*b
    cb = 128 -.168736*r -.331364*g + .5*b
    cr = 128 +.5*r - .418688*g - .081312*b
    return y, cb, cr

def padZero(img:np.array,s,l,b)->np.array:
    img=np.pad(img,((0,s-l),(0,s-b),(0,0)),'constant',constant_values=0)
    return img
    

def split(img:np.array,s)->np.array:
    img=img.reshape(-1).reshape(int(s*s/64),8,8)
    return img

def downSampling(c:np.array,s)->np.array:
    x=np.array([])
    for i in range(0,s,2):
        for j in range(0,s,2):
            x=np.append(x,(c[i][j]+c[i+1][j]+c[i][j+1]+c[i+1][j+1])/4)
    return x.reshape(int(s/2),int(s/2))
    
def trim(array: np.ndarray) -> np.ndarray:
    
    trimmed = np.trim_zeros(array, 'b')
    if len(trimmed) == 0:
        trimmed = np.zeros(1)
    return 

def zigzag(matrix: np.ndarray) -> np.ndarray:
    
    h = 0
    v = 0
    v_min = 0
    h_min = 0
    v_max = matrix.shape[0]
    h_max = matrix.shape[1]
    i = 0
    output = np.zeros((v_max * h_max))

    while (v < v_max) and (h < h_max):
        if ((h + v) % 2) == 0:  # going up
            if v == v_min:
                output[i] = matrix[v, h]  # first line
                if h == h_max:
                    v = v + 1
                else:
                    h = h + 1
                i = i + 1
            elif (h == h_max - 1) and (v < v_max):  # last column
                output[i] = matrix[v, h]
                v = v + 1
                i = i + 1
            elif (v > v_min) and (h < h_max - 1):  # all other cases
                output[i] = matrix[v, h]
                v = v - 1
                h = h + 1
                i = i + 1
        else:  # going down
            if (v == v_max - 1) and (h <= h_max - 1):  # last line
                output[i] = matrix[v, h]
                h = h + 1
                i = i + 1
            elif h == h_min:  # first column
                output[i] = matrix[v, h]
                if v == v_max - 1:
                    h = h + 1
                else:
                    v = v + 1
                i = i + 1
            elif (v < v_max - 1) and (h > h_min):  # all other cases
                output[i] = matrix[v, h]
                v = v + 1
                h = h - 1
                i = i + 1
        if (v == v_max - 1) and (h == h_max - 1):  # bottom right element
            output[i] = matrix[v, h]
            break
    return output

def run_length_encoding(array: np.ndarray) -> np.ndarray:
    return np.array([[len(list(group)), key] for key, group in groupby(array)])


def get_freq_dict(array: np.ndarray) -> dict:
    d={}
    for i in array:
        d[int(i[1])]=0
    for i in array:
        d[int(i[1])]+=i[0]
    return d
    #
    # data = Counter(array)
    # result = {k: d / len(array) for k, d in data.items()}
    # return result


class Node:
    def __init__(self, symbols:list,count):
        self.symbols = symbols
        self.count=count

    def addCode(self,ans:dict,code:str)->dict:
        for i in self.symbols:
            ans[i]=code+ans[i]
        return ans
        

    def __repr__(self):
        return f'{self.symbols} -> {self.count}'

def find_huffman(p: dict) -> dict:
    ans={}
    for i in p:
        ans[i]=''
    
    
    l=sorted(p.items(), key=lambda x: x[1])
    for i in range(len(l)):
        l[i]=Node([l[i][0]],l[i][1])
    n=len(l)
    while n>1:
        n1=l.pop(0)
        n2=l.pop(0)
        l.append(Node(n1.symbols+n2.symbols,n1.count+n2.count))
        ans=n1.addCode(ans,'0')
        ans=n2.addCode(ans,'1')
        n-=1
        l=sorted(l, key=lambda x: x.count)
    return ans
    