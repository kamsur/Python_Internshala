'''Calculate Team Score'''
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_evaDialog(object):
    def setupUi(self, evaDialog):
        evaDialog.setObjectName("evaDialog")
        evaDialog.resize(422, 393)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(evaDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.selection = QtWidgets.QVBoxLayout()
        self.selection.setObjectName("selection")
        self.selection_label = QtWidgets.QLabel(evaDialog)
        self.selection_label.setObjectName("selection_label")
        self.selection.addWidget(self.selection_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.slection_box = QtWidgets.QWidget(evaDialog)
        self.slection_box.setObjectName("slection_box")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.slection_box)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.teamselec = QtWidgets.QComboBox(self.slection_box)
        self.teamselec.setEditable(False)
        self.teamselec.setObjectName("teamselec")
        self.teamselec.addItem("")
        import sqlite3
        conn_teams=sqlite3.connect('cricket.db')
        cur_teams=conn_teams.cursor()
        teams= cur_teams.execute("SELECT name, value FROM teams;")                     # fetching team names
        y=teams.fetchall()
        self.opponent={}
        for i in y:
            self.teamselec.addItem(i[0])
            if i[1]!=None:
                self.opponent[i[0]]=i[1]                                                      #i is tuple
        conn_teams.close()
        self.teamselec.currentTextChanged.connect(self.listsetup)
        self.horizontalLayout.addWidget(self.teamselec)
        self.matchselec = QtWidgets.QComboBox(self.slection_box)
        self.matchselec.setEditable(False)
        self.matchselec.setObjectName("matchselec")
        self.matchselec.addItem("")
        self.horizontalLayout.addWidget(self.matchselec)
        self.selection.addWidget(self.slection_box)
        self.verticalLayout_2.addLayout(self.selection)
        self.line = QtWidgets.QFrame(evaDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.list = QtWidgets.QVBoxLayout()
        self.list.setObjectName("list")
        self.pplabel = QtWidgets.QWidget(evaDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pplabel.sizePolicy().hasHeightForWidth())
        self.pplabel.setSizePolicy(sizePolicy)
        self.pplabel.setObjectName("pplabel")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.pplabel)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.players_label = QtWidgets.QLabel(self.pplabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.players_label.sizePolicy().hasHeightForWidth())
        self.players_label.setSizePolicy(sizePolicy)
        self.players_label.setObjectName("players_label")
        self.horizontalLayout_2.addWidget(self.players_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.points_label = QtWidgets.QLabel(self.pplabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.points_label.sizePolicy().hasHeightForWidth())
        self.points_label.setSizePolicy(sizePolicy)
        self.points_label.setObjectName("points_label")
        self.horizontalLayout_2.addWidget(self.points_label)
        self.points_value = QtWidgets.QLabel(self.pplabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.points_value.sizePolicy().hasHeightForWidth())
        self.points_value.setSizePolicy(sizePolicy)
        self.points_value.setText("")
        self.points_value.setObjectName("points_value")
        self.horizontalLayout_2.addWidget(self.points_value)
        self.list.addWidget(self.pplabel)
        self.pplist = QtWidgets.QWidget(evaDialog)
        self.pplist.setObjectName("pplist")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.pplist)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.players_list = QtWidgets.QListWidget(self.pplist)
        self.players_list.setObjectName("players_list")
        self.horizontalLayout_3.addWidget(self.players_list)
        self.points_list = QtWidgets.QListWidget(self.pplist)
        self.points_list.setObjectName("points_list")
        self.horizontalLayout_3.addWidget(self.points_list)
        self.list.addWidget(self.pplist)
        self.verticalLayout_2.addLayout(self.list)
        self.scoreButton = QtWidgets.QPushButton(evaDialog)
        self.scoreButton.setObjectName("scoreButton")
        self.scoreButton.clicked.connect(self.calculate)
        self.verticalLayout_2.addWidget(self.scoreButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.retranslateUi(evaDialog)
        self.teamselec.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(evaDialog)
        msg=QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Select team to generate its value\nand calculate results in matches against other teams")
        msg.setWindowTitle("Welcome")
        msg.exec_()

    def retranslateUi(self, evaDialog):
        _translate = QtCore.QCoreApplication.translate
        evaDialog.setWindowTitle(_translate("evaDialog", "EVALUATE Team"))
        self.selection_label.setText(_translate("evaDialog", "Evaluate the Performance of your Fantasy Team"))
        self.teamselec.setCurrentText(_translate("evaDialog", "Select Team"))
        self.teamselec.setItemText(0, _translate("evaDialog", "Select Team"))
        self.matchselec.setCurrentText(_translate("evaDialog", "Select Match"))
        self.matchselec.setItemText(0, _translate("evaDialog", "Select Match"))
        self.players_label.setText(_translate("evaDialog", "Players"))
        self.points_label.setText(_translate("evaDialog", "Points"))
        self.scoreButton.setText(_translate("evaDialog", "Calculate Score"))

    def batscore(self,p):
        if p.get('role')=='bat':
            r=int(p.get('runs'))
            s=r//2+(r//100)*10+((r%100)//50)*5
            try:
                sr=(r/int(p.get('balls')))*100
                if sr>=80 and sr<=100:
                    s=s+2
                elif sr>100:
                    s=s+4
            except:
                s+=0
            s=s+int(p.get('4'))+2*int(p.get('6'))
            return s
        else:
            return 0

    def bowlscore(self,p):
        if p.get('role')=='bowl':
            w=int(p.get('wkts'))
            s=10*w
            if w>=5:
                s=s+10
            elif w>=3 and w<5:
                s=s+5
            try:
                er=int(p.get('runs'))/int(p.get('overs'))
                if er<2:
                    s=s+10
                elif er>=2 and er<=3.5:
                    s=s+7
                elif er>3.5 and er<=4.5:
                    s=s+4
            except:
                s+=0
            s=s+10*int(p.get('field'))
            return s
        else:
            return 0

    def listsetup(self):
        if self.teamselec.currentText()!="Select Team":
            try:
                del self.opponent[self.teamselec.currentText()]
            except:
                None
            self.match={}
            self.matchselec.clear()
            self.matchselec.addItem("Select Match")
            self.players_list.clear()
            self.points_list.clear()
            if len(self.opponent)>0:
                i=1
                for j in self.opponent.keys():
                    self.matchselec.addItem("Match{}".format(i))
                    self.match["Match{}".format(i)]=j
                    i+=1
            else:
                msg=QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("No valid opponent team present")
                msg.setWindowTitle("Caution")
                msg.exec_()
            import sqlite3
            conn_list=sqlite3.connect('cricket.db')
            cur_list=conn_list.cursor()
            cur_list.execute("SELECT players from teams WHERE UPPER(name)=?;",(self.teamselec.currentText().upper(),))
            y=cur_list.fetchone()
            if y[0]!=None:
                points=0
                for i in y[0].split(','):
                    cur_list.execute("SELECT * from match where UPPER(player)=?;",(i.upper(),))
                    x=cur_list.fetchone()
                    bat={ 'role' : 'bat' , 'runs' :x[1], '4' :x[3], '6' :x[4], 'balls' :x[2]}
                    bwl={ 'role' : 'bowl' , 'wkts' :x[8], 'overs' :x[5], 'runs' :x[7], 'field' :x[9]+x[10]+x[11]}
                    score=self.batscore(bat)+self.bowlscore(bwl)
                    points+=score
                    item=QtWidgets.QListWidgetItem(i)
                    self.players_list.addItem(item)
                    item=QtWidgets.QListWidgetItem(str(score))
                    self.points_list.addItem(item)
                cur_list.execute("UPDATE teams SET value=? WHERE UPPER(name)=?;",(points,self.teamselec.currentText().upper(),))
                conn_list.commit()
                conn_list.close()
                self.opponent[self.teamselec.currentText()]=points
                self.points_value.setText("{}".format(points))
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("No players added to this team")
                msg.setWindowTitle("Failed")
                msg.exec_()

    def calculate(self):
        if self.teamselec.currentText()!="Select Team":
            if len(self.match)==0:
                msg=QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("No valid opponent team present")
                msg.setWindowTitle("Failed")
                msg.exec_()
            elif self.teamselec.currentText() not in self.opponent.keys():
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("No players added to this team")
                msg.setWindowTitle("Failed")
                msg.exec_()
            else:
                y=self.match[self.matchselec.currentText()]
                if self.opponent[y]<self.opponent[self.teamselec.currentText()]:
                    text="Opponent: {}  Opponent Score: {}\nYour Team Score: {}\nYou Win!".format(y,self.opponent[y],self.opponent[self.teamselec.currentText()])
                elif self.opponent[y]==self.opponent[self.teamselec.currentText()]:
                    text="Opponent: {}  Opponent Score: {}\nYour Team score: {}\nDraw!".format(y,self.opponent[y],self.opponent[self.teamselec.currentText()])
                else:
                    text="Opponent: {}  Opponent score: {}\nYour Team score: {}\nYou Lose!".format(y,self.opponent[y],self.opponent[self.teamselec.currentText()])
                msg=QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(text)
                msg.setWindowTitle("Success")
                msg.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("No team selected")
            msg.setWindowTitle("Failed")
            msg.exec_()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaDialog = QtWidgets.QDialog()
    ui = Ui_evaDialog()
    ui.setupUi(evaDialog)
    evaDialog.show()
    sys.exit(app.exec_())
