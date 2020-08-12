'''Create NEW team'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newDialog(object):
    def setupUi(self, newDialog):
        newDialog.setObjectName("newDialog")
        newDialog.resize(193, 108)
        self.verticalLayout = QtWidgets.QVBoxLayout(newDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalWidget = QtWidgets.QWidget(newDialog)
        self.verticalWidget.setObjectName("verticalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newteam_label = QtWidgets.QLabel(self.verticalWidget)
        self.newteam_label.setObjectName("newteam_label")
        self.horizontalLayout.addWidget(self.newteam_label)
        self.verticalLayout.addWidget(self.verticalWidget)
        self.verticalWidget_2 = QtWidgets.QWidget(newDialog)
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.verticalWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.newteam_entry = QtWidgets.QLineEdit(self.verticalWidget_2)
        self.newteam_entry.setObjectName("newteam_entry")
        self.horizontalLayout_2.addWidget(self.newteam_entry)
        self.verticalLayout.addWidget(self.verticalWidget_2)
        self.verticalWidget_3 = QtWidgets.QWidget(newDialog)
        self.verticalWidget_3.setObjectName("verticalWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.verticalWidget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(self.create)
        self.buttonBox.rejected.connect(newDialog.close)
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.verticalWidget_3)

        self.retranslateUi(newDialog)
        QtCore.QMetaObject.connectSlotsByName(newDialog)

    def retranslateUi(self, newDialog):
        _translate = QtCore.QCoreApplication.translate
        newDialog.setWindowTitle(_translate("newDialog", "NEW Team"))
        self.newteam_label.setText(_translate("newDialog", "Enter Team Name"))

    def create(self):
        teamname=self.newteam_entry.text()
        if len(teamname)>0:
            import sqlite3
            conn_new=sqlite3.connect('cricket.db')
            cur_new=conn_new.cursor()
            cur_new.execute("SELECT name from teams WHERE UPPER(name)=?;",(teamname.upper(),))
            check=cur_new.fetchall()
            if len(check)>0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Name already exists")
                msg.setWindowTitle("Failed")
                msg.exec_()
            else:
                cur_new.execute("INSERT INTO teams (name,players,value) VALUES (?,?,?);",(teamname,None,None))
                conn_new.commit()
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team Created\nClick OPEN Team and select team {}\nto edit/add players to team".format(teamname))
                msg.setWindowTitle("Success")
                msg.exec_()
            self.newteam_entry.clear()
            conn_new.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newDialog = QtWidgets.QDialog()
    ui = Ui_newDialog()
    ui.setupUi(newDialog)
    newDialog.show()
    sys.exit(app.exec_())
