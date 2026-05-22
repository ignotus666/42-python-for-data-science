from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    try:
        starting_img = ft_load("animal.jpeg")
        print(starting_img)

        zoomed_img = starting_img[40:490, 440:940, :1]
        print(f"New shape after slicing: {zoomed_img.shape} "
              f"or {zoomed_img.shape[:2]}")

        plt.imshow(zoomed_img, cmap='gray')
        plt.show()

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    main()