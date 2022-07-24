# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scaletool_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(394, 119)
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.combo_current_unit = QComboBox(MainWindow)
        self.combo_current_unit.setObjectName(u"combo_current_unit")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_current_unit.sizePolicy().hasHeightForWidth())
        self.combo_current_unit.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.combo_current_unit)


        self.horizontalLayout.addLayout(self.formLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_2 = QLabel(MainWindow)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.combo_target_unit = QComboBox(MainWindow)
        self.combo_target_unit.setObjectName(u"combo_target_unit")
        sizePolicy.setHeightForWidth(self.combo_target_unit.sizePolicy().hasHeightForWidth())
        self.combo_target_unit.setSizePolicy(sizePolicy)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.combo_target_unit)


        self.horizontalLayout.addLayout(self.formLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(MainWindow)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.spnbox_scale_mult = QDoubleSpinBox(MainWindow)
        self.spnbox_scale_mult.setObjectName(u"spnbox_scale_mult")
        sizePolicy.setHeightForWidth(self.spnbox_scale_mult.sizePolicy().hasHeightForWidth())
        self.spnbox_scale_mult.setSizePolicy(sizePolicy)
        self.spnbox_scale_mult.setValue(1.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spnbox_scale_mult)


        self.horizontalLayout_2.addLayout(self.formLayout)

        self.chkbox_reset_xform = QCheckBox(MainWindow)
        self.chkbox_reset_xform.setObjectName(u"chkbox_reset_xform")

        self.horizontalLayout_2.addWidget(self.chkbox_reset_xform)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.btn_perform_scale = QPushButton(MainWindow)
        self.btn_perform_scale.setObjectName(u"btn_perform_scale")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_perform_scale.sizePolicy().hasHeightForWidth())
        self.btn_perform_scale.setSizePolicy(sizePolicy1)
        self.btn_perform_scale.setMinimumSize(QSize(0, 35))

        self.verticalLayout.addWidget(self.btn_perform_scale)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Scale Tool", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current Unit:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Target Unit:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Scale Multiplier:", None))
        self.chkbox_reset_xform.setText(QCoreApplication.translate("MainWindow", u"Freeze Transform?", None))
        self.btn_perform_scale.setText(QCoreApplication.translate("MainWindow", u"Perform Scale", None))
    # retranslateUi

