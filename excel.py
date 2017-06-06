# -*- coding: utf-8 -*-
import xlrd,xlwt

########################################################################
class excel:
    """
    读写excel的封装 针对03版本
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
    def readFromXls(self,xls_path,sheet_index = 0,sheet_name = ''):
        dataList = []
        try:
            book = xlrd.open_workbook(xls_path)
            sheet0 = book.sheet_by_index(sheet_index)
            # 获得行数和列数  
            nrows = sheet0.nrows    # 行总数  
            ncols = sheet0.ncols    # 列总数              
            for nrow in xrange(1,nrows):
                row_data = sheet0.row_values(nrow)
                if len(row_data ) == 0:
                    continue
                dataList.append(row_data)
        except Exception,e:
            print e
            dataList = -1
        return dataList      
    
    
    def writeToXls(self,xls_path,datalist,sheet_index = 0,sheet_name = '',write_mode = 0):
        """暂时只支持保存至新建表格"""
        
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)  
        sheet = book.add_sheet(sheet_name, cell_overwrite_ok=True)