# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yeison/Documentos/Desarrollo/Pinguino/GitHub/pinguino-ide/qtgui/frames/library_template.ui'
#
# Created: Fri Oct  2 14:51:15 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LibraryTemplate(object):
    def setupUi(self, LibraryTemplate):
        LibraryTemplate.setObjectName("LibraryTemplate")
        LibraryTemplate.resize(518, 276)
        self.gridLayout = QtGui.QGridLayout(LibraryTemplate)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_cancel = QtGui.QPushButton(LibraryTemplate)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtGui.QLabel(LibraryTemplate)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_lib_author = QtGui.QLineEdit(LibraryTemplate)
        self.lineEdit_lib_author.setObjectName("lineEdit_lib_author")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_lib_author)
        self.label_4 = QtGui.QLabel(LibraryTemplate)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_lib_path = QtGui.QLineEdit(LibraryTemplate)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_lib_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_lib_path.setSizePolicy(sizePolicy)
        self.lineEdit_lib_path.setReadOnly(True)
        self.lineEdit_lib_path.setObjectName("lineEdit_lib_path")
        self.horizontalLayout_3.addWidget(self.lineEdit_lib_path)
        self.pushButton_lib_path = QtGui.QPushButton(LibraryTemplate)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_lib_path.sizePolicy().hasHeightForWidth())
        self.pushButton_lib_path.setSizePolicy(sizePolicy)
        self.pushButton_lib_path.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_lib_path.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_lib_path.setObjectName("pushButton_lib_path")
        self.horizontalLayout_3.addWidget(self.pushButton_lib_path)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label = QtGui.QLabel(LibraryTemplate)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_lib_name = QtGui.QLineEdit(LibraryTemplate)
        self.lineEdit_lib_name.setObjectName("lineEdit_lib_name")
        self.horizontalLayout_2.addWidget(self.lineEdit_lib_name)
        self.checkBox_lib8 = QtGui.QCheckBox(LibraryTemplate)
        self.checkBox_lib8.setChecked(True)
        self.checkBox_lib8.setObjectName("checkBox_lib8")
        self.horizontalLayout_2.addWidget(self.checkBox_lib8)
        self.checkBox_lib32 = QtGui.QCheckBox(LibraryTemplate)
        self.checkBox_lib32.setObjectName("checkBox_lib32")
        self.horizontalLayout_2.addWidget(self.checkBox_lib32)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_3 = QtGui.QLabel(LibraryTemplate)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.plainTextEdit_lib_description = QtGui.QPlainTextEdit(LibraryTemplate)
        self.plainTextEdit_lib_description.setObjectName("plainTextEdit_lib_description")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.plainTextEdit_lib_description)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 4)
        self.pushButton_accept = QtGui.QPushButton(LibraryTemplate)
        self.pushButton_accept.setEnabled(False)
        self.pushButton_accept.setObjectName("pushButton_accept")
        self.gridLayout.addWidget(self.pushButton_accept, 1, 2, 1, 1)

        self.retranslateUi(LibraryTemplate)
        QtCore.QMetaObject.connectSlotsByName(LibraryTemplate)

    def retranslateUi(self, LibraryTemplate):
        LibraryTemplate.setWindowTitle(QtGui.QApplication.translate("LibraryTemplate", "Library Template", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cancel.setText(QtGui.QApplication.translate("LibraryTemplate", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("LibraryTemplate", "Author:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("LibraryTemplate", "Create in (*):", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_lib_path.setText(QtGui.QApplication.translate("LibraryTemplate", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LibraryTemplate", "Library name (*):", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_lib8.setText(QtGui.QApplication.translate("LibraryTemplate", "8bit", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_lib32.setText(QtGui.QApplication.translate("LibraryTemplate", "32bit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("LibraryTemplate", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_accept.setText(QtGui.QApplication.translate("LibraryTemplate", "Continue", None, QtGui.QApplication.UnicodeUTF8))

