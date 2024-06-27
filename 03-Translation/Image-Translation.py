#Image-Translation
import cv2
import matplotlib.pyplot as plt
import numpy as np

#Load Image
img = cv2.imread('lana.jpg')
#Convert BGR => RGB
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

width = image_rgb.shape[1]
height = image_rgb.shape[0]

tx = 100
ty = 70

#translation matrix
translation_matrix = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
translated_image = cv2.warpAffine(image_rgb, translation_matrix,(width, height))

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(7, 4))

#Plot
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')
axs[1].imshow(translated_image)
axs[1].set_title('Image Translation')

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()