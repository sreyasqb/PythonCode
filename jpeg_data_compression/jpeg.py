import cv2
import numpy as np
import math


from functions import _ycc, padZero, split, downSampling, zigzag, run_length_encoding, find_huffman, get_freq_dict




img=cv2.imread('jpeg_data_compression\\barbara.jpg',cv2.IMREAD_COLOR)
# print(img)
l,b=img.shape[:2]
s=2**math.ceil(math.log2(max(l,b)))

yl,crl,cbl=np.array([[]]),np.array([[]]),np.array([[]])

# #PADDING ZEROES TO MAKE IT POWER OF 2
img=padZero(img,s,l,b)

print(img.shape)

#CONVERTING THE COLOR SPACE TO Y,CR,CB
for i in range(s):
    yt,crt,cbt=[],[],[]
    for j in range(s):
        
        x=_ycc(img[i][j])
        yt.append(x[0]-128) #normalizing so subtracting
        crt.append(x[1]-128)
        cbt.append(x[2]-128)
        
            
    yl=np.append(yl,yt)
    crl=np.append(crl,crt)
    cbl=np.append(cbl,cbt)

#GETTING INDIVIDUAL COMPONENTS
yl=yl.reshape(s,s)
crl=crl.reshape(s,s)
cbl=cbl.reshape(s,s)
print('y cl cr array')
print(yl,crl,cbl)
#DOING DOWNSAMPLING
crl=downSampling(crl,s)
cbl=downSampling(cbl,s)

#SPLITTING INTO 8X8 BLOCKS
print(yl.shape)
yl=split(yl,s)
print(yl.shape)
noBlocks=int(s*s/64)

QTY = np.array([[16, 11, 10, 16, 24, 40, 51, 61],  # luminance quantization table
                [12, 12, 14, 19, 26, 48, 60, 55],
                [14, 13, 16, 24, 40, 57, 69, 56],
                [14, 17, 22, 29, 51, 87, 80, 62],
                [18, 22, 37, 56, 68, 109, 103, 77],
                [24, 35, 55, 64, 81, 104, 113, 92],
                [49, 64, 78, 87, 103, 121, 120, 101],
                [72, 92, 95, 98, 112, 100, 103, 99]])

#PERFORMING DCT AND QUANTIZATION
for i in range(noBlocks):
    yl[i]=cv2.dct(yl[i])
    yl[i]=np.divide(yl[i],QTY)

#ROUNDING OFF TO NEAREST INTEGER  
yl=np.rint(yl)
print(yl[0])
print()

#ZIGZAG TRAVERSAL
yZigZag=np.array([])
for i in yl:
    yZigZag=np.append(yZigZag,zigzag(i))

yZigZagReshape=yZigZag.reshape(noBlocks,64)
print(yZigZagReshape.shape)

#RUN LENGTH ENCODING
# for block in yZigZagReshape:
#     bRLE=run_length_encoding(block)
#     pass
yRLE=run_length_encoding(yZigZag)
print(yRLE.shape)
# print(yRLE)

yPTable=get_freq_dict(yRLE)
print(yPTable)
print()
print()
yHuffman=find_huffman(yPTable)
yHuffman=sorted(yHuffman.items(), key=lambda x: -len(x[1]))
for i in yHuffman:
    print(i[0],i[1],sep=' -> ')




    







# #Making blocks of 8x8
# splitImg=split(img)
# print(splitImg.shape)


