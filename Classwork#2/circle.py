import cv2

def circle_edge_detection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    wide = cv2.Canny(blurred, 200, 255)
    w, h, _ = image.shape
    for x in range(0,h,3):
        for y in range(0,w,3):
            edge = wide[y,x]
            
            if edge >= 255:
                cv2.circle(image, (x, y), 60, (0, 255, 0), 1)

    cv2.imwrite("output.png", image)
    cv2.imshow('detected',wide)
    cv2.imshow('detected circles',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = "Circle Objects.png"
img = cv2.imread(image_path)
circle_edge_detection(img)