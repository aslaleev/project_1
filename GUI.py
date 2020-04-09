from flask import Flask , render_template
from flask_cors import CORS
from flask import send_from_directory
import csv
import mysql.connector
import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def Index():
    return render_template('file.html', param=get_tasks(vivod_dannih()))

@app.route('/todo/api/v1.0/taskslist', methods=['GET'])
def get_tasks():
    with open('directory_of_report.csv', 'r', encoding='utf-8') as ff:
        value = []
        reader = csv.DictReader(ff)
        for line in reader:
            value.append(line)
    m=[]
    for i in range(len(value)):
        k = value[i]['reportname']
        m.append(k)
        i = int(i + 1)
    return ({'tasks':m})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_asd(task_id):
    with open('directory_of_report.csv', 'r', encoding='utf-8') as ff:
        value = []
        reader = csv.DictReader(ff)
        for line in reader:
            value.append(line)
    for i in range(len(value)):
        if value[i]['id'] == str(task_id):
            return str(value[i]['queries'])

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
    name_of_file = 'export_file_%s.csv' %now
    with open('export_file_%s.csv' %now, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(list)
    return name_of_file

@app.route('/todo/api/v1.0/uploads/<path:filename>', methods=['GET', 'POST'])
def download_file(filename):
    return send_from_directory("/Users/User/PycharmProjects/project_1/expirience", filename=filename, as_attachment=True)

@app.route('/todo/api/v1.0/tasks/<string:name>', methods=['GET'])
def file_name(name):
    return str(name)

if __name__ == '__main__':
    app.run(debug=True)


