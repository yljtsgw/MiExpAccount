# -*- coding: utf-8 -*-

"""
Module implementing mimi.
"""

from PyQt4.QtGui import QMainWindow,QApplication,QTableWidgetItem
from PyQt4.QtCore import pyqtSignature
import time
from Ui_mimi import Ui_mimi

class mimi(QMainWindow, Ui_mimi):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
    
    @pyqtSignature("int, int")
    def on_tableWidget_cellDoubleClicked(self, row, column):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        pass
    
    
    @pyqtSignature("")
    def on_pushButton_add_clicked(self):
        """
        Slot documentation goes here.
        """
        self.pushButton_add.setEnabled(False)
        checkMoneyTpyetext =  unicode(self.radioGroup_money.checkedButton().text(),'gbk')
        checkNametext =   unicode(self.radioGroup_name.checkedButton().text(),'gbk')
        inum = str(self.spinBox_num.text())
        fmoney = str(self.doubleSpinBox_money.text())
        tips = unicode(self.textEdit_tips.toPlainText(), 'gbk')
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        print checkMoneyTpyetext,checkNametext,inum,fmoney,tips,date
        currentRow = self.tableWidget.rowCount()        
        self.tableWidget.insertRow(currentRow)
        self.tableWidget.setItem(currentRow  ,0,QTableWidgetItem(checkMoneyTpyetext))
        self.tableWidget.setItem(currentRow  ,1,QTableWidgetItem(checkNametext))
        self.tableWidget.setItem(currentRow  ,2,QTableWidgetItem(fmoney))
        self.tableWidget.setItem(currentRow  ,3,QTableWidgetItem(inum))
        self.tableWidget.setItem(currentRow  ,4,QTableWidgetItem(tips))
        self.tableWidget.setItem(currentRow  ,5,QTableWidgetItem(date))
        self.pushButton_add.setEnabled(True)
        
    @pyqtSignature("")
    def on_pushButton_del_clicked(self):
        """
        Slot documentation goes here.
        """
        selectRow = self.tableWidget.currentRow()
        print selectRow
        self.tableWidget.removeRow(selectRow)
        
    @pyqtSignature("")
    def on_pushButton_output_clicked(self):
        """
        Slot documentation goes here.
        """
        
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mimi = mimi()
    mimi.show()
    sys.exit(app.exec_())

