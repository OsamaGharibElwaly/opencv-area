# Computer Vision: Essential Terminology (50 Concepts)

## 🔹 Fundamentals
- **Image Processing** – Manipulating an image to enhance it or extract information.
- **Computer Vision** – Enabling computers to interpret and understand visual data.
- **Dataset** – A collection of images (labeled or unlabeled) used to train or test CV models.
- **Noise** – Random variations in pixel values that degrade image quality.
- **Noise Reduction** – Techniques (e.g., blurring, filtering) to remove noise.

## 🔹 Image Representation
- **Grayscale** – Single-channel image where each pixel represents intensity (0=black, 255=white).
- **RGB** – Color model using Red, Green, Blue channels (3 channels).
- **BGR** – Same as RGB but channel order used by OpenCV (Blue, Green, Red).
- **Histogram** – Graph showing pixel intensity distribution per channel.
- **Image ROI (Region of Interest)** – A selected subset of an image to focus processing on.

## 🔹 Basic Operations
- **Image Masking** – Using a binary mask to isolate specific image regions.
- **Bitwise Operations** – AND, OR, XOR, NOT applied pixel-wise between images or masks.
- **Image Merging** – Combining multiple single-channel images into one multi-channel image.
- **Image Blending** – Linearly combining two images with a weight (e.g., `α * img1 + β * img2`).
- **Mathematical Formula** – Any pixel-wise or region-wise equation used in CV (e.g., convolution, affine maps).

## 🔹 Filtering & Kernels
- **Kernel (Filter Matrix)** – Small matrix convolved with an image to apply effects (blur, edge detection).
- **Convolution** – Sliding a kernel over an image, computing element-wise products and sum.
- **Image Filtering** – Applying a kernel or operation to modify pixel values.
- **Blurring** – Reducing detail and noise by averaging pixels (e.g., Gaussian blur).
- **Smoothing** – Synonym for blurring; suppresses high-frequency information.
- **Sharpening** – Enhancing edges by amplifying high-frequency components.

## 🔹 Morphological Operations (Binary/Shapes)
- **Morphological Operations** – Processes based on image shape (structuring element).
- **Erosion** – Shrinks foreground regions; removes small white noise.
- **Dilation** – Expands foreground regions; fills small holes.
- **Opening** – Erosion followed by dilation; removes small objects/noise.
- **Closing** – Dilation followed by erosion; fills small holes/breaks.
- **Morphological Gradient** – Difference between dilation and erosion; finds object boundaries.

## 🔹 Geometry & Transformations
- **Image Transformations** – Changing pixel locations via mathematical mapping.
- **Affine Transformation** – Linear mapping (translation, rotation, scale, shear) preserving points/lines.
- **Translation** – Shifting an image along X and Y axes.
- **Rotation** – Turning an image around a point by a given angle.
- **Scaling** – Enlarging or shrinking an image (resizing).
- **Axes** – Reference lines (X = horizontal, Y = vertical) for transformations.
- **Pinhole Cameras** – Simplified camera model where light passes through a tiny hole to form an inverted image.

## 🔹 Features & Detection
- **Feature Extraction** – Converting raw pixels into compact, meaningful descriptors.
- **Feature Detection** – Identifying keypoints (corners, blobs, edges) in an image.
- **Corner** – Point where two edges meet; high information content.
- **Template Matching** – Sliding a smaller image (template) over a larger image to find matches.
- **Object Detection** – Locating instances of real-world objects (e.g., faces, cars) in an image.
- **Object Extraction** – Isolating a detected object from the background.
- **Image Segmentation** – Partitioning an image into regions (pixel-level classification).

## 🔹 Advanced / Essential Additions (10 extra)
- **Structuring Element** – Shape (e.g., cross, rectangle) used in morphological ops.
- **Edge Detection** – Finding sharp intensity changes (e.g., Canny, Sobel).
- **Contour** – Curve joining continuous boundary points of a shape.
- **Thresholding** – Converting grayscale to binary based on a pixel intensity cutoff.
- **Bounding Box** – Rectangle enclosing a detected object.
- **Intersection over Union (IoU)** – Overlap ratio between predicted and ground-truth boxes; metric for detection.
- **Data Augmentation** – Generating new training images via flips, rotations, color shifts, etc.
- **Convolutional Neural Network (CNN)** – Deep learning model specialized for grid-like data (images).
- **Padding** – Adding extra pixels around an image border before convolution.
- **Stride** – Step size kernel moves during convolution.

---

## 📚 How to Use This List
1. Read **from top to bottom** – concepts build on previous ones.  
2. Each term links logically to the next (Basics → Representations → Operations → Filters → Morphology → Transforms → Features → Advanced).  
3. For beginners, stop after `Object Extraction`; revisit `Advanced` section later.

---
# 30 Most Essential OpenCV Functions (cv2)

This table organizes functions in a typical computer vision pipeline: **I/O → Preprocessing → Feature Extraction → Geometric Transformations → Output**.

| Function | Used For | Key Parameters | Returns |
| :--- | :--- | :--- | :--- |
| **1. cv2.imread** | Reading an image from a file. | `filename` (string), `flags` (e.g., `cv2.IMREAD_GRAYSCALE`) [citation:5] | NumPy array (image) |
| **2. cv2.imshow** | Displaying an image in a window. | `winname` (window name), `mat` (image array) [citation:5] | None |
| **3. cv2.cvtColor** | Converting an image between color spaces (e.g., BGR to Grayscale or HSV). | `src` (image), `code` (e.g., `cv2.COLOR_BGR2GRAY`) [citation:4][citation:5] | NumPy array (converted image) |
| **4. cv2.resize** | Resizing an image (scaling up or down). | `src`, `dsize` (output size), `interpolation` (e.g., `cv2.INTER_LINEAR`) [citation:4][citation:7] | NumPy array (resized image) |
| **5. cv2.GaussianBlur** | Smoothing/Blurring an image to reduce noise using a Gaussian kernel. | `src`, `ksize` (kernel size, must be odd), `sigmaX` [citation:4][citation:6] | NumPy array (blurred image) |
| **6. cv2.threshold** | Creating a binary image based on a fixed intensity threshold. | `src`, `thresh` (threshold value), `maxval`, `type` (e.g., `cv2.THRESH_BINARY`) [citation:5] | `retval` (used threshold), `dst` (binary image) |
| **7. cv2.adaptiveThreshold** | Thresholding an image where the threshold value varies across the image (good for uneven lighting). | `src`, `maxValue`, `adaptiveMethod`, `thresholdType`, `blockSize`, `C` [citation:6] | NumPy array (binary image) |
| **8. cv2.erode** | Eroding away boundaries of the foreground object. Useful for removing small white noise. | `src`, `kernel` (structuring element), `iterations` [citation:6][citation:9] | NumPy array (eroded image) |
| **9. cv2.dilate** | Expanding the foreground object. Useful for filling small holes. | `src`, `kernel`, `iterations` [citation:6][citation:9] | NumPy array (dilated image) |
| **10. cv2.morphologyEx** | Performing advanced morphological operations like Opening, Closing, or Gradient. | `src`, `op` (e.g., `cv2.MORPH_OPEN`), `kernel` [citation:6][citation:9] | NumPy array (transformed image) |
| **11. cv2.Canny** | Detecting edges in an image using the Canny Edge Detection algorithm. | `src`, `threshold1`, `threshold2` [citation:4][citation:6] | NumPy array (binary edge map) |
| **12. cv2.Sobel** | Computing image gradients (derivatives) in X or Y direction to find edges. | `src`, `ddepth`, `dx`, `dy`, `ksize` [citation:2][citation:3][citation:5] | NumPy array (gradient image) |
| **13. cv2.findContours** | Finding the boundaries/contours of white objects in a binary image. | `image`, `mode` (e.g., `cv2.RETR_EXTERNAL`), `method` [citation:6] | `contours` (list of points), `hierarchy` |
| **14. cv2.drawContours** | Drawing the detected contours onto an image. | `image`, `contours`, `contourIdx`, `color`, `thickness` [citation:6] | None (modifies image) |
| **15. cv2.matchTemplate** | Searching for a template (small image) inside a larger image. | `image`, `templ`, `method` (e.g., `cv2.TM_CCOEFF_NORMED`) [citation:6] | NumPy array (result matrix) |
| **16. cv2.goodFeaturesToTrack** | Detecting strong corners/features in an image (Shi-Tomasi algorithm). | `image`, `maxCorners`, `qualityLevel`, `minDistance` [citation:4][citation:6] | Array of corner coordinates |
| **17. cv2.calcHist** | Calculating the histogram of an image (distribution of pixel intensities). | `images`, `channels`, `mask`, `histSize`, `ranges` [citation:6] | NumPy array (histogram values) |
| **18. cv2.equalizeHist** | Improving contrast by spreading out the most frequent intensity values. | `src` (grayscale image) [citation:6] | NumPy array (equalized image) |
| **19. cv2.inRange** | Extracting specific colors from an image based on range bounds (used with HSV color space). | `src`, `lowerb`, `upperb` [citation:6] | NumPy array (binary mask) |
| **20. cv2.addWeighted** | Blending two images together using a linear combination (alpha blending). | `src1`, `alpha`, `src2`, `beta`, `gamma` [citation:5][citation:6] | NumPy array (blended image) |
| **21. cv2.bitwise_and** | Applying a mask to an image (extracting the Region of Interest). | `src1`, `src2`, `mask` [citation:5][citation:6] | NumPy array (masked image) |
| **22. cv2.warpAffine** | Applying geometric transformations (translation, rotation, scaling) to an image. | `src`, `M` (2x3 transformation matrix), `dsize` [citation:6][citation:7] | NumPy array (transformed image) |
| **23. cv2.getRotationMatrix2D** | Calculating the transformation matrix required to rotate an image. | `center`, `angle`, `scale` [citation:6][citation:7] | 2x3 NumPy array (transformation matrix) |
| **24. cv2.warpPerspective** | Applying a perspective transformation (changing the view angle, like a bird's eye view). | `src`, `M` (3x3 matrix), `dsize` [citation:6][citation:7] | NumPy array (transformed image) |
| **25. cv2.putText** | Adding text annotations (labels, titles) to an image. | `img`, `text`, `org` (position), `fontFace`, `fontScale`, `color`, `thickness` [citation:6] | None (modifies image) |
| **26. cv2.rectangle** | Drawing a rectangle on an image (e.g., to draw bounding boxes around detected objects). | `img`, `pt1`, `pt2`, `color`, `thickness` [citation:4][citation:6] | None (modifies image) |
| **27. cv2.circle** | Drawing a circle on an image. | `img`, `center`, `radius`, `color`, `thickness` (`-1` for filled) [citation:4][citation:6] | None (modifies image) |
| **28. cv2.imwrite** | Saving an image to a file on disk. | `filename`, `img` [citation:5][citation:6] | `True` (success) or `False` (failure) |
| **29. cv2.VideoCapture** | Capturing video from a camera or reading a video file frame by frame. | `index` (camera ID) or `filename` [citation:5][citation:6] | `cv2.VideoCapture` object |
| **30. cv2.CascadeClassifier** | Loading a pre-trained Haar Cascade model for object detection (e.g., faces, eyes). | `filename` (XML file path) [citation:4][citation:6] | `cv2.CascadeClassifier` object |


# Images with Code
# 📚 OpenCV Complete Tutorial Master Guide

## Core Operations

---

### 1. Image Blending

Combining two images with transparency using `cv2.addWeighted()`.

```python
import cv2

# Load images
img1 = cv2.imread('images/02-core-operations/blending.jpg')
img2 = cv2.imread('images/02-core-operations/affine.jpg')

# Resize to same dimensions
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Blend images (70% img1, 30% img2)
blended = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

# Display results
cv2.imshow('Image 1', img1)
cv2.imshow('Image 2', img2)
cv2.imshow('Blended Result', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
Result: ![Blended Result](https://images/02-core-operations/blending.jpg)

### 2. Affine Transformation

Linear mapping preserving points, lines, and parallelism.

```python
import cv2
import numpy as np

img = cv2.imread('images/02-core-operations/affine.jpg')
rows, cols = img.shape[:2]

# Define source and destination points
pts_src = np.float32([[50, 50], [200, 50], [50, 200]])
pts_dst = np.float32([[10, 100], [200, 50], [100, 250]])

# Get affine transformation matrix
M = cv2.getAffineTransform(pts_src, pts_dst)

# Apply transformation
transformed = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('Affine Transformed', transformed)
cv2.waitKey(0)
```
Result: ![Affine Transformed](https://images/02-core-operations/affine.jpg)

### 3. Image Translation

Shifting an image along X and Y axes.

```python
import cv2
import numpy as np

img = cv2.imread('images/02-core-operations/translation.jpg')

# Translation matrix: [1, 0, tx], [0, 1, ty]
tx, ty = 100, 50
M = np.float32([[1, 0, tx], [0, 1, ty]])

# Apply translation
translated = cv2.warpAffine(img, M, (img.shape[1] + tx, img.shape[0] + ty))

cv2.imshow('Original', img)
cv2.imshow('Translated', translated)
cv2.waitKey(0)
```
Result: ![Translated Result](https://images/02-core-operations/translation.jpg)

### 4. Image Rotation

Rotating an image around a center point.

```python
import cv2

img = cv2.imread('images/02-core-operations/rotation.jpg')
rows, cols = img.shape[:2]

# Get rotation matrix (center, angle, scale)
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)

# Apply rotation
rotated = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('Rotated 45°', rotated)
cv2.waitKey(0)
```
Result: ![Rotated Result](https://images/02-core-operations/rotation.jpg)

### 5. Perspective Transformation

Changing the view angle (bird's eye view).

```python
import cv2
import numpy as np

img = cv2.imread('images/02-core-operations/perspective.jpg')
rows, cols = img.shape[:2]

# Source points (original corners)
pts_src = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])

# Destination points (warped corners)
pts_dst = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# Get perspective matrix
M = cv2.getPerspectiveTransform(pts_src, pts_dst)

# Apply transformation
warped = cv2.warpPerspective(img, M, (300, 300))

cv2.imshow('Original', img)
cv2.imshow('Perspective Transformed', warped)
cv2.waitKey(0)
```
Result: ![Perspective Transformed](https://images/02-core-operations/perspective.jpg)
# 6. Arithmetic Operations
Adding, subtracting, and bitwise operations on images.

```python
import cv2
import numpy as np

img1 = cv2.imread('images/02-core-operations/blending.jpg')
img2 = cv2.imread('images/02-core-operations/affine.jpg')
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Image Addition
addition = cv2.add(img1, img2)

# Image Subtraction
subtraction = cv2.subtract(img1, img2)

# Bitwise AND
bitwise_and = cv2.bitwise_and(img1, img2)

cv2.imshow('Addition', addition)
cv2.imshow('Subtraction', subtraction)
cv2.imshow('Bitwise AND', bitwise_and)
cv2.waitKey(0)
```

Result:
[https://images/02-core-operations/blending.jpg](https://images/02-core-operations/blending.jpg)

# 7. Image Thresholding
Converting grayscale to binary based on intensity cutoff.

```python
import cv2

img = cv2.imread('images/03-image-processing/03-image-thresholding/threshold.jpg', 0)

# Simple threshold
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Adaptive threshold
adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Otsu's threshold
_, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('Original', img)
cv2.imshow('Binary Threshold', binary)
cv2.imshow('Adaptive Threshold', adaptive)
cv2.imshow("Otsu's Threshold", otsu)
cv2.waitKey(0)
```

Results:

| Binary | Adaptive | Otsu |
|--------|----------|------|
| ![https://images/03-image-processing/03-image-thresholding/threshold.jpg](https://images/03-image-processing/03-image-thresholding/threshold.jpg) | ![https://images/03-image-processing/03-image-thresholding/ada_threshold.jpg](https://images/03-image-processing/03-image-thresholding/ada_threshold.jpg) | ![https://images/03-image-processing/03-image-thresholding/otsu.jpg](https://images/03-image-processing/03-image-thresholding/otsu.jpg) |

# 8. Smoothing & Blurring
Reducing noise using different filter types.

```python
import cv2

img = cv2.imread('images/03-image-processing/04-smoothing-images/gaussian.jpg')

# Gaussian Blur
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# Median Blur (good for salt-pepper noise)
median = cv2.medianBlur(img, 5)

# Bilateral Filter (preserves edges)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow('Original', img)
cv2.imshow('Gaussian Blur', gaussian)
cv2.imshow('Median Blur', median)
cv2.imshow('Bilateral Filter', bilateral)
cv2.waitKey(0)
```

Results:

| Gaussian | Median | Bilateral |
|----------|--------|-----------|
| ![https://images/03-image-processing/04-smoothing-images/gaussian.jpg](https://images/03-image-processing/04-smoothing-images/gaussian.jpg) | ![https://images/03-image-processing/04-smoothing-images/median.jpg](https://images/03-image-processing/04-smoothing-images/median.jpg) | ![https://images/03-image-processing/04-smoothing-images/bilateral.jpg](https://images/03-image-processing/04-smoothing-images/bilateral.jpg) |
## 8. Smoothing & Blurring
Reducing noise using different filter types.

```python
import cv2

img = cv2.imread('images/03-image-processing/04-smoothing-images/gaussian.jpg')

# Gaussian Blur
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# Median Blur (good for salt-pepper noise)
median = cv2.medianBlur(img, 5)

# Bilateral Filter (preserves edges)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow('Original', img)
cv2.imshow('Gaussian Blur', gaussian)
cv2.imshow('Median Blur', median)
cv2.imshow('Bilateral Filter', bilateral)
cv2.waitKey(0)
```

**Results:**

| Gaussian | Median | Bilateral |
|----------|--------|-----------|
| ![Gaussian](https://images/03-image-processing/04-smoothing-images/gaussian.jpg) | ![Median](https://images/03-image-processing/04-smoothing-images/median.jpg) | ![Bilateral](https://images/03-image-processing/04-smoothing-images/bilateral.jpg) |

## 9. Morphological Transformations
Erosion, dilation, opening, and closing operations.

```python
import cv2
import numpy as np

img = cv2.imread('images/03-image-processing/05-morphological-transformations/gradient.png', 0)
kernel = np.ones((5, 5), np.uint8)

# Erosion (shrinks foreground)
erosion = cv2.erode(img, kernel, iterations=1)

# Dilation (expands foreground)
dilation = cv2.dilate(img, kernel, iterations=1)

# Opening (erosion then dilation)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Closing (dilation then erosion)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Morphological Gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('Original', img)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.imshow('Gradient', gradient)
cv2.waitKey(0)
```

**Results:**

| Erosion | Dilation | Opening | Closing | Gradient |
|---------|----------|---------|---------|----------|
| ![Erosion](https://images/03-image-processing/05-morphological-transformations/erosion.png) | ![Dilation](https://images/03-image-processing/05-morphological-transformations/dilation.png) | ![Opening](https://images/03-image-processing/05-morphological-transformations/opening.png) | ![Closing](https://images/03-image-processing/05-morphological-transformations/closing.png) | ![Gradient](https://images/03-image-processing/05-morphological-transformations/gradient.png) |

## 10. Edge Detection (Canny)
Detecting edges using the Canny algorithm.

```python
import cv2

img = cv2.imread('images/03-image-processing/07-canny-edge-detection/canny1.jpg', 0)

# Apply Canny edge detection
edges = cv2.Canny(img, 100, 200)

# With different thresholds
edges_low = cv2.Canny(img, 50, 150)
edges_high = cv2.Canny(img, 150, 250)

cv2.imshow('Original', img)
cv2.imshow('Canny Edges', edges)
cv2.imshow('Low Threshold', edges_low)
cv2.imshow('High Threshold', edges_high)
cv2.waitKey(0)
```

**Results:**

![Canny Edge Detection](https://images/03-image-processing/07-canny-edge-detection/canny1.jpg)
# 11. Image Gradients (Sobel)
Computing image derivatives in X and Y directions.

```python
import cv2
import numpy as np

img = cv2.imread('images/03-image-processing/06-image-gradients/gradients.jpg', 0)

# Sobel gradients
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Convert to uint8
sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))

# Combine gradients
sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)

cv2.imshow('Original', img)
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('Combined', sobel_combined)
cv2.waitKey(0)
```
Result:
[https://images/03-image-processing/06-image-gradients/gradients.jpg](https://images/03-image-processing/06-image-gradients/gradients.jpg)

# 12. Template Matching
Finding a template image inside a larger image.

```python
import cv2

img = cv2.imread('images/03-image-processing/12-template-matching/template_ccoeff_1.jpg')
template = cv2.imread('images/03-image-processing/12-template-matching/template_ccoeff_1.jpg')
h, w = template.shape[:2]

# Match template
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Draw rectangle around match
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

cv2.imshow('Detected', img)
cv2.waitKey(0)
```
Results:
[https://images/03-image-processing/12-template-matching/template_ccoeff_1.jpg](https://images/03-image-processing/12-template-matching/template_ccoeff_1.jpg)

# 13. Hough Line Transform
Detecting lines in an image.

```python
import cv2
import numpy as np

img = cv2.imread('images/03-image-processing/13-hough-line-transform/houghlines3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

# Hough Line Transform
lines = cv2.HoughLines(edges, 1, np.pi/180, 150)

# Draw lines
if lines is not None:
    for rho, theta in lines[:, 0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('Detected Lines', img)
cv2.waitKey(0)
```
Result:
[https://images/03-image-processing/13-hough-line-transform/houghlines3.jpg](https://images/03-image-processing/13-hough-line-transform/houghlines3.jpg)

# Feature Detection

## 14. Harris Corner Detection
Detecting corners in an image.

```python
import cv2
import numpy as np

img = cv2.imread('images/04-feature-detection/02-harris-corner-detection/harris_result.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Harris corner detection
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate to mark corners
dst = cv2.dilate(dst, None)

# Threshold for marking corners
img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('Harris Corners', img)
cv2.waitKey(0)
```
Result:
[https://images/04-feature-detection/02-harris-corner-detection/harris_result.jpg](https://images/04-feature-detection/02-harris-corner-detection/harris_result.jpg)
# 15. SIFT Features
Scale-Invariant Feature Transform for keypoint detection.

```python
import cv2

img = cv2.imread('images/04-feature-detection/04-sift-features/sift_keypoints.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors
kp, des = sift.detectAndCompute(gray, None)

# Draw keypoints
img_kp = cv2.drawKeypoints(img, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SIFT Keypoints', img_kp)
cv2.waitKey(0)
```
Result:
https://images/04-feature-detection/04-sift-features/sift_keypoints.jpg

# 16. ORB Features
Oriented FAST and Rotated BRIEF (faster alternative to SIFT).

```python
import cv2

img = cv2.imread('images/04-feature-detection/08-orb-features/orb_kp.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create ORB detector
orb = cv2.ORB_create()

# Detect keypoints and compute descriptors
kp, des = orb.detectAndCompute(gray, None)

# Draw keypoints
img_kp = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))

cv2.imshow('ORB Keypoints', img_kp)
cv2.waitKey(0)
```
Result:
https://images/04-feature-detection/08-orb-features/orb_kp.jpg

# 17. Feature Matching
Matching features between two images.

```python
import cv2

img1 = cv2.imread('images/04-feature-detection/09-feature-matching/matcher_result1.jpg')
img2 = cv2.imread('images/04-feature-detection/09-feature-matching/matcher_result2.jpg')

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect and compute features
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Create FLANN matcher
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
flann = cv2.FlannBasedMatcher(index_params, {})

# Match features
matches = flann.knnMatch(des1, des2, k=2)

# Apply ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

# Draw matches
result = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None)

cv2.imshow('Feature Matches', result)
cv2.waitKey(0)
```
Results:
https://images/04-feature-detection/09-feature-matching/matcher_result1.jpg
# 18. Camera Calibration

Finding camera intrinsic and extrinsic parameters.

```python
import cv2
import numpy as np

# Chessboard dimensions
pattern_size = (9, 6)
square_size = 25  # mm

# Prepare object points
objp = np.zeros((pattern_size[0] * pattern_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)
objp *= square_size

# Arrays to store object and image points
objpoints = []
imgpoints = []

img = cv2.imread('images/05-camera-calibration/calib_pattern.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find chessboard corners
ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)

if ret:
    objpoints.append(objp)
    imgpoints.append(corners)
    
    # Calibrate camera
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    
    # Undistort image
    dst = cv2.undistort(img, mtx, dist, None, mtx)
    
    print(f"Camera Matrix:\n{mtx}")
    print(f"Distortion Coefficients:\n{dist}")

cv2.imshow('Calibration Pattern', img)
cv2.waitKey(0)
```

Results:

| Pattern | Radial Distortion | Result |
|---------|-------------------|--------|
| ![Calibration Pattern](https://images/05-camera-calibration/calib_pattern.jpg) | ![Radial Distortion](https://images/05-camera-calibration/calib_radial.jpg) | ![Result](https://images/05-camera-calibration/calib_result.jpg) |

## Contour Detection

# 19. Finding and Drawing Contours

```python
import cv2
import numpy as np

img = cv2.imread('images/03-image-processing/09-contours/contour.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

cv2.imshow('Contours', img)
cv2.waitKey(0)
``` 

## Image Segmentation
# 20. GrabCut Algorithm

Interactive foreground extraction.

```python
import cv2
import numpy as np

img = cv2.imread('images/03-image-processing/16-grabcut-foreground-extraction/grabcut_output1.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

# GrabCut parameters
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)

# Define rectangle around object
rect = (50, 50, img.shape[1] - 50, img.shape[0] - 50)

# Apply GrabCut
cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

# Create mask where 0=background, 1=foreground
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Apply mask to image
result = img * mask2[:, :, np.newaxis]
cv2.imshow('Extracted Object', result)
cv2.waitKey(0)
```

### Results:
- Mask: ![Mask](https://images/03-image-processing/16-grabcut-foreground-extraction/grabcut_mask.jpg)
- Rectangle: ![Rectangle](https://images/03-image-processing/16-grabcut-foreground-extraction/grabcut_rect.jpg)
- Output: ![Output](https://images/03-image-processing/16-grabcut-foreground-extraction/grabcut_output1.jpg)

# 21. Watershed Segmentation

## Watershed Algorithm

```python
import cv2
import numpy as np

img = cv2.imread('images/03-image-processing/15-watershed-segmentation/water_coins.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Noise removal
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)

# Sure background area
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
## 22. Hough Circle Transform

Detecting circles in an image using Hough Circle Transform.

```python
import cv2
import numpy as np

img = cv2.imread('images/03-image-processing/14-hough-circle-transform/houghcircles2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Detect circles
circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=50, param2=30, minRadius=10, maxRadius=50)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Draw outer circle
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Draw center
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('Detected Circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

Result:  
[https://images/03-image-processing/14-hough-circle-transform/houghcircles2.jpg](https://images/03-image-processing/14-hough-circle-transform/houghcircles2.jpg)

## 23. Image Pyramids

Creating Gaussian and Laplacian pyramids for multi-scale processing.

```python
import cv2

img = cv2.imread('images/03-image-processing/08-image-pyramids/messipyr.jpg')

# Gaussian Pyramid
level1 = cv2.pyrDown(img)
level2 = cv2.pyrDown(level1)
level3 = cv2.pyrDown(level2)

# Laplacian Pyramid
laplacian1 = cv2.subtract(img, cv2.pyrUp(level1))
laplacian2 = cv2.subtract(level1, cv2.pyrUp(level2))
laplacian3 = cv2.subtract(level2, cv2.pyrUp(level3))

cv2.imshow('Original', img)
cv2.imshow('Gaussian Level 1', level1)
cv2.imshow('Gaussian Level 2', level2)
cv2.imshow('Laplacian Level 1', laplacian1)
cv2.waitKey(0)
```

Results:  
- Original: [https://images/03-image-processing/08-image-pyramids/messipyr.jpg](https://images/03-image-processing/08-image-pyramids/messipyr.jpg)  
- Gaussian Level 1: [https://images/03-image-processing/08-image-pyramids/messiup.jpg](https://images/03-image-processing/08-image-pyramids/messiup.jpg)  
- Gaussian Level 2: [https://images/03-image-processing/08-image-pyramids/res_mario.jpg](https://images/03-image-processing/08-image-pyramids/res_mario.jpg)  
- Laplacian: -

## 24. Histogram Calculation & Equalization

Understanding pixel intensity distribution.

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/03-image-processing/10-histograms/histogram.jpg', 0)

# Calculate histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Histogram equalization
equalized = cv2.equalizeHist(img)

# Calculate equalized histogram
hist_eq = cv2.calcHist([equalized], [0], None, [256], [0, 256])

# Plot histograms
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(hist)
plt.title('Original Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.plot(hist_eq)
plt.title('Equalized Histogram')
plt.xlabel('Pixel Intensity')

plt.show()

cv2.imshow('Original', img)
cv2.imshow('Equalized', equalized)
cv2.waitKey(0)
```

Result:  
[https://images/03-image-processing/10-histograms/histogram.jpg](https://images/03-image-processing/10-histograms/histogram.jpg)

## 25. Color Space Conversion

Working with different color spaces (HSV, LAB, YCrCb).

```python
import cv2

img = cv2.imread('images/02-core-operations/blending.jpg')

# Convert to different color spaces
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
ycbcr = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# Split channels
h, s, v = cv2.split(hsv)
l, a, b = cv2.split(lab)
y, cr, cb = cv2.split(ycbcr)

cv2.imshow('Original BGR', img)
cv2.imshow('HSV - Hue', h)
cv2.imshow('HSV - Saturation', s)
cv2.imshow('HSV - Value', v)
cv2.waitKey(0)
```
# 26. Color Detection using HSV
Detecting specific colors in an image.

```python
import cv2
import numpy as np

img = cv2.imread('images/03-image-processing/01-changing-colorspaces/color_detection.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define range for red color
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])

# Create mask for red
mask_red = cv2.inRange(hsv, lower_red, upper_red)

# Apply mask to original image
result = cv2.bitwise_and(img, img, mask=mask_red)

cv2.imshow('Original', img)
cv2.imshow('Red Mask', mask_red)
cv2.imshow('Red Detected', result)
cv2.waitKey(0)
```

# 27. Image Inpainting
Removing unwanted objects or repairing damaged images.

```python
import cv2
import numpy as np

img = cv2.imread('images/07-computational-photography/inpaint_basics.jpg')

# Create mask (white areas to be inpainted)
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:200, 100:200] = 255  # White square to remove

# Inpainting using Telea algorithm
result_telea = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

# Inpainting using Navier-Stokes
result_ns = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

cv2.imshow('Original', img)
cv2.imshow('Mask', mask)
cv2.imshow('Telea Result', result_telea)
cv2.imshow('Navier-Stokes Result', result_ns)
cv2.waitKey(0)
```

Results:

- Original: ![Original](https://images/07-computational-photography/inpaint_basics.jpg)
- Mask: -
- Result: ![Result](https://images/07-computational-photography/inpaint_result.jpg)

# 28. Image Denoising
Removing noise while preserving edges.

```python
import cv2

img = cv2.imread('images/07-computational-photography/nlm_multi.jpg')

# Non-Local Means Denoising
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

cv2.imshow('Original Noisy', img)
cv2.imshow('Denoised', dst)
cv2.waitKey(0)
```

Results:

- Noisy: ![Noisy](https://images/07-computational-photography/nlm_multi.jpg)
- Denoised: ![Denoised](https://images/07-computational-photography/nlm_result1.jpg)

# 29. High Dynamic Range (HDR)
Combining multiple exposures to create HDR image.

```python
import cv2
import numpy as np

# Load images with different exposures
images = []
exposures = []

for i in range(3):
    img = cv2.imread(f'images/07-computational-photography/exposures_{i}.jpg')
    images.append(img)
    exposures.append(1.0 / (2 ** i))

# Create HDR image
merge_mertens = cv2.createMergeMertens()
hdr = merge_mertens.process(images)

# Convert to 8-bit for display
hdr_8bit = np.clip(hdr * 255, 0, 255).astype('uint8')

cv2.imshow('HDR Result', hdr_8bit)
cv2.waitKey(0)
```

Results:

- Exposures: ![Exposures](https://images/07-computational-photography/exposures.jpg)
- HDR Result: ![HDR Result](https://images/07-computational-photography/fusion_mertens.jpg)

# 30. Face Detection using Haar Cascades
Detecting faces in images.

```python
import cv2

# Load pre-trained classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('images/08-object-detection/face_detection.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

print(f"Detected {len(faces)} faces")
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
```
# 31. Optical Flow

Tracking motion between consecutive frames.

```python
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Parameters for ShiTomasi corner detection
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

# Parameters for Lucas-Kanade optical flow
lk_params = dict(winSize=(15, 15), maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Take first frame
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# Find initial corners
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# Create mask for drawing
mask = np.zeros_like(old_frame)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    
    # Select good points
    if p1 is not None:
        good_new = p1[st == 1]
        good_old = p0[st == 1]
        
        # Draw tracks
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), (0, 255, 0), 2)
            frame = cv2.circle(frame, (int(a), int(b)), 5, (0, 0, 255), -1)
        
        img = cv2.add(frame, mask)
        cv2.imshow('Optical Flow', img)
        
        # Update previous frame and points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

# 32. Background Subtraction

Detecting moving objects in video.

```python
import cv2

# Create background subtractor
back_sub = cv2.createBackgroundSubtractorMOG2()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Apply background subtraction
    fg_mask = back_sub.apply(frame)
    
    # Remove noise
    fg_mask = cv2.medianBlur(fg_mask, 5)
    
    # Find contours
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw bounding boxes around detected objects
    for contour in contours:
        if cv2.contourArea(contour) > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow('Original', frame)
    cv2.imshow('Foreground Mask', fg_mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```
## 33. K-Means Clustering for Color Quantization
Reducing the number of colors in an image.

```python
import cv2
import numpy as np

img = cv2.imread('images/06-machine-learning/kmeans/kmeans.jpg')
Z = img.reshape((-1, 3))
Z = np.float32(Z)

# Define criteria and apply k-means
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8  # Number of colors
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert back to uint8 and reshape
center = np.uint8(center)
res = center[label.flatten()]
quantized = res.reshape((img.shape))

cv2.imshow('Original', img)
cv2.imshow(f'Quantized ({K} colors)', quantized)
cv2.waitKey(0)
```

## 34. Template Matching with Multiple Matches
Finding all instances of a template.

```python
import cv2
import numpy as np

img = cv2.imread('images/03-image-processing/12-template-matching/template_ccoeff_1.jpg')
template = cv2.imread('images/03-image-processing/12-template-matching/template_ccoeff_1.jpg')
h, w = template.shape[:2]

# Match template
result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

# Set threshold
threshold = 0.8
locations = np.where(result >= threshold)

# Draw all matches
for pt in zip(*locations[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

cv2.imshow('Multiple Matches', img)
cv2.waitKey(0)
```

📚 **Part 3: Complete Code Examples**
Real-World Application: Document Scanner

```python
import cv2
import numpy as np

def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    dst = np.array([[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]], dtype="float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped

# Load image and find document
img = cv2.imread('images/02-core-operations/perspective.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 75, 200)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest_contour = max(contours, key=cv2.contourArea)

# Approximate polygon
peri = cv2.arcLength(largest_contour, True)
approx = cv2.approxPolyDP(largest_contour, 0.02 * peri, True)

if len(approx) == 4:
    scanned = four_point_transform(img, approx.reshape(4, 2))
    cv2.imshow('Original', img)
    cv2.imshow('Scanned', scanned)
    cv2.waitKey(0)
```
# Real-World Application: Object Tracking with Color

```python
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define range for blue color
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # Create mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) > 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, "Blue Object", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    
    cv2.imshow('Tracking', frame)
    cv2.imshow('Mask', mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## Part 4: Quick Reference Cards

### Morphological Operations Summary

| Operation   | Formula           | Use Case                             |
|-------------|-------------------|--------------------------------------|
| Erosion     | A ⊖ B             | Remove small white noise             |
| Dilation    | A ⊕ B             | Fill small holes                     |
| Opening     | (A ⊖ B) ⊕ B      | Remove noise, preserve structure     |
| Closing     | (A ⊕ B) ⊖ B      | Fill holes, connect objects          |
| Gradient    | (A ⊕ B) - (A ⊖ B)| Find object boundaries                |

### Common Thresholding Methods

| Method        | Formula                             | Best For                           |
|---------------|-------------------------------------|------------------------------------|
| Binary        | 255 if src > thresh else 0         | Simple separation                   |
| Binary Inv    | 0 if src > thresh else 255         | Dark objects on light background    |
| Trunc         | thresh if src > thresh else src    | Limiting pixel values               |
| Tozero        | src if src > thresh else 0         | Preserve bright objects             |
| Otsu         | Auto-calculated threshold           | Bimodal histograms                 |
| Adaptive      | Varies across image                 | Uneven lighting                     |
unknown = cv2.subtract(sure_bg, sure_fg)

# Marker labelling
_, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# Apply watershed
markers = cv2.watershed(img, markers)
img[markers == -1] = [255, 0, 0]
cv2.imshow('Segmented', img)
cv2.waitKey(0)
```

### Results:
- Coins: ![Coins](https://images/03-image-processing/15-watershed-segmentation/water_coins.jpg)
- Distance Transform: ![Distance Transform](https://images/03-image-processing/15-watershed-segmentation/water_dt.jpg)
- Watershed Result: ![Watershed Result](https://images/03-image-processing/15-watershed-segmentation/water_result.jpg)
# 📚 OpenCV Complete Tutorial Master Guide

## An Interactive Learning Journey with 100+ Visual Examples

---

# 🎯 Part 1: Core Operations (10 Essential Codes)

## 1. Image Blending

Combining two images with transparency using `cv2.addWeighted()`.

```python
import cv2

# Load images
img1 = cv2.imread('images/02-core-operations/blending.jpg')
img2 = cv2.imread('images/02-core-operations/affine.jpg')

# Resize to same dimensions
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Blend images (70% img1, 30% img2)
blended = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('Blended Result', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
Result:  
https://images/02-core-operations/blending.jpg

## 2. Image Transformation (Affine)

Linear mapping preserving points, lines, and parallelism.

```python
import cv2
import numpy as np

img = cv2.imread('images/02-core-operations/affine.jpg')
rows, cols = img.shape[:2]

# Source and destination points
pts_src = np.float32([[50, 50], [200, 50], [50, 200]])
pts_dst = np.float32([[10, 100], [200, 50], [100, 250]])

# Get and apply affine transformation
M = cv2.getAffineTransform(pts_src, pts_dst)
transformed = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Transformed', transformed)
cv2.waitKey(0)
```
Result:  
https://images/02-core-operations/affine.jpg

## 3. Image Rotation

Rotating an image around its center.

```python
import cv2

img = cv2.imread('images/02-core-operations/rotation.jpg')
rows, cols = img.shape[:2]

# Rotation matrix (center, angle, scale)
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Rotated 45°', rotated)
cv2.waitKey(0)
```
Result:  
https://images/02-core-operations/rotation.jpg

## 4. Image Thresholding

Converting grayscale to binary based on intensity.

```python
import cv2

img = cv2.imread('images/03-image-processing/03-image-thresholding/threshold.jpg', 0)

# Simple threshold
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Adaptive threshold
adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Otsu's threshold
_, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('Binary', binary)
cv2.imshow('Adaptive', adaptive)
cv2.imshow('Otsu', otsu)
cv2.waitKey(0)
```
Results:  
Binary: https://images/03-image-processing/03-image-thresholding/threshold.jpg  
Adaptive: https://images/03-image-processing/03-image-thresholding/ada_threshold.jpg  
Otsu: https://images/03-image-processing/03-image-thresholding/otsu.jpg  

## 5. Edge Detection (Canny)

Detecting edges using the Canny algorithm.

```python
import cv2

img = cv2.imread('images/03-image-processing/07-canny-edge-detection/canny1.jpg', 0)

# Apply Canny edge detection
edges = cv2.Canny(img, 100, 200)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
```
Result:  
https://images/03-image-processing/07-canny-edge-detection/canny1.jpg
  
# 6. Morphological Operations

Erosion, dilation, opening, and closing.

```python
import cv2
import numpy as np

img = cv2.imread('images/03-image-processing/05-morphological-transformations/gradient.png', 0)
kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.waitKey(0)
```

### Results:

- Erosion: [Link](https://images/03-image-processing/05-morphological-transformations/erosion.png)
- Dilation: [Link](https://images/03-image-processing/05-morphological-transformations/dilation.png)
- Opening: [Link](https://images/03-image-processing/05-morphological-transformations/opening.png)
- Closing: [Link](https://images/03-image-processing/05-morphological-transformations/closing.png)

# 7. Contour Detection

Finding and drawing contours in an image.

```python
import cv2

img = cv2.imread('images/03-image-processing/09-contours/contour.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find and draw contours
contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

cv2.imshow('Contours', img)
cv2.waitKey(0)
```

# 8. Face Detection

Detecting faces using Haar Cascade classifier.

```python
import cv2

# Load pre-trained classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread('images/08-object-detection/face_detection.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

print(f"Detected {len(faces)} faces")
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
```

# 9. Feature Matching (SIFT)

Matching features between two images.

```python
import cv2

img1 = cv2.imread('images/04-feature-detection/09-feature-matching/matcher_result1.jpg')
img2 = cv2.imread('images/04-feature-detection/09-feature-matching/matcher_result2.jpg')

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect and compute features
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Create FLANN matcher
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
flann = cv2.FlannBasedMatcher(index_params, {})

# Match features
matches = flann.knnMatch(des1, des2, k=2)

# Apply ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

# Draw matches
result = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None)

cv2.imshow('Feature Matches', result)
cv2.waitKey(0)
```

### Results:
![Feature Match 1](https://images/04-feature-detection/09-feature-matching/matcher_result1.jpg)
## Image Segmentation (GrabCut)

Interactive foreground extraction.

```python
import cv2
import numpy as np

img = cv2.imread('images/03-image-processing/16-grabcut-foreground-extraction/grabcut_output1.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

# GrabCut parameters
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)

# Define rectangle around object
rect = (50, 50, img.shape[1] - 50, img.shape[0] - 50)

# Apply GrabCut
cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

# Create mask (0=background, 1=foreground)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Apply mask to image
result = img * mask2[:, :, np.newaxis]

cv2.imshow('Extracted Object', result)
cv2.waitKey(0)
```

### Results:

| Mask | Rectangle | Output |
|------|-----------|--------|
| ![Mask](https://images/03-image-processing/16-grabcut-foreground-extraction/grabcut_mask.jpg) | ![Rectangle](https://images/03-image-processing/16-grabcut-foreground-extraction/grabcut_rect.jpg) | ![Output](https://images/03-image-processing/16-grabcut-foreground-extraction/grabcut_output1.jpg) |
