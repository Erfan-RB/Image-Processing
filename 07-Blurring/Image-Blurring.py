#Image-Blurring
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('lana.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Apply blur
blurred = cv2.GaussianBlur(image, (3, 3), 0)
blurred_rgb = cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB)

fig, axs = plt.subplots(1, 2, figsize=(7, 4))

axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')
axs[1].imshow(blurred_rgb)
axs[1].set_title('Blurred Image')

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()