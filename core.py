import cv2
import imgdraw
import ascii
import os


def start_filter(filter: str = "ascii"):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print("Faulty Camera")
        exit(0)

    if filter == "ascii":
        while 1:
            ret, frame = cap.read()
            if not ret:
                print("Cant receive from stream")
                break
            frame = cv2.flip(frame, 1)
            s = ascii.img2ascii(frame)
            imgdraw.draw(s)
            img = cv2.imread("temp.jpg")
            cv2.imshow("filasc", img)
            if cv2.waitKey(1) == ord('q'):
                break

        if os.path.exists("temp.jpg"):
            os.remove("temp.jpg")
    cap.release()
    cv2.destroyAllWindows()