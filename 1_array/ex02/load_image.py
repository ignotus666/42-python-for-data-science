import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its format/shape,
    and returns its RGB pixel content as a numpy array.
    """
    try:
        img = Image.open(path)
        img_rgb = img.convert("RGB")
        res_array = np.array(img_rgb)

        print(f"The shape of image is: {res_array.shape}")
        print(res_array)

        return res_array

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None
