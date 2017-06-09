# -*- coding: utf-8 -*-
import xlrd,xlwt,time

########################################################################
class excel:
    """
    读写excel的封装 针对03版本
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
    def set_style(self,name,height,bold=False):
        style = xlwt.XFStyle() # 初始化样式
    
        font = xlwt.Font() # 为样式创建字体
        font.name = name # 'Times New Roman'
        font.bold = bold
        font.color_index = 4
        font.height = height
    
        # borders= xlwt.Borders()
        # borders.left= 6
        # borders.right= 6
        # borders.top= 6
        # borders.bottom= 6
    
        style.font = font
        # style.borders = borders
    
        return style        

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
    
    
    def writeToXls(self,xls_path,title_list,data_list,sheet_name = '',sheet_index = 0,write_mode = 0):
        """暂时只支持保存至新建表格"""
    
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)  
        if len(sheet_name) == 0:
            sheet_name = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        sheet = book.add_sheet(sheet_name, cell_overwrite_ok=True)
        for i in xrange(0,len(title_list)):
            sheet.write(0 ,i,title_list[i],self.set_style('Times New Roman',220,True))
        for row in xrange(0,len(data_list)):
            for col in xrange(0,len(data_list[row])):
                sheet.write(row+1,col,data_list[row][col],self.set_style('Times New Roman',220 ))
                print data_list[row][col]
                currentWidth = 260 * len(data_list[row][col])* 2
                print 'currentWidth:', currentWidth
                if sheet.col(col).width < currentWidth:
                    sheet.col(col).width = currentWidth
                print 'sheet.col(col).width:' ,sheet.col(col).width
        book.save(xls_path) #保存文件
        
        
if __name__ == '__main__':
    xls_name = u'测试.xls'
    titlelist = [u'我说呢','123','abc','333','555']
    #datalist = [['aaa',u'测试',111,'第2行','aaa'],['bbb',u'测试2',222,'第3行','aaa']]
    xlsc = excel()
    #xlsc.writeToXls(xls_name,titlelist,datalist,u'我自己建的')
    datalist = xlsc.readFromXls(xls_name)
    print datalist