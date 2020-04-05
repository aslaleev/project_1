from flask import Flask , render_template
from read_by_report import vivod_dannih
from flask_cors import CORS
from flask import send_from_directory
import csv
import mysql.connector
from datetime import date

app = Flask(__name__)
CORS(app)

tasks = vivod_dannih()

@app.route('/')
def Index():
    return render_template('file.html', param=get_tasks(tasks))


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks(tasks):
    m=[]
    for i in range(len(tasks)):
        k = tasks[i][' reportname ']
        m.append(k)
        i = int(i + 1)
    return m


@app.route('/todo/api/v1.0/taskslist', methods=['GET'])
def get_tasklisk():
    return ({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    date = ['param1', 'param2','param3']
    ke = dict()
    for n in range(len(tasks)):
        if int(tasks[n]['id']) == task_id:
            for i in tasks[n]:
                if (i in date and tasks[n][i] != ' '):
                    ke[i]=tasks[n][i]
            return ke


@app.route('/todo/api/v1.0/export/<string:param1>/<string:param2>', methods=['GET'])
def report(param1,param2):
    conn = mysql.connector.connect(host="localhost",
                                   user='root',
                                   password='12345',
                                   database='Договора',
                                   auth_plugin='mysql_native_password')
    if param1=='' and param2=='':
        ss = str (select)
        ss = " select * from product"
    elif param2=='':
        ss = "select * from product where datacreate > '%s' " % (param1)

    elif param1 == '':
        ss = "select * from product where datacreate < '%s' " % ( param2)
    else:
        ss = "select * from product where datacreate > '%s' and datacreate < '%s' " % ( param1, param2)
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


@app.route('/todo/api/v1.0/uploads/<path:filename>', methods=['GET', 'POST'])
def download_file(filename):
    return send_from_directory("/Users/User/PycharmProjects/project_1/expirience", filename=filename, as_attachment=True)


@app.route('/todo/api/v1.0/tasks/name', methods=['GET'])
def file_name():
    return "export_file.csv"


if __name__ == '__main__':
    app.run(debug=True)


