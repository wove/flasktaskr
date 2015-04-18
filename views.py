from flask import Flask, flash, redirect, render_template, request, session, url_for, g
from functools import wraps
import sqlite3


app = Flask(__name__)
app.config.from_object('config')

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def login_required(test):
    @wraps(test)
    def wrap(*arg, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap

@app.route('/logout/')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid credentials. Please try again'
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            return redirect(url_for('tasks'))
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/tasks/')
@login_required
def tasks():
    g.db = connect_db()
    cur = g.db.execute("SELECT name, due_date, priority, task_id FROM tasks WHERE status=1")
    open_tasks = [dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cur.fetchall()]
    cur = g.db.execute("SELECT name, due_date, priority, task_id FROM tasks WHERE status=0")
    closed_tasks = [dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template('tasks.html',
                            form=AddTaskForm(request.form),
                            open_tasks=open_tasks,
                            closed_tasks=closed_tasks)
