# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1200, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ComboBoxFeed = QtWidgets.QComboBox(self.centralwidget)
        self.ComboBoxFeed.setGeometry(QtCore.QRect(60, 10, 440, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ComboBoxFeed.setFont(font)
        self.ComboBoxFeed.setEditable(False)
        self.ComboBoxFeed.setObjectName("ComboBoxFeed")
        self.ButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonAdd.setGeometry(QtCore.QRect(10, 10, 40, 40))
        self.ButtonAdd.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonAdd.setIcon(icon)
        self.ButtonAdd.setObjectName("ButtonAdd")
        self.ButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSearch.setGeometry(QtCore.QRect(900, 10, 40, 40))
        self.ButtonSearch.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("data/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonSearch.setIcon(icon1)
        self.ButtonSearch.setObjectName("ButtonSearch")
        self.EntrySearch = QtWidgets.QLineEdit(self.centralwidget)
        self.EntrySearch.setGeometry(QtCore.QRect(950, 10, 240, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.EntrySearch.setFont(font)
        self.EntrySearch.setObjectName("EntrySearch")
        self.ListWidgetTitle = QtWidgets.QListWidget(self.centralwidget)
        self.ListWidgetTitle.setGeometry(QtCore.QRect(10, 90, 741, 280))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.ListWidgetTitle.setFont(font)
        self.ListWidgetTitle.setStyleSheet("")
        self.ListWidgetTitle.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ListWidgetTitle.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ListWidgetTitle.setObjectName("ListWidgetTitle")
        self.ListWidgetCategory = QtWidgets.QListWidget(self.centralwidget)
        self.ListWidgetCategory.setGeometry(QtCore.QRect(750, 90, 240, 280))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.ListWidgetCategory.setFont(font)
        self.ListWidgetCategory.setStyleSheet("")
        self.ListWidgetCategory.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ListWidgetCategory.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ListWidgetCategory.setObjectName("ListWidgetCategory")
        self.ListWidgetDate = QtWidgets.QListWidget(self.centralwidget)
        self.ListWidgetDate.setGeometry(QtCore.QRect(989, 90, 200, 280))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.ListWidgetDate.setFont(font)
        self.ListWidgetDate.setStyleSheet("")
        self.ListWidgetDate.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ListWidgetDate.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ListWidgetDate.setObjectName("ListWidgetDate")
        self.TextEditContent = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEditContent.setGeometry(QtCore.QRect(10, 430, 1180, 210))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TextEditContent.setFont(font)
        self.TextEditContent.setUndoRedoEnabled(False)
        self.TextEditContent.setReadOnly(True)
        self.TextEditContent.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.TextEditContent.setObjectName("TextEditContent")
        self.ComboBoxCategory = QtWidgets.QComboBox(self.centralwidget)
        self.ComboBoxCategory.setGeometry(QtCore.QRect(750, 60, 239, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.ComboBoxCategory.setFont(font)
        self.ComboBoxCategory.setStyleSheet("border: 1px solid black;\n"
"padding: 0 8px;\n"
"background: rgb(221, 221, 221)\n"
"")
        self.ComboBoxCategory.setObjectName("ComboBoxCategory")
        self.LabelDate = QtWidgets.QLabel(self.centralwidget)
        self.LabelDate.setGeometry(QtCore.QRect(989, 60, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.LabelDate.setFont(font)
        self.LabelDate.setStyleSheet("border: 1px solid black;\n"
"padding: 0 8px;\n"
"background: rgb(221, 221, 221)\n"
"")
        self.LabelDate.setObjectName("LabelDate")
        self.LabelTitle = QtWidgets.QLabel(self.centralwidget)
        self.LabelTitle.setGeometry(QtCore.QRect(10, 60, 741, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelTitle.sizePolicy().hasHeightForWidth())
        self.LabelTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.LabelTitle.setFont(font)
        self.LabelTitle.setStyleSheet("border: 1px solid black;\n"
"padding: 0 8px;\n"
"background: rgb(221, 221, 221)\n"
"")
        self.LabelTitle.setObjectName("LabelTitle")
        self.LabelTitle_2 = QtWidgets.QLabel(self.centralwidget)
        self.LabelTitle_2.setGeometry(QtCore.QRect(10, 380, 1181, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LabelTitle_2.sizePolicy().hasHeightForWidth())
        self.LabelTitle_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LabelTitle_2.setFont(font)
        self.LabelTitle_2.setStyleSheet("border: 1px solid black;\n"
"padding: 0 8px;\n"
"background: rgb(221, 221, 221)\n"
"")
        self.LabelTitle_2.setText("")
        self.LabelTitle_2.setObjectName("LabelTitle_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSS Feed Reader"))
        self.LabelDate.setText(_translate("MainWindow", "Published"))
        self.LabelTitle.setText(_translate("MainWindow", "Title"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

