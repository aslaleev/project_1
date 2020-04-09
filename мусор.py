from flask import Flask , render_template
from flask_cors import CORS
from flask import send_from_directory
import csv
import mysql.connector
import datetime


app = Flask(__name__)
CORS(app)

@app.route('/todo/api/v1.0/export/<string:select>/<string:param1>/<string:param2>', methods=['GET'])
def report(select,param1,param2):
    conn = mysql.connector.connect(host="localhost",
                                   user='root',
                                   password='12345',
                                   database='Договора',
                                   auth_plugin='mysql_native_password')
    if param1=='' and param2=='':
        ss = str (select)
    elif param2=='':
        ss = " %s  where datacreate > '%s' " % (select, param1)

    elif param1 == '':
        ss = " %s where datacreate < '%s' " % (select, param2)
    else:
        ss = " %s where datacreate > '%s' and datacreate < '%s' " % (select, param1, param2)
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    c = conn.cursor()
    list = []
    c.execute(ss)
    for row in c:
        minilist = []
        for i in range(len(row)):
            minilist.append(row[i])
        list.append(minilist)
    name_of_file = 'export_file_%s.csv' % now
    with open('export_file_%s.csv' % now, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(list)
    return name_of_file



if __name__ == '__main__':
    app.run(debug=True)

