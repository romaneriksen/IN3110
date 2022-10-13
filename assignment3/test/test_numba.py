from instapy.numba_filters import numba_color2gray, numba_color2sepia

import numpy.testing as nt


def test_color2gray(image, reference_gray):

    gray_image = numba_color2gray(image)
    nt.assert_allclose(gray_image, reference_gray)
    assert gray_image.dtype == reference_gray.dtype
    ...


def test_color2sepia(image, reference_sepia):

    gray_image = numba_color2sepia(image)
    nt.assert_allclose(gray_image, reference_sepia)
    assert gray_image.dtype == reference_sepia.dtype
    ...
