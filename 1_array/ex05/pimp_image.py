import numpy as np
import matplotlib.pyplot as plt


def ft_original(array):
    image = array
    plt.subplot(3, 2, 1)
    plt.imshow(image)
    plt.axis('off')
    plt.title("Figure VIII.1: Original", y=-0.1)


def ft_invert(array):
    """
    Inverts the color of the image received.
    """
    image = 255 - array
    plt.subplot(3, 2, 2)
    plt.imshow(image)
    plt.axis('off')
    plt.title("Figure VIII.2: Invert", y=-0.1)


def ft_red(array):
    """
    Keeps only the red channel of the image received.
    """
    red_channel = array[:, :, 0]
    image = array.copy()
    image[:, :, 0] = red_channel
    image[:, :, 1] = 0
    image[:, :, 2] = 0
    plt.subplot(3, 2, 3)
    plt.imshow(image)
    plt.axis('off')
    plt.title("Figure VIII.3: Red", y=-0.1)


def ft_green(array):
    """
    Keeps only the green channel of the image received.
    """
    green_channel = array[:, :, 1]
    image = array.copy()
    image[:, :, 0] = 0
    image[:, :, 1] = green_channel
    image[:, :, 2] = 0
    plt.subplot(3, 2, 4)
    plt.imshow(image)
    plt.axis('off')
    plt.title("Figure VIII.4: Green", y=-0.1)


def ft_blue(array):
    """
    Keeps only the blue channel of the image received.
    """
    blue_channel = array[:, :, 2]
    image = array.copy()
    image[:, :, 0] = 0
    image[:, :, 1] = 0
    image[:, :, 2] = blue_channel
    plt.subplot(3, 2, 5)
    plt.imshow(image)
    plt.axis('off')
    plt.title("Figure VIII.5: Blue", y=-0.1)


def ft_grey(array):
    """
    Converts the image received to grayscale.
    """
    px_mean = np.mean(array, axis=2)
    image = px_mean
    plt.subplot(3, 2, 6)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.title("Figure VIII.6: Grey", y=-0.1)
    plt.show()
