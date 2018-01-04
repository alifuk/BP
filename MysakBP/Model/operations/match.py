import cv2

def template():
    import cv2
    import numpy as np

    img_rgb = cv2.imread('bozkov_source.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('bozkov_pattern.jpg', 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_SQDIFF_NORMED)
    threshold = 0.4
    loc = np.where(res <= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    cv2.imwrite('res.png', img_rgb)