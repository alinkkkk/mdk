from PyQt6.QtWidgets import QApplication, QMainWindow

from avtorr import Ui_MainWindow1
from avtorr2 import Ui_MainWindow2

import sys
import sqlite3

myConnection = sqlite3.connect("base1.db")
myCursor = myConnection.cursor()
myCursor2 = myConnection.cursor()

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow1()
ui.setupUi(window)

window.show()
ui.label_2.setVisible(False)
ui.label_familia.setVisible(False)
ui.familiaEdit.setVisible(False)
ui.label_povtor.setVisible(False)
ui.lineEdit_povtor.setVisible(False)
ui.label_dolsh.setVisible(False)
ui.lineEdit_dolsh.setVisible(False)
ui.pushButton_profil.setVisible(False)
# ui.label_login.setVisible(True)
ui.label_nevse.setVisible(False)
#ui.label_myprof.setVisible(False)


def on_click():
    global login
    global password
    login = str(ui.lineEdit.text())
    password = str(ui.lineEdit_2.text())
    vhod = 0
    myCursor.execute("select * from avtor where Логин=? AND Пароль=?", (login, password))
    myResult = myCursor.fetchall()
    for i in myResult:
        if str(ui.lineEdit.text()) == str(i[1]) and str(ui.lineEdit_2.text()) == str(i[2]):
            vhod += 1
    if vhod == 1:
        print("ОКЕЙ")
        ui.label.setText("добро пожаловать!!!!")
        ui.pushButton_profil.setVisible(True)
    else:
        print("Отказано в доступе")
        ui.label.setText("Введено неверно")


def on_click2():
    ui.akk_label.setVisible(False)
    ui.pushButton.setVisible(False)
    ui.label_2.setVisible(True)
    ui.label_familia.setVisible(True)
    ui.familiaEdit.setVisible(True)
    ui.label_povtor.setVisible(True)
    ui.lineEdit_povtor.setVisible(True)
    ui.label_dolsh.setVisible(True)
    ui.lineEdit_dolsh.setVisible(True)
    ui.pushButton_profil.setVisible(False)
    ui.label_dobpol.setVisible(False)
    # myCursor.execute("select Логин from avtor ")
    # myResult = myCursor.fetchall()
    # print(myResult)

    login = str(ui.lineEdit.text())
    password = str(ui.lineEdit_2.text())
    familia = str(ui.familiaEdit.text())
    povtor = str(ui.lineEdit_povtor.text())
    dolsh = str(ui.lineEdit_dolsh.text())

    if password != povtor:
        ui.label.setText("Пароли не совпадают")
        return

    myCursor.execute("SELECT * FROM avtor WHERE Логин=?", (login,))
    result = myCursor.fetchall()
    if result:
        ui.label.setText("Пользователь уже с таким логином существует")
        return

        # if "@" not in login:
        #     ui.label.setText("Логин должен содержать символ @")
        #     return

    if len(password) < 8:
        ui.label.setText("Пароль должен быть не менее 8 символов")
        return
    if not any(char.isdigit() for char in password):
        ui.label.setText("Пароль должен содержать хотя бы одну цифру")
        return



    command = "INSERT INTO avtor (Логин, Пароль, Фамилия, Должность) VALUES (?, ?, ?, ?)"
    myCursor.execute(command, (login, password, familia, dolsh))
    myConnection.commit()
    ui.label.setText("Пользователь успешно добавлен")
    #ui.pushButton_profil.setVisible(True)

    ui.lineEdit.setVisible(True)
    ui.lineEdit_2.setVisible(True)
    ui.pushButton.setVisible(True)
    ui.login_label.setVisible(True)
    ui.pas_label.setVisible(True)
    ui.akk_label.setVisible(True)
    ui.label_dobpol.setVisible(True)
    ui.pushButton_regr.setVisible(True)

    ui.pushButton_regr.setVisible(False)
    ui.label_2.setVisible(False)
    #i.pas_label.setVisible(False)
    #ui.login_label.setVisible(False)
    ui.label_povtor.setVisible(False)
    ui.label_dolsh.setVisible(False)
    ui.label_familia.setVisible(False)
    ui.familiaEdit.setVisible(False)
    ui.lineEdit_povtor.setVisible(False)
    ui.lineEdit_dolsh.setVisible(False)
def on_click3():  # профиль
    ui.label.setVisible(False)
    ui.akk_label.setVisible(False)
    ui.pushButton.setVisible(False)
    ui.label_2.setVisible(False)
    ui.label_familia.setVisible(False)
    ui.familiaEdit.setVisible(False)
    ui.label_povtor.setVisible(False)
    ui.lineEdit_povtor.setVisible(False)
    ui.label_dolsh.setVisible(False)
    ui.lineEdit_dolsh.setVisible(False)
    ui.pushButton_profil.setVisible(False)
    ui.lineEdit.setVisible(False)
    ui.lineEdit_2.setVisible(False)
    ui.pas_label.setVisible(False)
    ui.login_label.setVisible(False)
    ui.pushButton_regr.setVisible(False)
    #ui.label_myprof.setVisible(True)
    ui.label_dobpol.setVisible(False)

    global window2
    window2 = QMainWindow()
    ui2 = Ui_MainWindow2()
    ui2.setupUi(window2)
    window.close()
    window2.show()

    myCursor.execute("select * from avtor ")
    myResult = myCursor.fetchall()
    for i in myResult:
        if login == str(i[1]) and password == str(i[2]):
            global id
            global familia
            familia=str(i[3])
            id=str(i[0])

    for i in myResult:
        if id == str(i[0]) :
            ui2.label_log2.setText(str(i[1]))
            ui2.label_par.setText(str(i[2]))
            ui2.label_fam.setText(str(i[3]))
            ui2.label_dol2.setText(str(i[4]))

    def change():
        ui2.label_log2.setVisible(False)
        ui2.label_par.setVisible(False)
        ui2.label_fam.setVisible(False)
        ui2.label_dol2.setVisible(False)
        ui2.pushButton_izmenit.setVisible(False)

        ui2.lineEdit_log2.setVisible(True)
        ui2.lineEdit_par2.setVisible(True)
        ui2.lineEdit_fam2.setVisible(True)
        ui2.lineEdit_dols2.setVisible(True)
        ui2.pushButton_save.setVisible(True)
        ui2.pushButton_vihod.setVisible(False)

        for i in myResult:
            if id == str(i[0]) :
                ui2.lineEdit_log2.setText(str(i[1]))
                ui2.lineEdit_par2.setText(str(i[2]))
                ui2.lineEdit_fam2.setText(str(i[3]))
                ui2.lineEdit_dols2.setText(str(i[4]))

    ui2.pushButton_izmenit.clicked.connect(change)

    def change(): #изменение внесенных данных
        login = str(ui.lineEdit.text())
        print(login)
        myCursor.execute("select login from avtor ")
        myResult = myCursor.fetchall()
        print(myResult)
        lg = []
        for i in myResult:
            lg.append(i[0])

        if login!=str(ui2.lineEdit_log2.text()) and str(ui2.lineEdit_log2.text()) in lg:
            ui2.label_zanit.setVisible(True)

        else:
            login = str(ui2.lineEdit_log2.text())
            password = str(ui2.lineEdit_par2.text())
            familia = str(ui2.lineEdit_fam2.text())
            dolsh = str(ui2.lineEdit_dols2.text())
            command = """UPDATE avtor SET login=?, password=?, familia=?, dolsh=? WHERE login=?"""
            data = (login, password, familia, dolsh)
            myCursor.execute(command, data)
            myConnection.commit()
            ui2.label_log2.setText(login)
            ui2.label_par.setText(password)
            ui2.label_fam.setText(familia)
            ui2.label_dol2.setText(dolsh)


            ui2.label_log2.setVisible(True)
            ui2.label_par.setVisible(True)
            ui2.label_fam.setVisible(True)
            ui2.label_dol2.setVisible(True)
            ui2.pushButton_save.setVisible(True)

            ui2.lineEdit_log2.setVisible(False)
            ui2.lineEdit_par2.setVisible(False)
            ui2.lineEdit_fam2.setVisible(False)
            ui2.lineEdit_dols2.setVisible(False)
            ui2.pushButton_save.setVisible(False)
            ui2.pushButton_vihod.setVisible(True)


    ui2.pushButton_save.clicked.connect(change)


    def home():
        window2.close()
        window.show()

    ui2.pushButton_vihod.clicked.connect(home)

ui.pushButton.clicked.connect(on_click)
ui.pushButton_regr.clicked.connect(on_click2)
ui.pushButton_profil.clicked.connect(on_click3)
app.exec()