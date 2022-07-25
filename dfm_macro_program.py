from dfm_macro_ui import Ui_Form
from imagesearch import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import sys
import pyautogui as pag
import mouse
import keyboard
import time
from PIL import ImageGrab, Image
import numpy as np
import random as rn


class Macro(QWidget, Ui_Form):
    def __init__(self):
        super(Macro, self).__init__()
        self.setupUi(self)
        self.setFixedSize(340, 120)

        self.pos = []
        self.no_item = Image.open("./no_item1.png")
        self.no_item = np.array(self.no_item)
        self.no_item = cv2.cvtColor(self.no_item, cv2.COLOR_RGB2BGR)
        self.result_image = Image.open("./no_item2.png")
        self.result_image = np.array(self.result_image)
        self.result_image = cv2.cvtColor(self.result_image, cv2.COLOR_RGB2BGR)
        self.pur = Image.open("./pur.png")
        self.pur = np.array(self.pur)
        self.pur = cv2.cvtColor(self.pur, cv2.COLOR_RGB2BGR)

        self.end.setDisabled(True)
        self.start.setDisabled(True)
        self.get_image.clicked.connect(self.get_image_source)
        self.get_pos.clicked.connect(self.get_pos_source)
        self.start.clicked.connect(self.start_macro)
        # while True:
        #     print(pag.position())

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def get_image_source(self):
        self.get_image.setDisabled(True)
        self.get_pos.setDisabled(True)

        while True:
            if keyboard.is_pressed("q"):
                img_start_pos = pag.position()
                self.label.setText("pos1 selected.")
                self.label.repaint()
                time.sleep(0.1)
                break

        while True:
            if keyboard.is_pressed("q"):
                img_end_pos = pag.position()
                self.label.setText("pos2 selected.")
                self.label.repaint()
                time.sleep(0.1)
                break

        img = ImageGrab.grab()
        self.img = img.crop(
            (img_start_pos.x, img_start_pos.y, img_end_pos.x, img_end_pos.y)
        )
        self.img = np.array(self.img)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)

        self.get_pos.setDisabled(False)

    def get_pos_source(self):
        while True:
            if keyboard.is_pressed("q"):
                self.pos.append(pag.position())
                self.label.setText("click pos" + str(len(self.pos)) + " selected.")
                self.label.repaint()
                time.sleep(0.1)
                break
        if len(self.pos) >= 6:
            self.start.setDisabled(False)
            self.end.setDisabled(False)
            self.get_pos.setDisabled(True)

    def start_macro(self):
        while True:
            pag.moveTo(
                rn.uniform(self.pos[0].x, self.pos[0].x + 140),
                rn.uniform(self.pos[0].y, self.pos[0].y + 25),
                rn.uniform(0.04, 0.08),
            )
            pag.click()
            search_pos = imagesearch(self.img)
            if search_pos[0] == -1:
                continue
            pag.moveTo(
                rn.uniform(search_pos[0] + 80, search_pos[0] + 370),
                rn.uniform(search_pos[1], search_pos[1] + 60),
            )
            pag.click()

            if imagesearch(self.no_item)[0] != -1:
                print("재고 없음")
                pag.press("esc")
                continue

            pag.moveTo(
                rn.uniform(self.pos[1].x, self.pos[1].x + 80),
                rn.uniform(self.pos[1].y, self.pos[1].y + 15),
                rn.uniform(0.09, 0.13),
            )
            pag.click()

            pag.moveTo(
                rn.uniform(self.pos[2].x, self.pos[2].x + 45),
                rn.uniform(self.pos[2].y, self.pos[2].y + 45),
                rn.uniform(0.09, 0.13),
            )
            pag.click()

            pag.moveTo(
                rn.uniform(self.pos[3].x, self.pos[3].x + 45),
                rn.uniform(self.pos[3].y, self.pos[3].y + 120),
                rn.uniform(0.09, 0.13),
            )
            pag.click()

            pag.moveTo(
                rn.uniform(self.pos[4].x, self.pos[4].x + 140),
                rn.uniform(self.pos[4].y, self.pos[4].y + 35),
                rn.uniform(0.09, 0.13),
            )
            pag.click()

            pag.moveTo(
                rn.uniform(self.pos[5].x, self.pos[5].x + 160),
                rn.uniform(self.pos[5].y, self.pos[5].y + 35),
                rn.uniform(0.09, 0.13),
            )
            pag.click()

            time.sleep(2.0)
            if imagesearch(self.result_image)[0] != -1:
                print("재고 없음")
                pag.press("esc")
                time.sleep(rn.uniform(1.0, 2.0))
            if imagesearch(self.pur)[0] != -1:
                pag.press("esc")
            print("=" * 50)
            time.sleep(rn.uniform(1.0, 2.0))


def main():
    app = QApplication(sys.argv)
    win = Macro()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
