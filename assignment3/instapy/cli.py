"""Command-line (script) interface to instapy"""

import argparse
import sys

import numpy as np
from PIL import Image

import instapy
from . import io, get_filter


def run_filter(
    file: str,
    out_file: str = None,
    implementation: str = "python",
    filter: str = "color2gray",
    scale: int = 1,
    sepia_alpha: float = 1
) -> None:
    """Run the selected filter"""
    # load the image from a file
    
    image = Image.open(file)
    
    if int(scale) != 1:
        # Resize image, if needed
        image = image.resize((image.width // int(scale), image.height // int(scale)))
    
    image = np.asarray(image)
    sepia_alpha
    # Apply the filter
    if filter == "gray":
        filter = "color2gray"
    elif filter == "sepia":
        filter = "color2sepia"
    else:
        filter = "color2gray"

    filt = get_filter(filter, implementation)

    if implementation == "numpy":
        filtered = filt(image, float(sepia_alpha))
    else:
        filtered = filt(image)

    if out_file:
        # save the file
        io.write_image(filtered)
    else:
        # not asked to save, display it instead
        io.display(filtered)


def main(argv=None):
    """Parse the command-line and call run_filter with the arguments"""
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser()

    # filename is positional and required
    parser.add_argument("file", help="The filename to apply filter to")
    parser.add_argument("-o", "--out", help="The output filename")
    

    # Add required arguments
    # parser.add_argument("-g", "--gray",action="store_const", const = "color2gray", help="Select gray filter")
    # parser.add_argument("-se", "--sepia", action="store_const", const = "color2sepia", help="Select sepia filter")
    parser.add_argument("-f", "--filter", choices=["gray", "sepia"],default="color2gray" ,help="The filter to be added to the image")
    parser.add_argument("-sc", "--scale", default=1 ,help="Scale factor to resize image")
    parser.add_argument("-i", "--implementation",choices=["python","numpy","numba"],default="numpy" ,help="The implementation")
    parser.add_argument("-k", default=1 ,help="Determines aplha value for sepia filter")

    # parse arguments and call run_filter
    args = parser.parse_args()

    run_filter(args.file, args.out, args.implementation, args.filter, args.scale, args.k)
