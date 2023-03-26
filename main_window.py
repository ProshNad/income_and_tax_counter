# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QHeaderView, QTableWidgetItem
from main import count_all, convert_to_num


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 472)
        MainWindow.setWindowIcon(QtGui.QIcon('icon_profile.png.'))
        MainWindow.setStyleSheet("background-color: white;\n"
"QTableWidget{\n"
"\n"
"background-color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"\n"
"border-radius: 20px;  \n"
"    background-color: rgb(255, 238, 251);;\n"
"   font-size: 15pt;\n"
"    font-weight: bold;\n"
"   color:  rgb(208, 90, 151);\n"
"    width:  40px;  \n"
"    height: 40px;       \n"
"    border-width: 0px;\n"
"    border-style: solid;  \n"
"    border-color:white;\n"
"}\n"
" \n"
" QPushButton:hover  {\n"
"    background-color: #dbeaff;;\n"
"border-radius: 15px;    \n"
"border-color: rgb(182, 89, 129);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #F9D8D4;\n"
"border-radius: 15px;    \n"
"} ")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 11, 6, 1, 2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"border-width: 0px;\n"
"    border-style: solid;  \n"
"    border-color: rgb(182, 89, 129);\n"
"}\n"
"QHeaderView::section {\n"
"    background-color:  rgb(255, 226, 240);\n"
"    padding: 4px;\n"
"    border: 0px;\n"
"}")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(99, 0, 99))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(99, 0, 99))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        brush = QtGui.QBrush(QtGui.QColor(99, 0, 99))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 3, 3, 7, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"\n"
"border-radius: 20px;  \n"
"    background-color: rgb(255, 238, 251);;\n"
"   font-size: 20pt;\n"
"\n"
"    font-weight: bold;\n"
"   color: rgb(208, 90, 151);\n"
"    width:  40px;  \n"
"    height: 40px;       \n"
"    border-width: 0px;\n"
"    border-style: solid;  \n"
"    border-color:white;\n"
"}\n"
" \n"
" QPushButton:hover  {\n"
"    background-color: #dbeaff;;\n"
"border-radius: 15px;    \n"
"border-color: rgb(182, 89, 129);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #F9D8D4;\n"
"border-radius: 15px;    \n"
"} ")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 1, 1, 2)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(14)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tableWidget_2.setStyleSheet("QTableWidget{\n"
"border-width: 0px;\n"
"    border-style: solid;  \n"
"    border-color: rgb(182, 89, 129);\n"
"}\n"
"QHeaderView::section {\n"
"    background-color:  rgb(255, 226, 240);\n"
"    padding: 4px;\n"
"    border: 0px;\n"
"}")
        self.tableWidget_2.setWordWrap(True)
        self.tableWidget_2.setRowCount(7)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(99, 0, 99))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(99, 0, 99))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(99, 0, 99))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(99, 0, 99))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item.setForeground(brush)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(30)
        self.gridLayout.addWidget(self.tableWidget_2, 3, 7, 7, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Quicksand SemiBold")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet("QLabel {\n"
"    color: rgb(208, 90, 151);\n"
"     border-width: 0px;\n"
"}    ")
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"\n"
"border-radius: 20px;  \n"
"    background-color: rgb(255, 238, 251);;\n"
"   font-size: 20pt;\n"
"\n"
"    font-weight: bold;\n"
"   color:rgb(208, 90, 151);\n"
"    width:  40px;  \n"
"    height: 40px;       \n"
"    border-width: 0px;\n"
"    border-style: solid;  \n"
"    border-color:white;\n"
"}\n"
" \n"
" QPushButton:hover  {\n"
"    background-color: #dbeaff;;\n"
"border-radius: 15px;    \n"
"border-color: rgb(182, 89, 129);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #F9D8D4;\n"
"border-radius: 15px;    \n"
"} ")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: rgb(208, 90, 151);\n"
"     border-width: 0px;\n"
"}    ")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 5)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def onClick_MinusRow(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.removeRow(rowPosition-1)
        rowPositionTab2 = self.tableWidget_2.rowCount()
        self.tableWidget_2.removeRow(rowPositionTab2-1)

    def onClick_PlusRow(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        rowPositionTab2 = self.tableWidget_2.rowCount()
        self.tableWidget_2.insertRow(rowPositionTab2)

    def onClick_Count(self):
        row_num = self.tableWidget.rowCount()
        for row in range(row_num):
            name = self.tableWidget.item(row, 0)
            hours = self.tableWidget.item(row, 1)
            rate = self.tableWidget.item(row, 2)
            if (name and hours and rate):
                income, tax, superd = count_all(convert_to_num(hours.text()), convert_to_num(rate.text()))
                self.tableWidget_2.setItem(row, 0, QTableWidgetItem(name.text()))
                self.tableWidget_2.setItem(row, 1, QTableWidgetItem(str(income)))
                self.tableWidget_2.setItem(row, 2, QTableWidgetItem(str(tax)))
                self.tableWidget_2.setItem(row, 3, QTableWidgetItem(str(superd)))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Assessment 1"))
        self.pushButton_3.setText(_translate("MainWindow", "Count"))
        self.pushButton_3.clicked.connect(self.onClick_Count)
        self.tableWidget.setSortingEnabled(False)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

        header = self.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)

        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Employee Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Hours Worked"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Hourly Rate"))
        self.pushButton_2.setText(_translate("MainWindow", "-"))
        self.pushButton_2.clicked.connect(self.onClick_MinusRow)
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Employee Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Income"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Superannuation Deduction"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Income Tax Deduction"))
        self.label.setText(_translate("MainWindow", "Tax and income accountant"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton.clicked.connect(self.onClick_PlusRow)
        self.label_2.setText(_translate("MainWindow", "Assessment 1 for TECH1200. Developed by student 1817276 - Nadia Proshutina."))
        self.actionAbout.setText(_translate("MainWindow", "About"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())