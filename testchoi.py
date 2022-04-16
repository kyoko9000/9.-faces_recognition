import face_recognition
from tkinter.filedialog import askopenfilename
import cv2
from tkinter import Tk
Tk().withdraw()
import os

#tạo danh sách tên
def encode_names():
   list_names = []
   folder_link = ('images/')
   for filename in os.listdir(folder_link):
      list_names.append(filename)
   return list_names

# tạo danh sách các khuôn mặt trong thư viện đã encoding
def encode_faces():
   list_people_encoding = []
   folder_link = ('images/')
   for filename in os.listdir(folder_link):
      know_image = face_recognition.load_image_file(f'{folder_link}{filename}')
      know_encoding = face_recognition.face_encodings(know_image)[0]
      list_people_encoding.append(know_encoding)
   return list_people_encoding

# tập hợp danh sách khuôn mặt và tên của hình ảnh trong thư viện
known_faces_encodings = encode_faces()
known_faces_names = encode_names()
print(known_faces_names)

# lấy thông tin của hình ảnh bất kỳ cần xác nhận
load_image = askopenfilename()
target_faces = face_recognition.load_image_file(load_image)
target_face_locations = face_recognition.face_locations(target_faces)
target_face_encodings = face_recognition.face_encodings(target_faces)

# so sánh
for (top,right,bottom,left),target_face_encoding in zip(target_face_locations,target_face_encodings):
    matches = face_recognition.compare_faces(known_faces_encodings, target_face_encoding, tolerance=0.55)

    name = 'unknow'
    if True in matches:
        match_index = matches.index(True)
        name = known_faces_names[match_index]

    # vẽ ra ô vuông lên khuôn mặt người được xác nhận
    cv2.rectangle(target_faces, (left, top), (right, bottom), (255, 0, 0), 3)
    cv2.rectangle(target_faces, (left, bottom + 30), (right, bottom), (255, 0, 0), cv2.FILLED)
    cv2.putText(target_faces, name, (left + 3, bottom + 25), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)

# chiếu hình ảnh lên
def render_image():
   RGB_image = cv2.cvtColor(target_faces, cv2.COLOR_BGR2RGB)
   cv2.imshow('face_recognition', RGB_image)
   cv2.waitKey(0)
render_image()