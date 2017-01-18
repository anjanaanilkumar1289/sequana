# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.resize(428, 369)
        Preferences.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(Preferences)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabs = QtWidgets.QTabWidget(Preferences)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setObjectName("tabs")
        self.tab_general = QtWidgets.QWidget()
        self.tab_general.setObjectName("tab_general")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_general)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tab_general)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.preferences_options_general_browser_value = QtWidgets.QComboBox(self.tab_general)
        self.preferences_options_general_browser_value.setObjectName("preferences_options_general_browser_value")
        self.preferences_options_general_browser_value.addItem("")
        self.preferences_options_general_browser_value.addItem("")
        self.preferences_options_general_browser_value.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.preferences_options_general_browser_value)
        self.label_3 = QtWidgets.QLabel(self.tab_general)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.preferences_options_general_logging_value = QtWidgets.QComboBox(self.tab_general)
        self.preferences_options_general_logging_value.setObjectName("preferences_options_general_logging_value")
        self.preferences_options_general_logging_value.addItem("")
        self.preferences_options_general_logging_value.addItem("")
        self.preferences_options_general_logging_value.addItem("")
        self.preferences_options_general_logging_value.addItem("")
        self.preferences_options_general_logging_value.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.preferences_options_general_logging_value)
        self.label_4 = QtWidgets.QLabel(self.tab_general)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.preferences_options_general_htmlpage_value = QtWidgets.QLineEdit(self.tab_general)
        self.preferences_options_general_htmlpage_value.setObjectName("preferences_options_general_htmlpage_value")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.preferences_options_general_htmlpage_value)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.tabs.addTab(self.tab_general, "")
        self.gridLayout_2.addWidget(self.tabs, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Preferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Preferences)
        self.tabs.setCurrentIndex(0)
        self.preferences_options_general_logging_value.setCurrentIndex(1)
        self.buttonBox.accepted.connect(Preferences.accept)
        self.buttonBox.rejected.connect(Preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(Preferences)
        Preferences.setTabOrder(self.tabs, self.preferences_options_general_browser_value)

    def retranslateUi(self, Preferences):
        _translate = QtCore.QCoreApplication.translate
        Preferences.setWindowTitle(_translate("Preferences", "Preferences"))
        self.label.setText(_translate("Preferences", "Select the browser to be used"))
        self.preferences_options_general_browser_value.setItemText(0, _translate("Preferences", "pyqt5"))
        self.preferences_options_general_browser_value.setItemText(1, _translate("Preferences", "firefox"))
        self.preferences_options_general_browser_value.setItemText(2, _translate("Preferences", "safari"))
        self.label_3.setText(_translate("Preferences", "Logging verbosity"))
        self.preferences_options_general_logging_value.setItemText(0, _translate("Preferences", "DEBUG"))
        self.preferences_options_general_logging_value.setItemText(1, _translate("Preferences", "INFO"))
        self.preferences_options_general_logging_value.setItemText(2, _translate("Preferences", "WARNING"))
        self.preferences_options_general_logging_value.setItemText(3, _translate("Preferences", "ERROR"))
        self.preferences_options_general_logging_value.setItemText(4, _translate("Preferences", "CRITICAL"))
        self.label_4.setText(_translate("Preferences", "HTML page to open as a report"))
        self.preferences_options_general_htmlpage_value.setText(_translate("Preferences", "multisummary.html"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_general), _translate("Preferences", "General"))
