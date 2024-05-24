import xlrd
book=xlrd.open_workbook('excel/EmpFamily.xlsx') #打开Excel
sheet=book.sheet_by_name('Sheet1') #根据编号获取sheet页
#sheet=book.sheet_by_name('sheet1') #也可以根据sheet页名字获取sheet页
#、第一步将excel表读取到二维表---->list2
nrows=sheet.nrows
list1=[]
list2=[]
tp={}
# for i in range(1,nrows):
# 	# print(sheet.row_values(i))#第一行内容
# 	list1=[(int(sheet.row_values(j)[0]),str(sheet.row_values(j)[2]),str(sheet.row_values(j)[3]),str(sheet.row_values(j)[4]),str(sheet.row_values(j)[5]),str(sheet.row_values(j)[6]),j+2) for j in range(1,nrows)]
# 	#这里很关键  从excel读取都是varchar ,由于 数据库该字段为int,所以这里也要转为int
# 	#取单元格的值sheet.row_values  ,sheet.nrows总行数,sheet.row_values(i) 第一列 为list
list2=[(int(sheet.row_values(j)[0]),str(sheet.row_values(j)[2]),str(sheet.row_values(j)[3]),str(sheet.row_values(j)[4]),str(sheet.row_values(j)[5]),str(sheet.row_values(j)[6]),j+2) for j in range(1,nrows)]
# print(type(sheet.row_values(i)))
print(list2)
# print(list1==list2)
#LIST2 直接使用列表向导式,简单点吧






