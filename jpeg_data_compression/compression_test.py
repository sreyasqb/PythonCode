import cv2
import os

inp=cv2.imread('jpeg_data_compression\\test1.png',cv2.IMREAD_COLOR)
out=cv2.imread('jpeg_data_compression\\result1.png',cv2.IMREAD_COLOR)

inpSize=os.path.getsize('jpeg_data_compression\\test1.png')
outSize=os.path.getsize('jpeg_data_compression\\result1.png')
print(100-(inpSize-outSize)/inpSize*100)

