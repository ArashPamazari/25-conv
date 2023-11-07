import cv2
import numpy as np

image = cv2.imread('images/flower_input.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

result = np.zeros(image.shape)

rows, cols = image.shape

for i in range(14, rows-14):
    for j in range(14, cols-14):
        if image[i, j] < 200:
            small_image = image[i-14:i+15, j-14:j+15]
            small_image_1d = small_image.reshape(841)
            small_image_1d_sorted = np.sort(small_image_1d)
            result[i, j] = small_image_1d_sorted[420]
        else:
            result[i, j] = image[i, j]

cv2.imwrite('flower.jpg', result)