# Form implementation generated from reading ui file 'avtorr2.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(629, 503)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.label_profil = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_profil.setGeometry(QtCore.QRect(220, 80, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_profil.setFont(font)
        self.label_profil.setObjectName("label_profil")
        self.label_login = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(160, 180, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.label_parol = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_parol.setGeometry(QtCore.QRect(160, 220, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_parol.setFont(font)
        self.label_parol.setObjectName("label_parol")
        self.label_familia = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_familia.setGeometry(QtCore.QRect(160, 260, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_familia.setFont(font)
        self.label_familia.setObjectName("label_familia")
        self.label_dolshnost = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_dolshnost.setGeometry(QtCore.QRect(160, 290, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_dolshnost.setFont(font)
        self.label_dolshnost.setObjectName("label_dolshnost")
        self.lineEdit_log2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_log2.setGeometry(QtCore.QRect(300, 180, 151, 21))
        self.lineEdit_log2.setObjectName("lineEdit_log2")
        self.lineEdit_dols2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_dols2.setGeometry(QtCore.QRect(300, 290, 151, 21))
        self.lineEdit_dols2.setObjectName("lineEdit_dols2")
        self.lineEdit_par2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_par2.setGeometry(QtCore.QRect(300, 220, 151, 21))
        self.lineEdit_par2.setObjectName("lineEdit_par2")
        self.lineEdit_fam2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_fam2.setGeometry(QtCore.QRect(300, 260, 151, 21))
        self.lineEdit_fam2.setObjectName("lineEdit_fam2")
        self.label_par = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_par.setGeometry(QtCore.QRect(300, 220, 151, 20))
        self.label_par.setText("")
        self.label_par.setObjectName("label_par")
        self.label_fam = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_fam.setGeometry(QtCore.QRect(300, 260, 141, 21))
        self.label_fam.setText("")
        self.label_fam.setObjectName("label_fam")
        self.pushButton_vihod = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_vihod.setGeometry(QtCore.QRect(310, 370, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_vihod.setFont(font)
        self.pushButton_vihod.setObjectName("pushButton_vihod")
        self.pushButton_save = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(310, 350, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setObjectName("pushButton_save")
        self.label_zanit = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_zanit.setGeometry(QtCore.QRect(280, 320, 161, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_zanit.setFont(font)
        self.label_zanit.setObjectName("label_zanit")
        self.label_log2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_log2.setGeometry(QtCore.QRect(300, 180, 141, 20))
        self.label_log2.setText("")
        self.label_log2.setObjectName("label_log2")
        self.label_dol2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_dol2.setGeometry(QtCore.QRect(300, 290, 151, 21))
        self.label_dol2.setText("")
        self.label_dol2.setObjectName("label_dol2")
        self.pushButton_izmenit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_izmenit.setGeometry(QtCore.QRect(300, 350, 141, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_izmenit.setFont(font)
        self.pushButton_izmenit.setObjectName("pushButton_izmenit")
        self.label_error = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(290, 330, 131, 20))
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 26))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))
        self.label_profil.setText(_translate("MainWindow2", "Мой профиль"))
        self.label_login.setText(_translate("MainWindow2", "Логин:"))
        self.label_parol.setText(_translate("MainWindow2", "Пароль:"))
        self.label_familia.setText(_translate("MainWindow2", "Фамилия:"))
        self.label_dolshnost.setText(_translate("MainWindow2", "Должность:"))
        self.pushButton_vihod.setText(_translate("MainWindow2", "Выйти"))
        self.pushButton_save.setText(_translate("MainWindow2", "Сохранить"))
        self.label_zanit.setText(_translate("MainWindow2", "Этот логин уже занят"))
        self.pushButton_izmenit.setText(_translate("MainWindow2", "Изменить данные"))
