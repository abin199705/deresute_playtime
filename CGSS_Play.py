# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:16:35 2021

@author: 阿濱
"""

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout ,QGroupBox
from PyQt5.QtCore import QTimer

class Ui_MainWindow(QWidget):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.resize(600, 400)
        self.time_label = QLabel()
        self.timeshow_label = QLabel()
        self.playtime_label = QLabel()
        self.playtimeshow_label = QLabel()
        self.fullcombo_label = QLabel()
        self.fullcomboshow_label = QLabel()
        
        
        self.playtimeshow_text = 0
        self.fullcomboshow_text = 0

        self.timekeep_Button = QPushButton()
        self.playtime_Button = QPushButton()
        self.fullcombo_Button = QPushButton()
        
  
        self.combine_1 = QHBoxLayout()
        self.combine_2 = QHBoxLayout()
        self.combine_3 = QHBoxLayout()
        self.combine_4 = QHBoxLayout()

        self.allwindow = QVBoxLayout()
        self.gridGroupBox1 = QGroupBox("")
        self.gridGroupBox2 = QGroupBox("")
        self.gridGroupBox3 = QGroupBox("")
        
        # QTimer
        self.timer = QTimer()

        # QPushButton
        self.playtime_Button.clicked.connect(self.timestart)
        self.timekeep_Button.clicked.connect(self.timekeep_clicked)

        # Other
        self.timer.timeout.connect(self.timestart)
        self.timeshow_text = 0
        
        
        self.layout_init()      
        self.signal_init()
        self.retranslateUi()

    def layout_init(self):
        
        self.combine_1.addWidget(self.time_label, 1)
        self.combine_1.addWidget(self.timeshow_label, 1)
        self.combine_1.addWidget(self.timekeep_Button, 1)   
        self.combine_2.addWidget(self.playtime_label, 1)
        self.combine_2.addWidget(self.playtimeshow_label, 1)
        self.combine_2.addWidget(self.playtime_Button, 1)          
        self.combine_3.addWidget(self.fullcombo_label, 1)   
        self.combine_3.addWidget(self.fullcomboshow_label, 1) 
        self.combine_3.addWidget(self.fullcombo_Button, 1)    
        
        self.gridGroupBox1.setLayout(self.combine_1)
        self.gridGroupBox2.setLayout(self.combine_2)
        self.gridGroupBox3.setLayout(self.combine_3)
        
        self.combine_4.addWidget(self.gridGroupBox2, 1)   
        self.combine_4.addWidget(self.gridGroupBox3, 1)  
                
        self.allwindow.addWidget(self.gridGroupBox1, 1)
        self.allwindow.addLayout(self.combine_4, 2)

    
        '''
        self.all_v_layout.setSizeConstraint(QVBoxLayout.SetFixedSize)
        '''
        self.setLayout(self.allwindow)
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("deresute_play")
        # self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.time_label.setText(_translate("MainWindow", "時間"))
        self.timeshow_label.setText(_translate("MainWindow", "00:00:00"))
        self.playtime_label.setText(_translate("MainWindow", "總次數"))
        self.playtimeshow_label.setText(_translate("MainWindow", "0"))
        self.fullcombo_label.setText(_translate("MainWindow", "FC次數"))
        self.fullcomboshow_label.setText(_translate("MainWindow", "0"))
        self.timekeep_Button.setText(_translate("MainWindow", "暫停"))
        self.playtime_Button.setText(_translate("MainWindow", "+1"))
        self.fullcombo_Button.setText(_translate("MainWindow", "+1"))


    def timekeep_clicked(self):
        self.timer.stop()

    def timestart(self):
        self.timer.start(100)
        self.timeshow_text += 1
        self.timeshow_label.setText(f'{self.timeshow_text}')
    
    def playtime_clicked(self):
        
        self.timestart()
        self.playtimeshow_text += 1
        self.playtimeshow_label.setText(f'{self.playtimeshow_text}')
    
    def fullcombo_clicked(self):
        
        self.playtime_clicked()
        #self.playtimeshow_text+=1
        #self.playtimeshow_label.setText(f'{self.playtimeshow_text}')
        self.fullcomboshow_text += 1
        self.fullcomboshow_label.setText(f'{self.fullcomboshow_text}')    
    
    def signal_init(self):
        self.timekeep_Button.clicked.connect(self.timekeep_clicked)
        self.playtime_Button.clicked.connect(self.playtime_clicked)
        self.fullcombo_Button.clicked.connect(self.fullcombo_clicked)   


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
