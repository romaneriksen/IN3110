"""numpy implementation of image filters"""

from typing import Optional
import numpy as np


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    r,g,b = 0.21, 0.72, 0.07
    N,M,O = image.shape
    gray_image = np.empty_like(image)

    # Hint: use numpy slicing in order to have fast vectorized code
    # Updates each value for the RGB tuple to the same gray value
    gray_image[:,:,0] = image[:, :, 0]*r + image[:, :, 1]*g + image[:, :, 2]*b
    gray_image[:,:,1] = image[:, :, 0]*r + image[:, :, 1]*g + image[:, :, 2]*b
    gray_image[:,:,2] = image[:, :, 0]*r + image[:, :, 1]*g + image[:, :, 2]*b

    gray_image = gray_image.astype("uint8")
    return gray_image


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
    you may ignore it for Task 9)

    Returns:
        np.array: sepia_image
    """
    
    sepia_matrix = [
        [ 0.393**k, 0.769*k, 0.189*k],
        [ 0.349*k, 0.686**k, 0.168*k],
        [ 0.272*k, 0.534*k, 0.131**k],
        ] 

    # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    # if not 0 <= k <= 1:
    #     raise ValueError(f"k must be between [0-1], got {k=}")

    sepia_image = np.empty_like(image)

    N,M,O = image.shape

    # Exctracting each of the RGB images
    red_image = image[:, :, 0]
    green_image = image[:, :, 1]
    blue_image = image[:, :, 2]
    
    # Apply the matrix filter
    # Computing the values for each of the RGB images, tr is the value for the transformed red image
    tr = sepia_matrix[0][0]*red_image + sepia_matrix[0][1]*green_image + sepia_matrix[0][2]*blue_image 
    tg = sepia_matrix[1][0]*red_image + sepia_matrix[1][1]*green_image + sepia_matrix[1][2]*blue_image 
    tb = sepia_matrix[2][0]*red_image + sepia_matrix[2][1]*green_image + sepia_matrix[2][2]*blue_image 

    # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    tr[tr > 255]=255
    tg[tg > 255]=255
    tb[tb > 255]=255

    # Creating the full sepia image
    sepia_image[:, :, 0] = tr
    sepia_image[:, :, 1] = tg
    sepia_image[:, :, 2] = tb


    sepia_image = sepia_image.astype("uint8")
    # Return image (make sure it's the right type!)
    return sepia_image
