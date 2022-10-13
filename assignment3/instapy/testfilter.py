import time
from . import io, python_filters, numpy_filters, numba_filters



image = io.read_image("test/rain.jpg")
start = time.time()
# sepia_image = numba_filters.numba_color2sepia(image)
gray_image = numpy_filters.numpy_color2gray(image)
slutt = time.time()
print(slutt-start)
# sepia_image2 = python_filters.python_color2sepia(image)
io.display(gray_image)
# io.display(sepia_image2)
