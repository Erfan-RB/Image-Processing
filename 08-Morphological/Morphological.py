#Morphological
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('lana.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create a structuring element
kernel = np.ones((3, 3), np.uint8)
# Perform dilation
dilated = cv2.dilate(image_gray, kernel, iterations=2)
# Perform dilation
eroded = cv2.erode(image_gray, kernel, iterations=2)

opening = cv2.morphologyEx(image_gray, cv2.MORPH_CLOSE,kernel)
closing = cv2.morphologyEx(image_gray, cv2.MORPH_CLOSE, kernel)

fig, axs = plt.subplots(2, 2, figsize=(7, 7))

# Plot the Dilated Image
axs[0,0].imshow(dilated, cmap='Greys')
axs[0,0].set_title('Dilated Image')
axs[0,0].set_xticks([])
axs[0,0].set_yticks([])

# Plot the Eroded Image
axs[0,1].imshow(eroded, cmap='Greys')
axs[0,1].set_title('Eroded Image')
axs[0,1].set_xticks([])
axs[0,1].set_yticks([])

# Plot the opening (erosion followed by dilation)
axs[1,0].imshow(opening, cmap='Greys')
axs[1,0].set_title('Opening')
axs[1,0].set_xticks([])
axs[1,0].set_yticks([])

# Plot the closing (dilation followed by erosion)
axs[1,1].imshow(closing, cmap='Greys')
axs[1,1].set_title('Closing')
axs[1,1].set_xticks([])
axs[1,1].set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()