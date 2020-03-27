# Сервис для вывода из БД csv файл с данными по sql запросу
import cx_Oracle
import csv


def report(select):
    # dsn=cx_Oracle.makedsn('localhost','3306',service_name='MySQL@localhost:3306')
    # conn = cx_Oracle.connect(user= 'root',password = '12345', dsn=dsn)
    # c = conn.cursor()
    connstr = 'root/Mysql@localhost:3306/orcl'
    conn = cx_Oracle.connect(connstr)
    c = conn.cursor()
    list = []

    with open('read.txt', 'r', encoding='utf-8') as tt:
        c.execute(select)
    for row in c:
        minilist = []
        for i in range(len(row)):
            minilist.append(row[i])
        list.append(minilist)

    with open('1.csv', "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(list)


def export(param1,param2,select):
    ss = str (select + 'where datecreate > ' + param1 + 'and datecreate < ' + param2)
    print(ss)

    with open('export_file.csv', "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(ss)



f = export('22.02.19', '12.02.20', 'select * from contractins')


# f = report('select * from product c')