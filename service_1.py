# Сервис для вывода из БД csv файл с данными по sql запросу
import cx_Oracle

def report(select,param1,param2):
    conn = mysql.connector.connect(host="localhost",
                                   user='root',
                                   password='12345',
                                   database='Договора',
                                   auth_plugin='mysql_native_password')
    if param1=='' and param2=='':
        ss = str (select)
    elif param2=='':
        ss = str (select + ' where datacreate > ' + param1)
    elif param1 == '':
        ss = str (select + ' where ' + ' datacreate < ' + param2)
    else:
        ss = str (select + ' where datacreate > ' + param1 + ' and datacreate < ' + param2)
    c = conn.cursor()
    list = []
    c.execute(ss)
    for row in c:
        minilist = []
        for i in range(len(row)):
            minilist.append(row[i])
        list.append(minilist)
    with open('export_file.csv', "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(list)






#f = export('22.02.19', '12.02.20', 'select * from contractins')

f = report('select productid,name from product', '', '')