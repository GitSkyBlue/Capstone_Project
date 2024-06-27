import cv2

cap = cv2.VideoCapture(1)
c = 0
f = None
while True:
    c += 1
    ret, frame = cap.read()

    cv2.imshow('', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if c == 15:
        f = frame
        break

cap.release()
cv2.destroyAllWindows()

cv2.imshow('', f)
cv2.waitKey(0)
cv2.destroyAllWindows()
