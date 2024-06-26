#Image-Rotation
import cv2
import matplotlib.pyplot as plt

#Load image
img = cv2.imread('lana.jpg')
#Convert BGR => RGB
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#Image Rotation
center = (image_rgb.shape[1] // 2, image_rgb.shape[0] // 2)
angle = 30
scale = 1

rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image_rgb, rotation_matrix, (img.shape[1],img.shape[0]))

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(7, 4))
axs[0].imshow(image_rgb)
axs[0].set_title('Orginal Image')
axs[1].imshow(rotated_image)
axs[1].set_title('Image Rotation')

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()    