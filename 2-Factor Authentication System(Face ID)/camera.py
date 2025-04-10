import cv2

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_face.jpg", frame)
    cap.release()
    return "captured_face.jpg"



