import cv2


def emptyfunction():
    pass

def main():

    imgpath1 = "Windows-10-Wallpapers-02-1920-x-1080.jpg"
    imgpath2 = "Astronaut-Mood-Earth-Planets-Mask-1920-x-1080-1.jpg"


    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)

    windowname = "Output"
    cv2.namedWindow(windowname)

    output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

    cv2.createTrackbar('Alpha', windowname, 0, 10, emptyfunction)

    while(True):
        cv2.imshow(windowname, output)

        if cv2.waitKey(1) == 27:
            break

        alpha = cv2.getTrackbarPos('Alpha', windowname)/10
        beta = 1-alpha

        output= cv2.addWeighted(img1, alpha, img2, beta, 0)

        print(alpha, beta)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()