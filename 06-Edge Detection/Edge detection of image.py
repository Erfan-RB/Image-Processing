#Edge detection of image 
import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('lana.jpg')
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Canny edge detection
edges = cv2.Canny(image= image_rgb, threshold1=100, threshold2=700)

fig, axs = plt.subplots(1, 2, figsize=(7, 4))

axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')
axs[1].imshow(edges)
axs[1].set_title('Image edges')

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()    