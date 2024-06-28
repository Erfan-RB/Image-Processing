#Image-Shearing
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('lana.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

width = image_rgb.shape[1]
height = image_rgb.shape[0]

#Define shearing factor
shearX = -0.15
shearY = 0

transformation_matrix = np.array([[1, shearX, 0],
                                  [0, 1, shearY]], dtype=np.float32)

sheared_image =cv2.warpAffine(image_rgb, transformation_matrix, (width, height))

fig, axs = plt.subplots(1, 2, figsize=(7, 4))

axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')
axs[1].imshow(sheared_image)
axs[1].set_title('Sheared image')

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()    
