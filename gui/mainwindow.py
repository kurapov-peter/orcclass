# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 758)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.gridStackedWidget.setObjectName("gridStackedWidget")
        self.pageQuestions = QtWidgets.QWidget()
        self.pageQuestions.setObjectName("pageQuestions")
        self.gridLayout = QtWidgets.QGridLayout(self.pageQuestions)
        self.gridLayout.setObjectName("gridLayout")
        self.root_layout = QtWidgets.QGridLayout()
        self.root_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.root_layout.setContentsMargins(5, 5, 5, 5)
        self.root_layout.setObjectName("root_layout")
        self.alternative = QtWidgets.QListWidget(self.pageQuestions)
        self.alternative.setMinimumSize(QtCore.QSize(600, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.alternative.setFont(font)
        self.alternative.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.alternative.setAlternatingRowColors(True)
        self.alternative.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.alternative.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.alternative.setProperty("isWrapping", False)
        self.alternative.setWordWrap(True)
        self.alternative.setObjectName("alternative")
        self.root_layout.addWidget(self.alternative, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.pageQuestions)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.root_layout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.pageQuestions)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.root_layout.addWidget(self.label_2, 3, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.pageQuestions)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.root_layout.addWidget(self.progressBar, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.badClass = QtWidgets.QPushButton(self.pageQuestions)
        self.badClass.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.badClass.setFont(font)
        self.badClass.setObjectName("badClass")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.badClass)
        self.horizontalLayout.addWidget(self.badClass)
        self.goodClass = QtWidgets.QPushButton(self.pageQuestions)
        self.goodClass.setMinimumSize(QtCore.QSize(200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.goodClass.setFont(font)
        self.goodClass.setObjectName("goodClass")
        self.buttonGroup.addButton(self.goodClass)
        self.horizontalLayout.addWidget(self.goodClass)
        self.root_layout.addLayout(self.horizontalLayout, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.root_layout, 0, 0, 1, 1)
        self.gridStackedWidget.addWidget(self.pageQuestions)
        self.pageResult = QtWidgets.QWidget()
        self.pageResult.setObjectName("pageResult")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.pageResult)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.root_layout_2 = QtWidgets.QGridLayout()
        self.root_layout_2.setObjectName("root_layout_2")
        self.label_8 = QtWidgets.QLabel(self.pageResult)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.root_layout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.question_number_layout_2 = QtWidgets.QHBoxLayout()
        self.question_number_layout_2.setContentsMargins(6, 6, 6, 6)
        self.question_number_layout_2.setObjectName("question_number_layout_2")
        self.label_9 = QtWidgets.QLabel(self.pageResult)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.question_number_layout_2.addWidget(self.label_9)
        self.number_of_questions_2 = QtWidgets.QLabel(self.pageResult)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.number_of_questions_2.setFont(font)
        self.number_of_questions_2.setObjectName("number_of_questions_2")
        self.question_number_layout_2.addWidget(self.number_of_questions_2)
        self.root_layout_2.addLayout(self.question_number_layout_2, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.pageResult)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.root_layout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.result_container_2 = QtWidgets.QHBoxLayout()
        self.result_container_2.setObjectName("result_container_2")
        self.ineffective_container_2 = QtWidgets.QVBoxLayout()
        self.ineffective_container_2.setContentsMargins(6, 6, 6, 6)
        self.ineffective_container_2.setObjectName("ineffective_container_2")
        self.label_11 = QtWidgets.QLabel(self.pageResult)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.ineffective_container_2.addWidget(self.label_11)
        self.ineffective_text_2 = QtWidgets.QPlainTextEdit(self.pageResult)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ineffective_text_2.setFont(font)
        self.ineffective_text_2.setObjectName("ineffective_text_2")
        self.ineffective_container_2.addWidget(self.ineffective_text_2)
        self.result_container_2.addLayout(self.ineffective_container_2)
        self.effective_container_2 = QtWidgets.QVBoxLayout()
        self.effective_container_2.setContentsMargins(6, 6, 6, 6)
        self.effective_container_2.setObjectName("effective_container_2")
        self.label_12 = QtWidgets.QLabel(self.pageResult)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.effective_container_2.addWidget(self.label_12)
        self.effective_text_2 = QtWidgets.QPlainTextEdit(self.pageResult)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.effective_text_2.setFont(font)
        self.effective_text_2.setObjectName("effective_text_2")
        self.effective_container_2.addWidget(self.effective_text_2)
        self.result_container_2.addLayout(self.effective_container_2)
        self.root_layout_2.addLayout(self.result_container_2, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.root_layout_2, 0, 0, 1, 1)
        self.gridStackedWidget.addWidget(self.pageResult)
        self.gridLayout_3.addWidget(self.gridStackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menuMenu.addAction(self.actionexit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.gridStackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Оцените следующую альтернативу:"))
        self.label_2.setText(_translate("MainWindow", "Выберите класс для данной альтернативы:"))
        self.badClass.setText(_translate("MainWindow", "Неэффективная деятельнось"))
        self.goodClass.setText(_translate("MainWindow", "Эффективная деятельнось"))
        self.label_8.setText(_translate("MainWindow", "Классификация построена успешно!"))
        self.label_9.setText(_translate("MainWindow", "Число заданных вопросов:"))
        self.number_of_questions_2.setText(_translate("MainWindow", "-123456789"))
        self.label_10.setText(_translate("MainWindow", "Были построены следующие решающие правила:"))
        self.label_11.setText(_translate("MainWindow", "Верхняя граница неэффективного класса"))
        self.label_12.setText(_translate("MainWindow", "Нижняя граница эффективного класса"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionexit.setText(_translate("MainWindow", "exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
