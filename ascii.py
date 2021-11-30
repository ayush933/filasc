import cv2
import imutils


def img2ascii(img) -> str:
    # Todo:Implement using luminosity
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    chars.reverse()
    new_w = 110
    n_img = imutils.resize(img, width=new_w)
    s = ""
    for i in n_img:
        for j in i:
            # print(chars[j // 25] * 2, end="")
            s += chars[j // 25] * 2
        # print()
        s += "\n"
    return s
