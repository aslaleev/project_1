from flask import Flask , render_template
from flask_cors import CORS
from flask import send_from_directory
import csv
import mysql.connector


app = Flask(__name__)
CORS(app)


@app.route('/todo/api/v1.0/export/<string:param1>/<string:param2>', methods=['GET'])
def report(param1,param2):
    conn = mysql.connector.connect(host="localhost",
                                   user='root',
                                   password='12345',
                                   database='Договора',
                                   auth_plugin='mysql_native_password')
    if param1=='' and param2=='':
        ss = str (select)
    elif param2=='':
        ss = "select * from product where datacreate > '%s' " % (param1)
    elif param1 == '':
        ss = "select * from product where datacreate < '%s' " % (param2)
    else:
        ss = "select name, sokr from product where datacreate > '%s' and datacreate < '%s' " % (param1, param2)

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
    return '1'


if __name__ == '__main__':
    app.run(debug=True)
