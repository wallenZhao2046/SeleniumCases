#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import codecs
import xlrd

login_text = '登录'

class X1UserInfo(object):
    def __init__(self, path=''):
        self.x1 = xlrd.open_workbook(path)

    def get_sheet_info(self):
        listkey = ['uname', 'pwd']
        infolist = []
        for row in range(self.sheet.nrows):
            info = self.sheet.row_values(row)
            tmp = zip(listkey, info)
            infolist.append(dict(tmp))
        return infolist
    def get_sheetinfo_by_name(self, name):
        selft.sheet = self.x1.sheet_by_name(name)
        return self.get_sheet_info()
    def get_sheetinfo_by_index(selft, index):
        self.sheet = self.x1.sheet_by_inde(index)
        return self.get_sheet_info()        

def openBrowser():
    d = webdriver.Chrome()
    return d

def openUrl(d, url):
    d.get(url)
    d.maximize_window()

def get_ele_times(driver, times, func):
    return WebDriverWait(driver, times).until(func)

def findElement(d, ele_dict):
    '''
        input: text_id, userid, pwdid, loginid
        return userEle, pwdEle, loginEle
    '''

    ele_login = get_ele_times(d, 10, lambda d : d.find_element_by_link_text(ele_dict['text_id']) )
    ele_login.click()
    userEle = d.find_element_by_id(ele_dict['userid'])
    pwdEle = d.find_element_by_id(ele_dict['pwdid'])
    loginEle = d.find_element_by_id(ele_dict['loginid'])

    # for find_mth in ele_dict:
    #     print "find_mth is %s"%find_mth
    #     command = "driver." + fine_math + "(" + ele_dict[find_mth] + ")" 
    #     print "command: %s" %command
    #     ele = exec(command)
    #     elements.append(ele)
    return userEle, pwdEle, loginEle

def sendValues(ele_tuple, account_dict):
    '''
    ele tuple
    account : uname, pwd
    '''
    listkey = ['uname', 'pwd']
    i = 0
    for key in listkey:
        ele_tuple[i].clear()
        ele_tuple[i].send_keys(account_dict[key])
        i += 1
    ele_tuple[2].click()



def login_test():
    url = 'http://www.maiziedu.com'
    ele_dict = {
        "text_id" : login_text,
        "userid" : "id_account_l",
        "pwdid" : "id_password_l",
        "loginid" : "login_btn"
    }

    account_dict = {
        'uname' : 'aaa',
        'pwd' : 'wrong pwd'
    }

    print 'begin to open browser'
    d = openBrowser()
    print 'begin to open url.'
    openUrl(d, url)
    print 'open Url done.'

    ele_tuple = findElement(d, ele_dict)
   
    sendValues(ele_tuple, account_dict)
    checkResult(d, '该账户格式不正确')
    d.close()

if __name__ == '__main__':
    print 'begin testing ...'
    login_test()
    print 'end testing .'