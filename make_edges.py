from skimage import io, filters, feature
import os
import numpy as np
import sys

image_path = raw_input("Path to image: ")

#try:
test_image = io.imread(image_path, flatten=True)
#except:
    #print('Cannot open "%s"') % image_path
    #sys.exit()

path, filename = os.path.split(image_path)

# Sobel edges
sobel_edges = filters.sobel(test_image)
io.imsave(path + '/sobel_' + filename, sobel_edges)

# Canny edges
canny_edges = feature.canny(test_image, sigma = 1)
canny_out = np.uint8(canny_edges * 255) # convert from array of boolean values
io.imsave(path + '/canny_' + filename, canny_out)

