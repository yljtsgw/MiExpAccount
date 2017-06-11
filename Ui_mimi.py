# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\workspace\MIMI\mimi.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import config


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def getMoneyTypeList():
    moneylist = config.getConfigToList('moneytype')
    if moneylist == -1 :
        moneylist = []
    return moneylist

def getNameList():    
    namelist = config.getConfigToList('names')
    if namelist == -1 :
        namelist = []
    return namelist

def getTitleList():
    titlelist = config.getConfigToList('titles')
    if titlelist == -1 :
        titlelist = []
    return titlelist

class Ui_mimi(object):
   

        
    def setupUi(self, mimi):
        QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName('gbk'))
        mimi.setObjectName(_fromUtf8("mimi"))
        mimi.resize(999, 839)
        icon = QtGui.QIcon()
        QtGui.QPixmap
        try:            
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("./mi.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            icon.addPixmap(QtGui.QPixmap(_fromUtf8("./mi.ico")), QtGui.QIcon.Normal, QtGui.QIcon.On)
            mimi.setWindowIcon(icon)
            print " get the ico"
        except Exception, e:
            print e        
        self.centralwidget = QtGui.QWidget(mimi)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox_money = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_money.setGeometry(QtCore.QRect(40, 30, 251, 751))
        self.groupBox_money.setObjectName(_fromUtf8("groupBox_money"))
        self.widget = QtGui.QWidget(self.groupBox_money)
        self.widget.setGeometry(QtCore.QRect(30, 40, 37, 47))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.splitter = QtGui.QSplitter(self.groupBox_money)
        self.splitter.setGeometry(QtCore.QRect(7, 20, 241, 701))
        self.splitter.setMinimumSize(QtCore.QSize(241, 441))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        #self.radioButton_2 = QtGui.QRadioButton(self.widget)
        #self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        #self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.radioGroup_money = QtGui.QButtonGroup(self.groupBox_money) 
        self.moneylist = getMoneyTypeList()
        count = 0
        for moneytype in self.moneylist:
            try:
                exec('self.radioButtonM_%d = QtGui.QRadioButton(self.splitter)'%count)
                exec('self.radioButtonM_%d.setObjectName(_fromUtf8("radioButtonM_%d"))'%(count,count))
                exec('self.radioButtonM_%d.setMinimumSize(QtCore.QSize(180, 20))'%count)                
                exec('self.radioGroup_money.addButton(self.radioButtonM_%d)'%(count))
                exec('self.radioButtonM_%d.setText(_translate("mimi", "%s", None))'%(count,moneytype))     
            except Exception,e:
                print e
            count = count +1  
        self.radioButtonM_0.setChecked(True)
        self.groupBox_name = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_name.setGeometry(QtCore.QRect(310, 30, 201, 261))
        self.groupBox_name.setObjectName(_fromUtf8("groupBox_name"))
        self.widget1 = QtGui.QWidget(self.groupBox_name)
        self.widget1.setGeometry(QtCore.QRect(20, 40, 117, 47))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.splitter_2 = QtGui.QSplitter(self.groupBox_name)
        self.splitter_2.setGeometry(QtCore.QRect(10, 30, 181, 221))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))        
        self.radioGroup_name = QtGui.QButtonGroup(self.groupBox_name) 
        self.namelist = getNameList()
        count = 0
        for name in self.namelist:
            try:
                exec('self.radioButton_%d = QtGui.QRadioButton(self.splitter_2)'%count)
                exec('self.radioButton_%d.setObjectName(_fromUtf8("radioButton_%d"))'%(count,count))
                exec('self.radioButton_%d.setMinimumSize(QtCore.QSize(180, 20))'%count)   
                exec('self.radioGroup_name.addButton(self.radioButton_%d)'%(count))
                exec('self.radioButton_%d.setText(_translate("mimi", "%s", None))'%(count,name))                
            except Exception,e:
                print e
            count = count +1        
        self.radioButton_0.setChecked(True)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 50, 71, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 180, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit_tips = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_tips.setGeometry(QtCore.QRect(530, 210, 411, 81))
        self.textEdit_tips.setObjectName(_fromUtf8("textEdit_tips"))
        
        self.titlelist = getTitleList()
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(330, 370, 611, 371))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))        
        self.tableWidget.setColumnCount(len(self.titlelist))
        self.tableWidget.setRowCount(0)        
        for i in xrange(0,len(self.titlelist)):
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)        
            
        self.pushButton_add = QtGui.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(790, 300, 121, 51))
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.pushButton_del = QtGui.QPushButton(self.centralwidget)
        self.pushButton_del.setGeometry(QtCore.QRect(390, 770, 93, 28))
        self.pushButton_del.setObjectName(_fromUtf8("pushButton_del"))
        self.pushButton_output = QtGui.QPushButton(self.centralwidget)
        self.pushButton_output.setGeometry(QtCore.QRect(850, 770, 93, 28))
        self.pushButton_output.setObjectName(_fromUtf8("pushButton_output"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 100, 72, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.doubleSpinBox_money = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_money.setGeometry(QtCore.QRect(610, 100, 111, 22))
        self.doubleSpinBox_money.setMaximum(99999.99)
        self.doubleSpinBox_money.setObjectName(_fromUtf8("doubleSpinBox_money"))
        self.spinBox_num = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_num.setGeometry(QtCore.QRect(610, 50, 111, 22))
        self.spinBox_num.setMinimum(1)
        self.spinBox_num.setMaximum(9999)
        self.pushButton_input = QtGui.QPushButton(self.centralwidget)
        self.pushButton_input.setGeometry(QtCore.QRect(720, 770, 93, 28))
        self.pushButton_input.setObjectName(_fromUtf8("pushButton_input"))       
        mimi.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mimi)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mimi.setStatusBar(self.statusbar)

        self.retranslateUi(mimi)
        QtCore.QMetaObject.connectSlotsByName(mimi)

    def retranslateUi(self, mimi):
        mimi.setWindowTitle(_translate("MiExpAccount", "MiExpAccount", None))
        self.groupBox_money.setTitle(_translate("mimi", "费用分类", None))
        self.groupBox_name.setTitle(_translate("mimi", "报销人员", None))
        self.label.setText(_translate("mimi", "附件个数：", None))
        self.label_2.setText(_translate("mimi", "备注：", None))
        
        for i in xrange(0,len(self.titlelist)):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("mimi", self.titlelist[i], None))            
        self.pushButton_add.setText(_translate("mimi", "添加", None))
        self.pushButton_del.setText(_translate("mimi", "删除", None))
        self.pushButton_output.setText(_translate("mimi", "导出xls", None))
        self.label_3.setText(_translate("mimi", "money:", None))
        self.pushButton_input.setText(_translate("mimi", "导入xls", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mimi = QtGui.QMainWindow()
    ui = Ui_mimi()
    ui.setupUi(mimi)
    mimi.show()
    sys.exit(app.exec_())

