import json
from flask import Flask , render_template
from read_by_report import vivod_dannih

app = Flask(__name__)

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
    for n in range(len(tasks)):
        if int(tasks[n]['id']) == task_id:
            return tasks[n]




if __name__ == '__main__':
    app.run(debug=True)


