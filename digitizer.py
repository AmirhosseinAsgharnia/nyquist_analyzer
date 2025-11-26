import cv2 as cv
import argparse

def main():
    parser = argparse.ArgumentParser(description="Digitizer program.")
    parser.add_argument("-i", "--image", default="image.jpg", help="Please enter the image name after -i: python /digitizer -i image_name.jpg")
    args = parser.parse_args()

    image_path = args.image
    image = cv.imread(image_path)

    if image is None:
        print("There is no input image")
        return 0

    cv.imshow("Image", image)
    cv.waitKey()

if __name__ == "__main__":
    main()
