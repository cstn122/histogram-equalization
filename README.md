# Histogram Equalization (by theory)

Input a bad image and make it better.

**Prerequisite: cv2, matplotlib.pyplot, numpy

1. Generate the histogram of the original image.
![Original Histogram](https://imgur.com/8utpRWm.png)

2. Calculate its PDF (probability density function) by dividing the histogram array by the sum of the image's pixels.
![PDF](https://imgur.com/ReCr6iA.png)

3. Calculate its CDF (cumulative distribution function) by integrating PDF.
![CDF](https://imgur.com/y6HZY3c.png)

4. Multiply CDF by 255, the max value of a grayscale image.

5. Generate the equalized histogram by merging 1 and 4. </br>
*(We can also compare the equalized result with the one using cv2.equalizeHist().)*
![Comparing Histograms](https://imgur.com/Q1WH2hn.png)
![Comparing Images](https://imgur.com/JGZUvxu.png)
