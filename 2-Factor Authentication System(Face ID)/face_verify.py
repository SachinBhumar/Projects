import os
import cv2
import json
import face_recognition

ENCODINGS_FILE = "encodings.json"

def verify_face(username):
    if not os.path.exists(ENCODINGS_FILE):
        return False

    with open(ENCODINGS_FILE, "r") as f:
        encodings = json.load(f)

    if username not in encodings:
        return False

    known_encoding = encodings[username]

    print("Verifying... Look at the camera.")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Failed to access webcam.")
        return False

    face_img = face_recognition.face_encodings(frame)
    if not face_img:
        print("No face detected.")
        return False

    match = face_recognition.compare_faces([known_encoding], face_img[0])
    return match[0]







