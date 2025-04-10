import os
import cv2
import json
import getpass
import face_recognition

# Constants
DATASET_PATH = "dataset"
USERS_FILE = "users.json"
ENCODINGS_FILE = "encodings.json"

# Make sure dataset directory exists
if not os.path.exists(DATASET_PATH):
    os.makedirs(DATASET_PATH)

# Load users
if os.path.exists(USERS_FILE):
    with open(USERS_FILE, "r") as f:
        users = json.load(f)
else:
    users = {}

# Load face encodings
if os.path.exists(ENCODINGS_FILE):
    with open(ENCODINGS_FILE, "r") as f:
        encodings = json.load(f)
else:
    encodings = {}

username = input("Enter a new username: ")
if username in users:
    print("Username already exists!")
    exit()

password = getpass.getpass("Enter password (hidden): ")
users[username] = password

print("Capturing face... Please look at the camera.")
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

if not ret:
    print("Failed to access webcam.")
    exit()

# Save face image
img_path = os.path.join(DATASET_PATH, f"{username}.jpg")
cv2.imwrite(img_path, frame)

# Encode face
face_img = face_recognition.load_image_file(img_path)
face_enc = face_recognition.face_encodings(face_img)

if not face_enc:
    print("Face not detected. Please try again.")
    os.remove(img_path)
    exit()

encodings[username] = face_enc[0].tolist()

# Save to files
with open(USERS_FILE, "w") as f:
    json.dump(users, f)

with open(ENCODINGS_FILE, "w") as f:
    json.dump(encodings, f)

print("User registered successfully!")




