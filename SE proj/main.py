import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5 import QtCore
import pyrebase
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import mode
from argparse import ArgumentParser
import cv2 as cv
import winsound

PW='xxxxx'

firebaseConfig = {'apiKey': "AIzaSyBoVwS25BX7K2ZYLRR3P3voCocn6JGsXSM",
    'authDomain': "seproj1-eb3b9.firebaseapp.com",
    'databaseURL': "xxxxxx",
    'projectId': "seproj1-eb3b9",
    'storageBucket': "seproj1-eb3b9.appspot.com",
    'messagingSenderId': "929935515972",
    'appId': "1:929935515972:web:b53e771200534ea1e17711",
    'measurementId': "G-8Z133Q9X6R"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


class MyApp(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('mark1.ui', self)


        self.log.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createAccount.clicked.connect(self.gotoSignUp)
    def loginfunction(self):
        if(auth.sign_in_with_email_and_password(self.email.text(),self.password.text())):
            print("logged in")
            mainwindow = mainWindow()
            widget.addWidget(mainwindow)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            print("invalid credential")
    def gotoSignUp(self):
        newaccount = signUp()
        widget.addWidget(newaccount)
        widget.setCurrentIndex(widget.currentIndex()+1)

class signUp(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('mark3.ui', self)
        self.signUpButton.clicked.connect(self.signupfunction)
        self.confirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.back.clicked.connect(self.goBack)
    def goBack(self):
            app = MyApp()
            widget.addWidget(app)
            widget.setCurrentIndex(widget.currentIndex() + 1)
    def signupfunction(self):
        if self.password.text() == self.confirmPassword.text():
            email = self.email.text()
            password = self.password.text()
            try:
               auth.create_user_with_email_and_password(email, password)
               login = MyApp()
               widget.addWidget(login)
               widget.setCurrentIndex(widget.currentIndex()+1)
            except:
                print("error")
        else:
            print("invalid credential")


class mainWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('mark2.ui', self)
        self.logoutButton.clicked.connect(self.gotologinpage)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.changeNo.clicked.connect(self.gotochangenum)
        self.changePass.clicked.connect(self.gotochangepass)
        currentDate = QDate.currentDate()
        labelDate = currentDate.toString()
        print(labelDate)
        self.dateTime_2.setText(labelDate)
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.imageUpdate.connect(self.imageUpdateSlot)
        #self.stop.clicked.connect(self.cancelFeed)
        #self.start.clicked.connect(self.Worker1.start())


    def imageUpdateSlot(self, image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(image))
    def cancelFeed(self):
        self.Worker1.stop()
    def ImageUpdateSlot(self, Image):
        self.liveVideo.setPixmap(QPixmap.fromImage(Image))
    def gotologinpage(self):
        login = MyApp()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.dateTime.setText(label_time)
    def gotochangenum(self):
        newpage = changeNumber()
        widget.addWidget(newpage)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotochangepass(self):
        newpage = changePassword()
        widget.addWidget(newpage)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Worker1(QThread):
    imageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True

        ap = ArgumentParser()
        ap.add_argument('-rec', '--record', default=False, action='store_true', help='Record?')
        ap.add_argument('-pscale', '--pyr_scale', default=0.5, type=float,
                            help='Image scale (<1) to build pyramids for each image')
        ap.add_argument('-l', '--levels', default=3, type=int, help='Number of pyramid layers')
        ap.add_argument('-w', '--winsize', default=15, type=int, help='Averaging window size')
        ap.add_argument('-i', '--iterations', default=3, type=int,
                            help='Number of iterations the algorithm does at each pyramid level')
        ap.add_argument('-pn', '--poly_n', default=5, type=int,
                            help='Size of the pixel neighborhood used to find polynomial expansion in each pixel')
        ap.add_argument('-psigma', '--poly_sigma', default=1.1, type=float,
                            help='Standard deviation of the Gaussian that is used to smooth derivatives used as a basis for the polynomial expansion')
        ap.add_argument('-th', '--threshold', default=10.0, type=float, help='Threshold value for magnitude')
        ap.add_argument('-p', '--plot', default=False, action='store_true', help='Plot accumulators?')
        ap.add_argument('-rgb', '--rgb', default=False, action='store_true', help='Show RGB mask?')
        ap.add_argument('-s', '--size', default=10, type=int, help='Size of accumulator for directions map')

        args = vars(ap.parse_args())

        directions_map = np.zeros([args['size'], 5])
        while self.ThreadActive:
            cap = cv.VideoCapture(0)
            if args['record']:
                h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
                w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
                codec = cv.VideoWriter_fourcc(*'MPEG')
                out = cv.VideoWriter('out.avi', codec, 10.0, (w, h))

            if args['plot']:
                plt.ion()

            frame_previous = cap.read()[1]
            gray_previous = cv.cvtColor(frame_previous, cv.COLOR_BGR2GRAY)
            hsv = np.zeros_like(frame_previous)
            hsv[:, :, 1] = 255
            param = {
                'pyr_scale': args['pyr_scale'],
                'levels': args['levels'],
                'winsize': args['winsize'],
                'iterations': args['iterations'],
                'poly_n': args['poly_n'],
                'poly_sigma': args['poly_sigma'],
                'flags': cv.OPTFLOW_LK_GET_MIN_EIGENVALS
            }

            while True:
                grabbed, frame = cap.read()
                if not grabbed:
                    break

                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                flow = cv.calcOpticalFlowFarneback(gray_previous, gray, None, **param)
                mag, ang = cv.cartToPolar(flow[:, :, 0], flow[:, :, 1], angleInDegrees=True)
                ang_180 = ang / 2

                gray_previous = gray
                move_sense = ang[mag > args['threshold']]
                move_mode = mode(move_sense)[0]

                if 10 < move_mode <= 100:
                    directions_map[-1, 0] = 1
                    directions_map[-1, 1:] = 0
                    directions_map = np.roll(directions_map, -1, axis=0)
                elif 100 < move_mode <= 190:
                    directions_map[-1, 1] = 1
                    directions_map[-1, :1] = 0
                    directions_map[-1, 2:] = 0
                    directions_map = np.roll(directions_map, -1, axis=0)
                elif 190 < move_mode <= 280:
                    directions_map[-1, 2] = 1
                    directions_map[-1, :2] = 0
                    directions_map[-1, 3:] = 0
                    directions_map = np.roll(directions_map, -1, axis=0)
                elif 280 < move_mode or move_mode < 10:
                    directions_map[-1, 3] = 1
                    directions_map[-1, :3] = 0
                    directions_map[-1, 4:] = 0
                    directions_map = np.roll(directions_map, -1, axis=0)
                else:
                    directions_map[-1, -1] = 1
                    directions_map[-1, :-1] = 0
                    directions_map = np.roll(directions_map, 1, axis=0)

                if args['plot']:
                    plt.clf()
                    plt.plot(directions_map[:, 0], label='Down')
                    plt.plot(directions_map[:, 1], label='Right')
                    plt.plot(directions_map[:, 2], label='Up')
                    plt.plot(directions_map[:, 3], label='Left')
                    plt.plot(directions_map[:, 4], label='Waiting')
                    plt.legend(loc=2)
                    plt.pause(1e-5)
                    plt.show()

                loc = directions_map.mean(axis=0).argmax()
                if loc == 0:
                    text = 'Moving down'
                elif loc == 1:
                    text = 'Moving to the right'
                elif loc == 2:
                    text = 'Moving up'
                elif loc == 3:
                    text = 'Moving to the left'
                else:
                    text = 'move to detect motion'


                if loc in [0,1,2,3]:
                    winsound.Beep(2000, 100)



                hsv[:, :, 0] = ang_180
                hsv[:, :, 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
                rgb = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)

                frame = cv.flip(frame, 1)
                cv.putText(frame, text, (30, 90), cv.FONT_HERSHEY_COMPLEX, frame.shape[1] / 500, (0, 0, 255), 2)

                k = cv.waitKey(1) & 0xff
                if k == ord('q'):
                    break
                if args['record']:
                    out.write(frame)
                if args['rgb']:
                    cv.imshow('Mask', rgb)
                image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                flippedImage = image
                convertToQtFormat = QImage(flippedImage.data, flippedImage.shape[1], flippedImage.shape[0],
                                           QImage.Format_RGB888)
                pic = convertToQtFormat.scaled(1081, 541, Qt.KeepAspectRatio)
                self.imageUpdate.emit(pic)


                k = cv.waitKey(1) & 0xff
                if k == ord('q'):
                    break

            cap.release()
            if args['record']:
                out.release()
            if args['plot']:
                plt.ioff()
            cv.destroyAllWindows()




    def stop(self):
        self.ThreadActive = False
        self.quit()




class changeNumber(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('mark4.ui', self)
        self.submitNo.clicked.connect(self.changenum)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.back.clicked.connect(self.goBack)
    def goBack(self):
            app = mainWindow()
            widget.addWidget(app)
            widget.setCurrentIndex(widget.currentIndex() + 1)
    def changenum(self):
        if self.password.text() == PW:
            app = mainWindow()
            widget.addWidget(app)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            print("invalid credential")


class changePassword(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('mark5.ui', self)
        self.submit.clicked.connect(self.changepass)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.back.clicked.connect(self.goBack)
    def goBack(self):
            app = mainWindow()
            widget.addWidget(app)
            widget.setCurrentIndex(widget.currentIndex() + 1)
    def changepass(self):
        if self.password.text() == PW:
            if self.newPass.text() == self.confirmPass.text():
             app = mainWindow()
             widget.addWidget(app)
             widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                print("typo error in password")
        else:
            print("invalid credential")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    app_icon = QtGui.QIcon()
    app_icon.addFile('logo.png')
    app.setWindowIcon(app_icon)
    app.setApplicationName('MR.SECURITY BETA')
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(myapp)
    widget.setFixedWidth(1094)
    widget.setFixedHeight(707)
    widget.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing window')