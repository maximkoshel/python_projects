import sys
import translation
import injector
from sys import exit as sysExit
from PyQt5 import QtCore, QtGui, QtWidgets

global r , file

r = open("saving.txt",encoding="utf-8").read()

#translate Function  -----------------------------------------------------------
def translate_Pushed():
    file = open("Saving.txt","r+",encoding="utf-8")
    lines = file.readlines()
    file.seek(0)
    global detect,text_translate
    text_translate = ui.textEdit_main.toPlainText()
    translated = translation.translate(text_translate)
    Hebrew = translated[0]
    Russian = translated[1]
    English = translated[2]
    detect = translation.detect_language(text_translate)
    file.write(Hebrew+' - '+ Russian+' - '+English+'\n')
    for line in lines:
        file.write(line)
    file.close()
    j = open("saving.txt",encoding="utf-8").read()
    ui.textBrowser.setText(j)
    ui.textBrowser.update()

    if(detect.lang == 'en'):
        ui.textEdit_2.setText(Hebrew)
        ui.textEdit_1.setText(Russian)
    if(detect.lang == 'ru'):
        ui.textEdit_2.setText(Hebrew)
        ui.textEdit_1.setText(English)
    if(detect.lang == 'iw'):
        ui.textEdit_1.setText(Russian)
        ui.textEdit_2.setText(English)
#check spelling func------------------------------------------------------------
def check_spelling():
    text_translate = ui.textEdit_main.toPlainText()
    injector.chrome_check_spelling(text_translate)
#Open more Function ------------------------------------------------------------
def open_more1():

    if(detect.lang == 'iw'):
        injector.hebrew_to_russian(text_translate)
    elif(detect.lang == 'ru'):
        injector.russian_to_english(text_translate)
    elif(detect.lang == 'en'):
        injector.english_to_russian(text_translate)
def open_more2():
    if(detect.lang == 'iw'):
        injector.hebrew_to_english(text_translate)
    elif(detect.lang == 'ru'):
        injector.russian_to_hebrew(text_translate)
    elif(detect.lang == 'en'):
        injector.english_to_hebrew(text_translate)
#-------------------------------------------------------------------------------

#GUI----------------------------------------------------------------------------
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(845, 781)



        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-20, -300, 891, 1141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Untitled-2.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setIndent(0)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")

        self.textEdit_main = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_main.setGeometry(QtCore.QRect(190, 140, 411, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_main.setFont(font)
        self.textEdit_main.setObjectName("textEdit_main")

        self.textEdit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_1.setGeometry(QtCore.QRect(10, 320, 411, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_1.setFont(font)
        self.textEdit_1.setObjectName("textEdit_1")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(425, 320, 411, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")




        #Spelling button-------------------------------------------------------
        self.pushSpelling = QtWidgets.QPushButton(self.centralwidget)
        self.pushSpelling.setGeometry(QtCore.QRect(600, 139, 131, 40))
        self.pushSpelling.setObjectName("pushSpelling")
        self.pushSpelling.clicked.connect(check_spelling)
        #Translate button -----------------------------------------------------
        self.pushTranslate = QtWidgets.QPushButton(self.centralwidget)
        self.pushTranslate.setGeometry(QtCore.QRect(330, 240, 131, 31))
        self.pushTranslate.setObjectName("pushTranslate")
        self.pushTranslate.clicked.connect(translate_Pushed)
        #-----------------------------------------------------------------------
        #Left button -----------------------------------------------------------
        self.OpenWebsite_1 = QtWidgets.QPushButton(self.centralwidget)
        self.OpenWebsite_1.setGeometry(QtCore.QRect(150, 420, 131, 31))
        self.OpenWebsite_1.setObjectName("OpenWebsite_1")
        self.OpenWebsite_1.clicked.connect(open_more1)
        #-----------------------------------------------------------------------
        #Right botton-----------------------------------------------------------
        self.openWensite_2 = QtWidgets.QPushButton(self.centralwidget)
        self.openWensite_2.setGeometry(QtCore.QRect(560, 420, 131, 31))
        self.openWensite_2.setObjectName("openWensite_2")
        self.openWensite_2.clicked.connect(open_more2)
        #-----------------------------------------------------------------------
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(190, 510, 411, 202))
        self.textBrowser.setObjectName("textBrowser")

        self.label_2.raise_()
        self.pushTranslate.raise_()
        self.textEdit_2.raise_()
        self.textEdit_1.raise_()
        self.textEdit_main.raise_()
        self.OpenWebsite_1.raise_()
        self.openWensite_2.raise_()
        self.textBrowser.raise_()
        self.pushSpelling.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushTranslate.setText(_translate("MainWindow", "Translate"))
        self.openWensite_2.setText(_translate("MainWindow", "Open Website"))
        self.OpenWebsite_1.setText(_translate("MainWindow", "Open Website"))
        self.pushSpelling.setText(_translate("MainWindow", "Check Spelling"))

        app.aboutToQuit.connect(self.closeEvent)
    def closeEvent(self):
        sys.exit(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.textBrowser.setPlainText(r) #show history search
    sys.exit(app.exec_())
