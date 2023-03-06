import cv2

img_counter = 0

cap = cv2.VideoCapture(0)
if not (cap.isOpened()):
    print ("Coudl not open video device")

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) %256 == 27:
        break

    elif cv2.waitKey(1) %256 == 32:
        img_name = 'opencv_frame_{}.png'.format(img_counter)
        cv2.imwrite(img_name, frame)
        print('{}a fost facuta!'.format(img_name))
        img_counter += 1

cap.release()

cv2.destroyAllWindows()