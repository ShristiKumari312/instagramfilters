import cv2
import numpy as np
from matplotlib import pyplot as plt
im=cv2.imread("image.jpg")
row, column =im.shape[:2]
cannal_x=cv2.getGaussianKernel(column,200)
cannal_y=cv2.getGaussianKernel(row, 200)
cannal= cannal_y*cannal_x.T
filter=255*cannal/np.linalg.norm(cannal)
wintage_im = np.copy(im)
for i in range(3):
    wintage_im[:,:,i]=wintage_im[:,:,i]*filter
plt.imshow(wintage_im)
plt.show()