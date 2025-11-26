import cv2 as cv
import argparse

def main():
    parser = argparse.ArgumentParser(description="Digitizer program.")
    parser.add_argument("-i", default="image.jpg", help="Please enter the image name after -i: python /digitizer -i image_name.jpg")
    args = parser.parse_args()

if __name__ == "__main__":
    main()
