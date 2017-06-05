# -*- coding: gbk -*-
import ConfigParser,re

cf = ConfigParser.ConfigParser()
configFile = 'config.ini'

def getConfig(option):
    data = ''
    try:
        cf.read(configFile)
        data = cf.get('config', option)
        data = unicode(data,'gbk')
    except:
        data = ''
    return data

def getTemp(option):
    data = ''
    try:
        cf.read(configFile)
        data = cf.get('TEMP', option)
        data = unicode(data,'gbk')
    except:
        data = ''
    return data

def saveTemp(option,value):
    cf.read(configFile)
    section = 'TEMP'
    cf.set(section, option,unicode(value).encode('gbk'))
    cf.write(open(configFile,'w')) 
    
    
def getConfigToList(option):
    data=[]
    try:
        strdata = getConfig(option)
        if len(strdata) != 0:
            strdata = strdata.replace(u'，', ',')
            datalist = strdata.split(',')
            if len(datalist) != 0:
                return datalist
        return -1
    except Excepiton, e:
        print e
        return  -1
            