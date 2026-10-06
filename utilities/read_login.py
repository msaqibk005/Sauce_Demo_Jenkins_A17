

from xlrd import *

def get_test1_data():
    wb = open_workbook("test_data/SauceDemo.xlsx")
    exc = wb.sheet_by_name("Sheet1")

    rows = exc.row_values(1)
    testcase = rows[0]
    username = rows[1]
    password = rows[2]

    return testcase,username,password


#______________________________________________________________________________________________________________________



data = []

def get_test2_data():
    wb = open_workbook("test_data/SauceDemo.xlsx")
    exc = wb.sheet_by_name('Sheet1')

    for i in range(2,exc.nrows):
        rows = exc.row_values(i)
        testcase = rows[0]
        username = rows[1]
        password = rows[2]

        data.append((testcase,username,password))          # storing in tuple ()
    return data


#_______________________________________________________________________________________________________________________



def get_test3_data():
    wb = open_workbook("test_data/SauceDemo.xlsx")
    exc = wb.sheet_by_name('Sheet2')
    rows = exc.row_values(1)
    testcase = rows[0]
    f_name = rows[1]
    l_name = rows[2]
    zipcode = rows[3]

    return testcase,f_name,l_name,zipcode



#_______________________________________________________________________________________________________________________


data_2 = []

def get_test4_data():
    wb = open_workbook("test_data/SauceDemo.xlsx")
    exc = wb.sheet_by_name('Sheet2')

    for i in range(2,exc.nrows):
        rows = exc.row_values(i)
        testcase = rows[0]
        f_name = rows[1]
        l_name = rows[2]
        zipcode = rows[3]

        data_2.append((testcase,f_name,l_name,zipcode))

    return data_2





















