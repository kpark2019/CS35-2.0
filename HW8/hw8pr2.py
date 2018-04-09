# ## Problem 2:  green-screening!
# 
# This question asks you to write one function that takes in two images:
#  + orig_image  (the green-screened image)
#  + new_bg_image (the new background image)
#  
# It also takes in a 2-tuple (corner = (0,0)) to indicate where to place the upper-left
#   corner of orig_image relative to new_bg_image
#
# The challenge is to overlay the images -- but only the non-green pixels of
#   orig_image...
#

#
# Again, you'll want to borrow from hw7pr1 for
#  + opening the files
#  + reading the pixels
#  + create some helper functions
#    + defining whether a pixel is green is the key helper function to write!
#  + then, creating an output image (start with a copy of new_bg_image!)
#
# Happy green-screening, everyone! Include at least TWO examples of a background!
#
from colour import Color
import numpy as np
from matplotlib import pyplot as plt
import cv2

# Here is a signature for the green-screening...
# remember - you will want helper functions!
def green_screen2( orig_image, new_bg_image, corner=(0,0) ):
    """ be sure to include a better docstring here! """
    green = whatsgreen2(orig_image)
    together = (orig_image - green) + (new_bg_image - green.invert())
    return together

def whatsgreen2(image):
    """Instead of using RGB, after some research, trial and error, we found
    that using hue and saturation was much more efficient and more effective
    in discerning grrenscreen. So we used IMage's method hueDistance()
    to figure out the differences in green and pick up most variations and
    shades of green."""
    green = image.hueDistance(color= Color('green'), minvalue=40).binarize()
    return green

def green_screen( orig_image, new_bg_image, corner=(0,0) ):
    """In order to properly greenscreen, I am going to
    + Determine what range of rgb values defines green using a helper function and then change all greens to one shade
    + Then taking that new picture, we will replace each pixel with the corresponding pixel
    + Then we will again replace pixels, but this time from the background but only if the background
    is larger than the original picture"""

    #
    # First let's create a universal height and figure out what the length
    # should be for the smaller picture
    #
    bg_height = new_bg_image.shape[0]
    og_height = orig_image.shape[0]
    bg_length = new_bg_image.shape[1]
    og_length = orig_image.shape[1]
    if bg_height > og_height:
        new_height = bg_height
        new_length1 = (new_height / orig_image.shape[0]) * orig_image.shape[1]
        new_length1 = int(new_length1)
    else:
        new_height = og_height
        new_length1 = (new_height / new_bg_image.shape[0]) * new_bg_image.shape[1]
        new_length1 = int(new_length1)

    #
    # Then let's resize the images accordingly
    #
    if bg_height > og_height:
        orig_image = cv2.resize(orig_image, dsize=(new_length1, new_height), interpolation=cv2.INTER_LINEAR)
    else:
        new_bg_image = cv2.resize(new_bg_image, dsize=(new_length1, new_height), interpolation=cv2.INTER_LINEAR)

    #
    # Let's employ the helper function whatsgreen() to get a new one green image
    # Then with that image let's replace the green pixels with the corresponding pixel from
    #   the background image
    #
    green = whatsgreen(orig_image)
    num_rows, num_cols, num_chans = green.shape
    final = green.copy()
    for row in range(num_rows):
        for col in range(num_cols):
            r, g, b = green[row, col]
            print(row, col)
            if r == 0 and g == 255 and b == 0:
                final[row, col] = new_bg_image[row, col]

    #
    #
    #
    if bg_length > og_length:
        final_final = new_bg_image.copy()
    else:
        final_final = orig_image.copy()

    num_rows, num_cols, num_chans = final.shape
    print(num_rows, num_cols)
    for row in range(num_rows):
        for col in range(num_cols):
            final_final[row, col] = final[row, col]
    return final_final

def whatsgreen(image):
    new_image = image.copy()
    num_rows, num_cols, num_chans = new_image.shape
    print(num_rows, num_cols)
    for row in range(num_rows):
        for col in range(num_cols):
            r, g, b = image[row, col]

            print(row, col)
            print(r, g, b)
            if r < 125 and g > 185 and b < 190:
                new_image[row, col] = [0, 255, 0]
                print("GREEEEEEEN")

    plt.imshow(new_image)


    return new_image



green_image = cv2.imread('Kenny.JPG',cv2.IMREAD_COLOR)
back_image = cv2.imread('dodds.jpg',cv2.IMREAD_COLOR)
new_image = green_screen( green_image, back_image )
plt.imshow(new_image)
plt.show()


# Comment and reflection    You should include a short triple-quoted comment
# at the bottom of hw7pr3.py that reflects on how you implemented your green_screen function.
# In addition, you should include at least two examples, named
# green_screen1.png
# green_screen2.png
# -- using your own images -- of the green-screening in action!

""" Unfortunately, our greenscreen didn't work as well. Although we were able to fine-tune
 the ranges for our definition of 'green', for some reason there were a couple bugs.
 For one, some of the colors in the originial picture changed as well. We're not quite
 sure why, but we believe that in finding green values, some of the other pixels also changed.
 Other than that, however, we were able to get most of our picture in and even
 did a bit of resizing."""
