import json
from flask import Flask , render_template
from read_by_report import vivod_dannih
from flask_cors import CORS
import csv


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


@app.route('/todo/api/v1.0/export/<string:param1>/<string:param2>/<string:select>', methods=['GET'])
def export(param1,param2,select):
    ss = str (select + ' where datecreate > ' + param1 + ' and datecreate < ' + param2)
    with open('export_file.csv', "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(ss)
        return '1'



if __name__ == '__main__':
    app.run(debug=True)


