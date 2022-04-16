#no need to install anything
import sys
# pip install pyqt5, pip install pyqt5 tools
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtGui
# just change the name
from Screen_9 import Ui_MainWindow
import face_recognition
from tkinter.filedialog import askopenfilename
import cv2
from tkinter import Tk
Tk().withdraw()
import os

class MainWindow:
    def __init__(self):
        # the way app working
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.Button_start.clicked.connect(self.detecpic)
        self.uic.Button_stop.clicked.connect(self.main_win.close)

    def detecpic(self):
        # tạo danh sách tên trong thu vien
        def encode_names():
            list_names = []
            folder_link = ('images/')
            for filename in os.listdir(folder_link):
                list_names.append(filename)
            return list_names

        # danh sach khuon mat cua nhung nguoi trong thu vien
        def encode_faces():
            list_people_encoding = []
            folder_link = ('images/')
            for filename in os.listdir(folder_link):
                known_image = face_recognition.load_image_file(f'{folder_link}{filename}')
                known_encoding = face_recognition.face_encodings(known_image)[0]
                list_people_encoding.append(known_encoding)
            return list_people_encoding

        # tong hop lai danh sach
        known_faces_encodings = encode_faces()
        known_faces_names = encode_names()
        print(known_faces_names)

        # load bat ky hinh anh nao len de xac nhan
        load_image = askopenfilename()
        target_faces = face_recognition.load_image_file(load_image)
        target_faces_locations = face_recognition.face_locations(target_faces)
        target_faces_encodings = face_recognition.face_encodings(target_faces)

        # so sanh
        for (top, right, bottom, left), target_faces_encoding in zip(target_faces_locations, target_faces_encodings):
            matches = face_recognition.compare_faces(known_faces_encodings, target_faces_encoding, tolerance=0.55)
            print(matches)
            name = 'unknow'
            if True in matches:
                match_index = matches.index(True)
                name = known_faces_names[match_index]
                # ve ra o vuong len khuon mat nguoi duoc xac nhan
                cv2.rectangle(target_faces, (left, top), (right, bottom), (255, 0, 0), 3)
                cv2.rectangle(target_faces, (left, bottom + 30), (right, bottom), (255, 0, 0), cv2.FILLED)
                cv2.putText(target_faces, name, (left + 3, bottom + 25), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)

        # chieu hinh anh len
        def render_image():
            RGB_image = cv2.cvtColor(target_faces, cv2.COLOR_BGR2RGB)
            # ******A3: chuyển hình từ CV2 thành Pyqt5 *******
            # lấy hình từ A2 sau khi đã vẽ hình chữ nhật lên mặt
            image = RGB_image
            # khai báo kích thước hình ảnh
            height, width, channel = image.shape
            bytesPerLine = 3 * width
            # chuyển đổi ảnh CV2 thành Pyqt5
            image = QtGui.QImage(image.data, width, height, bytesPerLine,
                                 QtGui.QImage.Format_RGB888).rgbSwapped()
            # trình diễn ảnh Pyqt5 lên màn hình
            self.uic.Screen.setPixmap(QtGui.QPixmap.fromImage(image))

        render_image()

    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())