import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load image and read it using 'imread()'
image1 = mpimg.imread(r"C:\Users\DELL\Pictures\Camera Roll\Logo.png")
image2 = cv2.imread(r"C:\Users\DELL\Pictures\Camera Roll\Logo.png")

M,N,C = image1.shape
# To calculate number of pixels in image
pixel = M*N
print(pixel)

# Display image
plt.figure()
plt.subplot(1,2,1)
plt.imshow(image1)
plt.title("Read image by using Matplotlib")

plt.subplot(1,2,2)
plt.imshow(image2)
plt.title("Read image by using OpenCV")

plt.show()

# Convert BGR image into RGB and Gray scale
rgb = cv2.cvtColor(image2,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

plt.figure()

plt.subplot(1,3,1)
plt.imshow(image2)
plt.title("BGR")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(rgb)
plt.title("RGB")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(gray, cmap = "gray")
plt.title("GRAY")
plt.axis("off")

plt.show()

image3 = cv2.imread(r'C:\Users\DELL\Pictures\Camera Roll\Eren.jfif')

plt.figure(figsize=(25,17))

# Convert BGR → RGB
rgb = cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)

# Convert to Grayscale
gray = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(15, 6))

# Image
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")

# Histogram
plt.subplot(1, 2, 2)
plt.hist(gray.ravel(), bins=256, range=[0, 255])
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.show()

img = cv2.imread(r'C:\Users\DELL\Pictures\Camera Roll\Eren.jfif')
cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

rows, cols = img.shape[:2]
M = np.float32([[1,0,50],[0,1,30]])
translated = cv2.warpAffine(img, M, (cols,rows))
cv2.imshow("translated image", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()

scaled = cv2.resize(img, None, fx=1.5, fy=1.5)

cv2.imshow("scaled image",scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()