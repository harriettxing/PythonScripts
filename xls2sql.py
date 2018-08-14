# Generate sql insert statement for a sheet in Excel

import openpyxl
import sys

#python.exe xls2sql.py InputExcelFileName.xlsx SheetName OutputDBTableName TableID
#print(str(sys.argv))

#print("xls2sql.py")

book = openpyxl.load_workbook(sys.argv[1])
sheet = book.get_sheet_by_name(sys.argv[2])

count = 0
for i, row in enumerate(sheet.iter_rows()):
    if (i == 0):
        cols = "( "
        for j, c in enumerate(row):
            cols = cols + c.value + ', '
        cols = cols + sys.argv[4] + " )  "
#        print(cols + '\n')
    if (i > 0):
        vals = "( "
        for j, c in enumerate(row):
            vals = vals + '"'+ str(c.value) +'"' + ', '
        vals = vals + '0 ) '
        stmt = "insert into " + sys.argv[3] + cols + " values " + vals + ";"
        print(stmt + '\n')
        count = count + 1


        

       
    
