import openpyxl

wb = openpyxl.load_workbook('考勤人员数据.xlsx')
sheet = wb['人员基本信息']
row_list = []
for row in sheet.iter_rows():
    cell_list = []
    for cell in row:
        cell_list.append(cell.value)
    row_list.append(cell_list)
fp = open("插入考勤记录.sql", "a+")
del row_list[0]
for row in row_list:
    date = row[1]
    datestr = date.strftime('%Y-%m-%d')
    print(date)
    pushDate = datestr + ' 00:00:00.000'

    userNo = row[2]
    insertSql = "INSERT INTO UserAttendanceRecord([UserNo],[AttendanceDate],[AttendanceTime],[CreateDate],[StatisticStatus],[Remark])VALUES("
    insertSql += "'" + userNo + "',"
    attendanceList = row[4:]
    for cell in attendanceList:
        if cell is not None and cell != '':
            insertSql1 = insertSql + "'" + pushDate + "',"
            print(datestr)
            pushDate1 = datestr + ' ' + cell.strftime('%H:%M:%S') + '.000'
            insetSql1 = insertSql1 + "'" + pushDate1 + "','" + pushDate1 + "',1,null)"
            print(insetSql1, file=fp)
            print("Go", file=fp)
fp.close()
