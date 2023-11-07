import cv2
import numpy as np

image = cv2.imread('images/building.tif')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

result_1 = np.zeros(image.shape)
result_2 = np.zeros(image.shape)

mask_1 = np.array([[-1, 0, 1], 
                [-1, 0, 1],
                [-1, 0, 1]])

mask_2 = np.array([[-1, -1, -1], 
                [0, 0, 0],
                [1, 1, 1]])

rows, cols = image.shape

for i in range(1, rows-1):
    for j in range(1, cols-1):
        small_image = image[i-1:i+2, j-1:j+2]
        result_1[i, j] = np.sum(small_image * mask_1)
        result_2[i, j] = np.sum(small_image * mask_2)

cv2.imwrite('buildingOne.jpg', result_1)
cv2.imwrite('buildingTwo.jpg', result_2)