import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)  # Use grayscale for histogram calculation

# Calculate the histogram
himg = cv2.calcHist([img], [0], None, [256], [0, 256])

# Display the original image
cv2.imshow("Original Image", img)

# Plot the histogram using Matplotlib
plt.plot(himg)
plt.title("Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()

# Wait for a key press and close the OpenCV window
cv2.waitKey(0)
cv2.destroyAllWindows()