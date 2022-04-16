import face_recognition
from tkinter.filedialog import askopenfilename
import cv2
from tkinter import Tk
Tk().withdraw()

kyoko_image = face_recognition.load_image_file("images/kyoko.jpg")
kyoko_face_encoding = face_recognition.face_encodings(kyoko_image)[0]

selena_image = face_recognition.load_image_file("images/selena.jpg")
selena_face_encoding = face_recognition.face_encodings(selena_image)[0]

taylor_image = face_recognition.load_image_file("images/taylor.jpg")
taylor_face_encoding = face_recognition.face_encodings(taylor_image)[0]

known_faces_encodings = [kyoko_face_encoding,selena_face_encoding,taylor_face_encoding]
known_faces_names = ['kyoko','selena','taylor']

load_image = askopenfilename()
target_faces = face_recognition.load_image_file(load_image)
target_face_locations = face_recognition.face_locations(target_faces)
target_face_encodings = face_recognition.face_encodings(target_faces)

for (top,right,bottom,left),target_face_encoding in zip(target_face_locations,target_face_encodings):
    matches = face_recognition.compare_faces(known_faces_encodings, target_face_encoding, tolerance=0.55)
    print(matches)
    name = 'unknow'
    if True in matches:
        match_index = matches.index(True)
        name = known_faces_names[match_index]
        print(match_index)
    cv2.rectangle(target_faces, (left, top), (right, bottom), (255, 0, 0), 3)
    cv2.rectangle(target_faces, (left, bottom + 30), (right, bottom), (255, 0, 0), cv2.FILLED)
    cv2.putText(target_faces, name, (left + 3, bottom + 25), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)
# def render_image():
RGB_image = cv2.cvtColor(target_faces, cv2.COLOR_BGR2RGB)
cv2.imshow('face_recognition', RGB_image)
cv2.waitKey(0)
# render_image()