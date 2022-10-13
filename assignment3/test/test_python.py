from instapy.python_filters import python_color2gray, python_color2sepia
from numpy import random

def test_color2gray(image):
    # run color2gray
    gray_image = python_color2gray(image)

    # check that the result has the right shape, type
    assert image.shape[0] == gray_image.shape[0]
    assert image.shape[1] == gray_image.shape[1]
    assert image.dtype == gray_image.dtype

    # assert uniform r,g,b values
    for i in range(10):
        x = random.randint(image.shape[0])
        y = random.randint(image.shape[1])
        pixel_value = int(image[x][y][0]*0.21 + image[x][y][1]*0.72 + image[x][y][2]*0.07)
        assert gray_image[x][y][0] == pixel_value
        assert gray_image[x][y][1] == pixel_value
        assert gray_image[x][y][2] == pixel_value


def test_color2sepia(image):
    # run color2sepia
    sepia_image = python_color2sepia(image)

    # check that the result has the right shape, type
    assert image.shape[0] == sepia_image.shape[0]
    assert image.shape[1] == sepia_image.shape[1]
    assert image.dtype == sepia_image.dtype

    sepia_matrix = [
    [ 0.393, 0.769, 0.189],
    [ 0.349, 0.686, 0.168],
    [ 0.272, 0.534, 0.131],
    ]

    # verify some individual pixel samples
    # according to the sepia matrix
    for i in range(10):
        x = random.randint(image.shape[0])
        y = random.randint(image.shape[1])

        red, green, blue = image[x][y][0], image[x][y][1], image[x][y][2]

        tr = sepia_matrix[0][0]*red + sepia_matrix[0][1]*green + sepia_matrix[0][2]*blue 
        tg = sepia_matrix[1][0]*red + sepia_matrix[1][1]*green + sepia_matrix[1][2]*blue 
        tb = sepia_matrix[2][0]*red + sepia_matrix[2][1]*green + sepia_matrix[2][2]*blue
        if tr > 255:
            tr = 255 
        if tg > 255:
            tg = 255
        if tb > 255:
            tb = 255

        assert sepia_image[x][y][0] == int(tr)
        assert sepia_image[x][y][1] == int(tg)
        assert sepia_image[x][y][2] == int(tb)
    
