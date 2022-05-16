import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
org_img = cv2.imread('Indoor_Low_Contrast.bmp', 0)

# Generate histogram (original)
org_hist = cv2.calcHist([org_img], [0], None, [256], [0, 256])

# Turn histogram into array
flat_org_hist = np.ravel(org_hist).astype('uint8')
print('histogram: \n', flat_org_hist)

# pdf
nr, nc = org_img.shape[:2]
#pdf = flat_org_hist / (nr*nc)
pdf = flat_org_hist / flat_org_hist.sum()

print('\n pdf: \n', pdf)
plt.stem(pdf)
plt.title('pdf')
plt.show()

# cdf
for i in range(len(pdf)):
    cdf = pdf[:]
    cdf[i] += pdf[i-1]
    i += 1
print('\n cdf: \n', cdf)
plt.plot(cdf)
plt.title('cdf')
plt.show()

# Equalize
eq_cdf = (cdf * 255).astype('uint8')
print('\n eq: \n', eq_cdf)
eq_img = eq_cdf[org_img]
eq_hist = cv2.calcHist([eq_img], [0], None, [256], [0, 256])

# Equalize by cv2
cv_eq = cv2.equalizeHist(org_img)
cv_hist = cv2.calcHist([cv_eq], [0], None, [256], [0, 256])

# ======================================================================

# Show images
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(org_img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Before')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(eq_img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('After')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(cv_eq, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Equalize by cv2')
plt.show()


# Show histograms
plt.subplot(3, 1, 1)
plt.stem(org_hist)
plt.xlim([-10, 266])
plt.xlabel('bin')
plt.ylabel('#')
plt.title('Original histogram')

plt.subplot(3, 1, 2)
plt.stem(eq_hist)
plt.xlim([-10, 266])
plt.xlabel('bin')
plt.ylabel('#')
plt.title('Equalized histogram')

plt.subplot(3, 1, 3)
plt.stem(cv_hist)
plt.xlim([-10, 266])
plt.xlabel('bin')
plt.ylabel('#')
plt.title('Equalized histogram by cv2')

plt.show()