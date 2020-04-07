import cv2
import numpy as np

def question1(img):
    #BGR -> RGB
    blue = img[:,:,0].copy()
    green = img[:,:,1].copy()
    red = img[:,:,2].copy()

    img[:,:,0] = red
    img[:,:,1] = green
    img[:,:,2] = blue
    return img

def question2(img):
    #BGR->grayscale
    #flot64では表示ができないよってuint8に変換する
    blue = img[:,:,0].copy()
    green = img[:,:,1].copy()
    red = img[:,:,2].copy()
    #Y = 0.2126 R + 0.7152 G + 0.0722 B
    img = 0.2126 *red + 0.7152 *green + 0.0722 *blue
    print(img.dtype)
    img = img.astype(np.uint8)
    print(img.dtype)

    return img

def question3(img):
    #BGR
    blue = img[:,:,0].copy()
    green = img[:,:,1].copy()
    red = img[:,:,2].copy()
    #Y = 0.2126 R + 0.7152 G + 0.0722 B
    img = 0.2126 *red + 0.7152 *green + 0.0722 *blue
    img = img.astype(np.uint8)
    #print(img[img < 128])
    img[img < 128] = 0
    #print(img[img >= 128])
    img[img >= 128] = 255
    img = img.astype(np.uint8)
    return img

if __name__ == "__main__":
    img = cv2.imread("imori.jpg")
    cv2.imshow("Original",img)
    result = question3(img)
    cv2.imshow("result",result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()