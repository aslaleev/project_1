# Сервис для вывода из БД csv файл с данными по sql запросу
import cx_Oracle
import csv


def report(select):
    dsn_tns=cx_Oracle.makedsn('ORADEV','1521',service_name='diadaily')
    conn = cx_Oracle.connect(user= 'sogins',password = '1', dsn=dsn_tns)
    c = conn.cursor()
    list = []
    minilist = []
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




f = report('select c.contractid, c.signdate, c.insproductid from contractins c FETCH FIRST 10 ROWS ONLY')