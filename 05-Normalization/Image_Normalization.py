#Image_Normalization
import cv2
import numpy as np 
import matplotlib.pyplot as plt

image = cv2.imread('lana.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Split the image into channels
b, g, r = cv2.split(image_rgb)
# Normalization parameter
min_value = 0
max_value = 1
norm_type = cv2.NORM_MINMAX

b_normalized = cv2.normalize(b.astype('float'), None, min_value, max_value, norm_type)
g_normalized = cv2.normalize(g.astype('float'), None, min_value, max_value, norm_type)
r_normalized = cv2.normalize(r.astype('float'), None, min_value, max_value, norm_type)

normalized_image = cv2.merge((b_normalized, g_normalized, r_normalized))
print(normalized_image[:,:,0])

plt.imshow(normalized_image)
plt.xticks([])
plt.yticks([])
plt.title('Normalized Image')
plt.show()