import cv2
import numpy as np

image = cv2.imread('images/img_4.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def convolution(conv):
    result = np.zeros(image.shape)

    mask = np.ones((conv, conv)) / conv ** 2

    rows, cols = image.shape

    for i in range(conv//2, rows-conv//2):
        for j in range(conv//2, cols-conv//2):
            small_image = image[i-conv//2:i+conv//2+1, j-conv//2:j+conv//2+1]
            result[i, j] = np.sum(small_image * mask)
    
    return result

list_size = [3, 5, 7, 15]
i = 0

for size in list_size:
    res = convolution(size)
    cv2.imwrite(f'dynamic{i}.jpg', res)
    i += 1