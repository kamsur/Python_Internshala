'''MAIN application code'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fantasy.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from new import Ui_newDialog
from evaluate import Ui_evaDialog
from open import Ui_openDialog

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(580, 595)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setEnabled(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.selections = QtWidgets.QVBoxLayout()
        self.selections.setContentsMargins(-1, 0, -1, -1)
        self.selections.setObjectName("selections")
        self.selections_label = QtWidgets.QLabel(self.centralwidget)
        self.selections_label.setObjectName("selections_label")
        self.selections.addWidget(self.selections_label)
        self.selec_labval = QtWidgets.QWidget(self.centralwidget)
        self.selec_labval.setObjectName("selec_labval")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.selec_labval)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.batselec_label = QtWidgets.QLabel(self.selec_labval)
        self.batselec_label.setObjectName("batselec_label")
        self.horizontalLayout.addWidget(self.batselec_label)
        self.batselec_val = QtWidgets.QLabel(self.selec_labval)
        self.batselec_val.setText("")
        self.batselec_val.setObjectName("batselec_val")
        self.horizontalLayout.addWidget(self.batselec_val)
        self.bowselec_label = QtWidgets.QLabel(self.selec_labval)
        self.bowselec_label.setObjectName("bowselec_label")
        self.horizontalLayout.addWidget(self.bowselec_label)
        self.bowselec_val = QtWidgets.QLabel(self.selec_labval)
        self.bowselec_val.setText("")
        self.bowselec_val.setObjectName("bowselec_val")
        self.horizontalLayout.addWidget(self.bowselec_val)
        self.arselec_label = QtWidgets.QLabel(self.selec_labval)
        self.arselec_label.setObjectName("arselec_label")
        self.horizontalLayout.addWidget(self.arselec_label)
        self.arselec_val = QtWidgets.QLabel(self.selec_labval)
        self.arselec_val.setText("")
        self.arselec_val.setObjectName("arselec_val")
        self.horizontalLayout.addWidget(self.arselec_val)
        self.wkselec_label = QtWidgets.QLabel(self.selec_labval)
        self.wkselec_label.setObjectName("wkselec_label")
        self.horizontalLayout.addWidget(self.wkselec_label)
        self.wkselec_val = QtWidgets.QLabel(self.selec_labval)
        self.wkselec_val.setText("")
        self.wkselec_val.setObjectName("wkselec_val")
        self.horizontalLayout.addWidget(self.wkselec_val)
        self.selections.addWidget(self.selec_labval)
        self.verticalLayout.addLayout(self.selections)
        self.points = QtWidgets.QHBoxLayout()
        self.points.setObjectName("points")
        self.pointsA = QtWidgets.QWidget(self.centralwidget)
        self.pointsA.setObjectName("pointsA")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.pointsA)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pointsA_label = QtWidgets.QLabel(self.pointsA)
        self.pointsA_label.setObjectName("pointsA_label")
        self.horizontalLayout_2.addWidget(self.pointsA_label)
        self.pointsA_val = QtWidgets.QLabel(self.pointsA)
        self.pointsA_val.setText("")
        self.pointsA_val.setObjectName("pointsA_val")
        self.horizontalLayout_2.addWidget(self.pointsA_val)
        self.points.addWidget(self.pointsA)
        self.pointsU = QtWidgets.QWidget(self.centralwidget)
        self.pointsU.setObjectName("pointsU")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.pointsU)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pointsU_label = QtWidgets.QLabel(self.pointsU)
        self.pointsU_label.setObjectName("pointsU_label")
        self.horizontalLayout_3.addWidget(self.pointsU_label)
        self.pointsU_val = QtWidgets.QLabel(self.pointsU)
        self.pointsU_val.setText("")
        self.pointsU_val.setObjectName("pointsU_val")
        self.horizontalLayout_3.addWidget(self.pointsU_val)
        self.points.addWidget(self.pointsU)
        self.verticalLayout.addLayout(self.points)
        self.radteam = QtWidgets.QHBoxLayout()
        self.radteam.setObjectName("radteam")
        self.playersA_rad = QtWidgets.QWidget(self.centralwidget)
        self.playersA_rad.setObjectName("playersA_rad")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.playersA_rad)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.bat_rad = QtWidgets.QRadioButton(self.playersA_rad)
        self.bat_rad.setObjectName("bat_rad")
        self.horizontalLayout_4.addWidget(self.bat_rad)
        self.bow_rad = QtWidgets.QRadioButton(self.playersA_rad)
        self.bow_rad.setObjectName("bow_rad")
        self.horizontalLayout_4.addWidget(self.bow_rad)
        self.ar_rad = QtWidgets.QRadioButton(self.playersA_rad)
        self.ar_rad.setObjectName("ar_rad")
        self.horizontalLayout_4.addWidget(self.ar_rad)
        self.wk_rad = QtWidgets.QRadioButton(self.playersA_rad)
        self.wk_rad.setObjectName("wk_rad")
        self.horizontalLayout_4.addWidget(self.wk_rad)
        self.radteam.addWidget(self.playersA_rad)
        self.teamU = QtWidgets.QWidget(self.centralwidget)
        self.teamU.setObjectName("teamU")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.teamU)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.teamU_label = QtWidgets.QLabel(self.teamU)
        self.teamU_label.setObjectName("teamU_label")
        self.horizontalLayout_5.addWidget(self.teamU_label)
        self.teamU_name = QtWidgets.QLabel(self.teamU)
        self.teamU_name.setText("")
        self.teamU_name.setObjectName("teamU_name")
        self.horizontalLayout_5.addWidget(self.teamU_name)
        self.radteam.addWidget(self.teamU)
        self.verticalLayout.addLayout(self.radteam)
        self.list = QtWidgets.QHBoxLayout()
        self.list.setObjectName("list")
        self.listA = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listA.sizePolicy().hasHeightForWidth())
        self.listA.setSizePolicy(sizePolicy)
        self.listA.setObjectName("listA")
        self.list.addWidget(self.listA)
        self.listU = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listU.sizePolicy().hasHeightForWidth())
        self.listU.setSizePolicy(sizePolicy)
        self.listU.setObjectName("listU")
        self.list.addWidget(self.listU)

        self.verticalLayout.addLayout(self.list)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        mainWindow.setMenuBar(self.menubar)
        self.actionNEW_Team = QtWidgets.QAction(mainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionNEW_Team.triggered.connect(self.openNew)
        self.actionOPEN_Team = QtWidgets.QAction(mainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionOPEN_Team.triggered.connect(self.openOpen)
        self.actionSAVE_Team = QtWidgets.QAction(mainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionSAVE_Team.triggered.connect(self.saveteam)
        self.actionEVALUATE_Team = QtWidgets.QAction(mainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionEVALUATE_Team.triggered.connect(self.openEvaluate)
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Fantasy Cricket"))
        self.selections_label.setText(_translate("mainWindow", "Your Selections"))
        self.batselec_label.setText(_translate("mainWindow", "Batsmen(BAT)"))
        self.bowselec_label.setText(_translate("mainWindow", "Bowlers(BOW)"))
        self.arselec_label.setText(_translate("mainWindow", "Allrounders(AR)"))
        self.wkselec_label.setText(_translate("mainWindow", "Wicket-keeper(WK)"))
        self.pointsA_label.setText(_translate("mainWindow", "Points Available"))
        self.pointsU_label.setText(_translate("mainWindow", "Points Used"))
        self.bat_rad.setText(_translate("mainWindow", "BAT"))
        self.bow_rad.setText(_translate("mainWindow", "BOW"))
        self.ar_rad.setText(_translate("mainWindow", "AR"))
        self.wk_rad.setText(_translate("mainWindow", "WK"))
        self.teamU_label.setText(_translate("mainWindow", "Team Name"))
        self.menuManage_Teams.setTitle(_translate("mainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("mainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("mainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("mainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("mainWindow", "EVALUATE Team"))

    def openNew(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_newDialog()
        self.ui.setupUi(self.window)
        self.window.exec_()
    def openOpen(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_openDialog()
        self.ui.setupUi(self.window)
        self.window.exec_()
        if not self.ui.x:
            self.activate(self.ui.comboBox.currentText())
    def openEvaluate(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_evaDialog()
        self.ui.setupUi(self.window)
        self.window.exec_()

    def activate(self, selected_team):
        self.centralwidget.setEnabled(True)
        self.pointsA=1000
        self.pointsU=0
        self.selections={'BAT':0,'BWL':0,'AR':0,'WK':0}
        self.playersU={'BAT':[],'BWL':[],'AR':[],'WK':[]}
        self.playersA={'BAT':[],'BWL':[],'AR':[],'WK':[]}
        self.val={}
        self.listA.clear()
        self.listU.clear()
        self.selected_team=selected_team
        self.rad_ctg=''
        self.bat_rad.clicked.connect(lambda:self.listsetup('BAT'))
        self.bow_rad.clicked.connect(lambda:self.listsetup('BWL'))
        self.ar_rad.clicked.connect(lambda:self.listsetup('AR'))
        self.wk_rad.clicked.connect(lambda:self.listsetup('WK'))
        self.listA.itemDoubleClicked.connect(self.removelistA)                                 #REMOVELISTA
        self.listU.itemDoubleClicked.connect(self.removelistU)                                 #REMOVELISTU
        import sqlite3
        conn_activate=sqlite3.connect('cricket.db')
        cur_activate=conn_activate.cursor()
        cur_activate.execute("SELECT player,ctg,value from stats;")
        y=cur_activate.fetchall()
        for i in y:
            self.playersA[i[1]].append(i[0])
            self.val[i[0]]=i[2]
        cur_activate.execute("SELECT players from teams WHERE UPPER(name)=?;",(self.selected_team.upper(),))
        y=cur_activate.fetchone()
        if not y[0] is None:
            for i in y[0].split(','):
                item=QtWidgets.QListWidgetItem(i)
                self.removelistA(item)

        conn_activate.close()
        self.display()

    def listsetup(self, key):
        self.rad_ctg=key
        self.listA.clear()
        for i in self.playersA[key]:
            item=QtWidgets.QListWidgetItem(i)
            self.listA.addItem(item)

    def display(self):
        self.pointsA_val.setText("{}".format(self.pointsA))
        self.pointsU_val.setText("{}".format(self.pointsU))
        self.teamU_name.setText("{}".format(self.selected_team))
        self.batselec_val.setText("{}".format(self.selections['BAT']))
        self.bowselec_val.setText("{}".format(self.selections['BWL']))
        self.arselec_val.setText("{}".format(self.selections['AR']))
        self.wkselec_val.setText("{}".format(self.selections['WK']))

    def removelistA(self, item):
        for key, value in self.playersA.items():
            if item.text() in value:
                n=0
                for value in self.playersU.values():
                    n+=len(value)
                if n==11:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("11 players already selected")
                    msg.setWindowTitle("Failed")
                    msg.exec_()
                    break
                elif key=='WK' and len(self.playersU[key])>0:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Critical)
                    msg.setText("You can't select more than one wicketkeeper")
                    msg.setWindowTitle("Failed")
                    msg.exec_()
                    break
                elif self.val[item.text()]<=self.pointsA:
                    self.selections[key]+=1
                    self.playersU[key].append(item.text())
                    self.playersA[key].remove(item.text())
                    self.pointsU+=self.val[item.text()]
                    self.pointsA-=self.val[item.text()]
                    self.listA.takeItem(self.listA.row(item))
                    self.listU.addItem(item.text())
                    self.display()
                    break
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Not enough points available")
            msg.setWindowTitle("Failed")
            msg.exec_()

    def removelistU(self, item):
        for key, value in self.playersU.items():
            if item.text() in value and key==self.rad_ctg:
                self.selections[key]-=1
                self.playersU[key].remove(item.text())
                self.playersA[key].append(item.text())
                self.pointsU-=self.val[item.text()]
                self.pointsA+=self.val[item.text()]
                self.listU.takeItem(self.listU.row(item))
                self.listA.addItem(item.text())
                self.display()
                break
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Player does not belong to selected category")
            msg.setWindowTitle("Failed")
            msg.exec_()

    def saveteam(self):
        try:
            n=0
            for value in self.playersU.values():
                n+=len(value)
            if n<11:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                if (11-n)>1:
                    msg.setText("{} more players needed".format(11-n))
                else:
                    msg.setText("1 more player needed")
                msg.setWindowTitle("Failed")
                msg.exec_()
            elif len(self.playersU['WK'])==0:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Atleast one wicketkeeper needed")
                msg.setWindowTitle("Failed")
                msg.exec_()
            else:
                players=[]
                for value in self.playersU.values():
                    for i in value:
                        players.append(i)
                players_str = ','.join(players)
                import sqlite3
                conn_save=sqlite3.connect('cricket.db')
                cur_save=conn_save.cursor()
                cur_save.execute("UPDATE teams SET players=?, value=NULL WHERE UPPER(name)=?;",(players_str,self.selected_team.upper(),))
                conn_save.commit()
                conn_save.close()
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Team Saved\nOpen EVALUATE Team and select team {} to generate value of team\nand calculate results in matches against other teams".format(self.selected_team))
                msg.setWindowTitle("Success")
                msg.exec_()
        except:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("No Team Opened")
            msg.setWindowTitle("Failed")
            msg.exec_()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
