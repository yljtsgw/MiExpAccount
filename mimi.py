# -*- coding: utf-8 -*-

"""
Module implementing mimi.
"""

from PyQt4.QtGui import QMainWindow,QApplication,QTableWidgetItem,QFileDialog,QMessageBox
from PyQt4.QtCore import pyqtSignature,QString
import time
from Ui_mimi import Ui_mimi,getTitleList
import excel

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
        self.excelfile = ''
        self.excelMethod = excel.excel()
    
    #@pyqtSignature("int, int")
    #def on_tableWidget_cellDoubleClicked(self, row, column):
        #"""
        #Slot documentation goes here.
        #"""
        ## TODO: not implemented yet
        ##raise NotImplementedError
        #pass
    
    
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
        删除选中行数据.
        """
        selectRow = self.tableWidget.currentRow()
        print selectRow
        self.tableWidget.removeRow(selectRow)
    
    @pyqtSignature("")
    def on_pushButton_output_clicked(self):    
        """
        导入EXCEL
        """
        bClear = False
        nrows = self.tableWidget.rowCount()   # 行总数 
        if nrows > 0:
            ret = QMessageBox.warning(self, 'WARNING', u'原表格中存在数据，请确认是否覆盖\n选是，将覆盖\n选否，会将导入内容添加至表格内', QMessageBox.Yes,QMessageBox.No,QMessageBox.Cancel )
            if ret == QMessageBox.Yes:
                QMessageBox.warning(self, '再次确认', u'点击确定将清除当前表格内容，再次确认是否删除', QMessageBox.Yes,QMessageBox.Cancel)
                bClear = True
                nrows = 0
            elif ret == QMessageBox.Cancel:
                return False
        if self.excelfile.strip() == '':
            lastPath = QString()
        else:
            lastPath = self.excelfile
        excelfile = QFileDialog.getOpenFileName(self, self.tr('Open xls'), lastPath,
                                                self.tr("xls Files(*.xls)"))        
        if excelfile =="" :
            return
        self.excelfile =  unicode(excelfile,'gbk')
        print self.excelfile            
        datalist = self.excelMethod.readFromXls(self.excelfile)
        if datalist == -1:
            QMessageBox.warning(self, u'读取失败', u'数据读取失败,请确认选择文件内容！！！', QMessageBox.Yes )
            return False
        
        
    @pyqtSignature("")
    def on_pushButton_output_clicked(self):
        """
        导出至EXCEL.
        """
        datalist = self.getTableDataList()
        if len(datalist) == 0:
            QMessageBox.warning(self, 'WARNING', u'当前列表为空，无需导出', QMessageBox.Yes )
            return False
        if self.excelfile.strip() == '':
            lastPath = QString()
        else:
            lastPath = self.excelfile
        excelfile = QFileDialog.getSaveFileName(self, self.tr('Save xls'), lastPath,
                                                self.tr("xls Files(*.xls)"))
        
        if excelfile =="" :
            return
        self.excelfile =  unicode(excelfile,'gbk')
        print self.excelfile
        try:
            self.excelMethod.writeToXls(self.excelfile, getTitleList(), datalist)       
        except Exception,e:
            print e 
            QMessageBox.warning(self, u'保存失败', u'请确认当前选择的EXCEL是否关闭\n保存失败！！！', QMessageBox.Yes )
    
    def getTableDataList(self):
        datalist = []
        nrows = self.tableWidget.rowCount()   # 行总数  
        ncols = self.tableWidget.columnCount()    # 列总数  
        for i in xrange(0,nrows):
            rowdatalist = []
            for j in xrange(0,ncols):
                data = unicode(self.tableWidget.item(i,j).text(),'gbk')
                rowdatalist.append(data)
            datalist.append(rowdatalist)
            print rowdatalist
        return datalist
    
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mimi = mimi()
    mimi.show()
    sys.exit(app.exec_())

