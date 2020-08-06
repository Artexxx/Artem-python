""" Для обнаружения пидоров переместите их фото в директорию /pidor"""
import os
import cv2
import numpy as np
import face_recognition as fr

face = []
encode = []
known_faces = []
names = []
x = 0

for filename in os.listdir("pidor"):
    if filename.endswith(".jpg"):
        face.append(fr.load_image_file(os.path.join("pidor", filename)))
        encode.append(fr.face_encodings(face[x])[0])
        known_faces.append(encode[x])
        names.append(filename.replace(".jpg", ""))
        print(filename)
        x = x + 1

camera = cv2.VideoCapture(0)

while True:
    ret, img = camera.read()

    rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    locations = fr.face_locations(rgbImg)
    encodings = fr.face_encodings(rgbImg, locations)

    name = "unknown!"
    for encoding in encodings:
        matches = fr.compare_faces(known_faces, encoding)
        name = "unknown!"

        face_distances = fr.face_distance(known_faces, encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = names[best_match_index]
        print("Podor detected. " + name)

    if name != "unknown!":
        for (top, right, bottom, left) in locations:
            cv2.putText(img, "pidor detected!!!", (left - 70, top - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
            cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

    cv2.imshow('search system', img)

    if cv2.waitKey(10) == 27:  # press `ESC`
        break

camera.release()
cv2.destroyAllWindows()
