from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    try:
        cut_img = ft_load("animal.jpeg")
        print(cut_img)

        transposed_img = np.array([list(row) for row in zip(*cut_img)])
        print(f"New shape after Transpose: {transposed_img.shape[:2]}")
        print(transposed_img)
        
        plt.imshow(transposed_img, cmap='gray')
        plt.show()

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()