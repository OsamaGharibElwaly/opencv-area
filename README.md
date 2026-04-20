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
