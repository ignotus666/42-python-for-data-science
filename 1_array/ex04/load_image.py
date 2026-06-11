import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its format/shape,
    and returns its RGB pixel content as a numpy array.
    """
    try:
        assert isinstance(path, str) and len(path.strip()) > 0, \
            "Path must be a valid string."
        assert path.lower().endswith(('.jpg', '.jpeg', '.png')), \
            "Unsupported format."

        img = Image.open(path)
        img_rgb = img.convert("RGB")
        res_array = np.array(img_rgb)

        cut_img = res_array[20:520, 440:940, :1]
        print(f"The shape of the image is: {cut_img.shape} "
              f"or {cut_img.shape[:2]}")

        return cut_img

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Exception: {e}")
