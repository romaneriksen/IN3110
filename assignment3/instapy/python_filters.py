"""pure Python implementation of image filters"""

import numpy as np


def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    N,M,O = image.shape
    # iterate through the pixels, and apply the grayscale transform
    for i in range(N):
        for j in range(M):
            # Exctracting the current RGB values and computing the resulting gray value
            sum = image[i][j][0]*0.21 + image[i][j][1]*0.72 + image[i][j][2]*0.07
            # Setting the gray value
            gray_image[i][j][0] = sum
            gray_image[i][j][1] = sum
            gray_image[i][j][2] = sum

    gray_image = gray_image.astype("uint8")
    
    return gray_image



def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
        ] 

    sepia_image = np.empty_like(image)
    # Iterate through the pixels
    N,M,O = image.shape
    for i in range(N):
        for j in range(M):
            # Applying the sepia matrix

            # Extracting current RGB values
            red, green, blue = image[i][j][0], image[i][j][1], image[i][j][2]

            # Computing the RGB values for the sepia image
            tr = sepia_matrix[0][0]*red + sepia_matrix[0][1]*green + sepia_matrix[0][2]*blue 
            tg = sepia_matrix[1][0]*red + sepia_matrix[1][1]*green + sepia_matrix[1][2]*blue 
            tb = sepia_matrix[2][0]*red + sepia_matrix[2][1]*green + sepia_matrix[2][2]*blue

            # Setting the maximum value for the RGB values for the sepia image
            if tr > 255:
                tr = 255 
            if tg > 255:
                tg = 255
            if tb > 255:
                tb = 255
            
            # Setting the RGB Values for the sepia image
            sepia_image[i][j][0] = tr
            sepia_image[i][j][1] = tg
            sepia_image[i][j][2] = tb

    # applying the sepia matrix

    # Return image
    sepia_image = sepia_image.astype("uint8")
    
    return sepia_image
