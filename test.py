import face_recognition as fr
import cv2
from tkinter import Tk

from tkinter.filedialog import askopenfilename
import os
Tk().withdraw()


load_image = askopenfilename()
target_image = fr.load_image_file(load_image)
target_encoding = fr.face_encodings(target_image)
def encode_faces():
    list_people_encoding = []
    folder_link = ('images/')
    for filename in os.listdir(folder_link):
        know_image = fr.load_image_file(f'{folder_link}{filename}')
        know_encoding = fr.face_encodings(know_image)[0]
        list_people_encoding.append((know_encoding,filename))
    return list_people_encoding

def find_target_face():
    face_location = fr.face_locations(target_image)
    for person in encode_faces():
        filename = person[1]
        is_target_face = fr.compare_faces(person[0],target_encoding,tolerance=0.55)
        # print(f'{is_target_face}{filename}')
        face_number = 0
        lable = filename
        print(lable)
        for location in face_location:
            if is_target_face[face_number]:
                create_frame(location, lable)
            face_number += 1

def create_frame(location,lable):
    top,right,bottom,left = location
    cv2.rectangle(target_image, (left, top), (right, bottom), (255, 0, 0), 3)
    cv2.rectangle(target_image, (left, bottom + 20), (right, bottom), (255, 0, 0), cv2.FILLED)
    cv2.putText(target_image,lable,(left + 3, bottom + 14), cv2.FONT_HERSHEY_DUPLEX,0.4,(255,255,255),1)

def render_image():
    arb_ima = cv2.cvtColor(target_image,cv2.COLOR_BGR2RGB)
    cv2.imshow('face_recognition', arb_ima)
    cv2.waitKey(0)

find_target_face()
render_image()







