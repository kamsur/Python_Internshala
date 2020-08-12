'''OPEN existing team'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_openDialog(object):
    def setupUi(self, openDialog):
        openDialog.setObjectName("openDialog")
        openDialog.resize(158, 97)
        self.verticalLayout = QtWidgets.QVBoxLayout(openDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(openDialog)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(openDialog)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.openTeam(openDialog))
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        import sqlite3
        conn_teams=sqlite3.connect('cricket.db')
        cur_teams=conn_teams.cursor()
        teams= cur_teams.execute("SELECT name FROM teams;")                     # fetching team names
        y= teams.fetchall()
        for i in y:
            self.comboBox.addItem(i[0])                                         #i is tuple
        conn_teams.close()
        self.retranslateUi(openDialog)
        QtCore.QMetaObject.connectSlotsByName(openDialog)
        self.x=True

    def retranslateUi(self, openDialog):
        _translate = QtCore.QCoreApplication.translate
        openDialog.setWindowTitle(_translate("openDialog", "OPEN Team"))
        self.pushButton.setText(_translate("openDialog", "Open"))

    def openTeam(self,openDialog):
        if self.comboBox.currentText()!='':
            openDialog.close()
            self.x=False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    openDialog = QtWidgets.QDialog()
    ui = Ui_openDialog()
    ui.setupUi(openDialog)
    openDialog.show()
    sys.exit(app.exec_())
