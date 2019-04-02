import cv2

def main():

    windowname = "live video recording"
    cv2.namedWindow(windowname)

    cap = cv2.VideoCapture(0)

    filename = "R:\output.avi"
    codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    framerate = 20
    resolution = (640, 480)

    Videofileoutput = cv2.VideoWriter(filename, codec, framerate, resolution)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while(ret):
        ret, frame = cap.read()

        Videofileoutput.write(frame)


        cv2.imshow(windowname, frame)
        if cv2.waitKey(1)==27 :
            break

    cv2.destroyAllWindows()
    Videofileoutput.release()
    cap.release()


if __name__ == '__main__':
    main()