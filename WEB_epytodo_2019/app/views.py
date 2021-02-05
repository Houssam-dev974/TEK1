#!/usr/bin/env python3
from app import app
from flask import jsonify
from flask import abort
from flask import render_template
from flask import request
from app.controller import Controller
import  pymysql  as sql
import string
import json

######## Error handlers ########

@app.errorhandler(401)
def log_error(h_error):
    error_msg = "you must be logged in"
    return jsonify(error=error_msg)

@app.errorhandler(500)
def task_id_error(h_error):
    error_msg = "task id does not exist"
    return jsonify(error=error_msg)

@app.errorhandler(400)
def internal_error(h_error):
    error_msg = "internal error"
    return jsonify(error=error_msg)

def is_error(response_data):
    strerror = '{"error"'
    for i in range(0, 8):
        if (response_data[i] != strerror[i]):
            return (False)
    return (True)

######## Routes ########

class Member:
    user_connected = False
    name = "none"
    user_id = "none"

member = Member()

@app.route('/', methods =['GET'])
def      route_home ():
    if (member.user_connected == False):
        user_status = "Disconnected"
    else:
        user_status = "Connected"
    return render_template("home.html",
                            status = user_status)

@app.route('/home', methods =['GET'])
def      route_index ():
    return render_template("index.html",
                            title = "Hello World !",
                            navlist = [
                            ('/', 'index', 'Indexezzzz'),
                            ('/products', 'products', 'Products'),
                            ('/account', 'account', 'Account')])




@app.route('/register', methods =['GET'])
def      register ():
    member.user_connected = False
    if (member.user_connected == False):
        return render_template('register.html')
    else:
        return jsonify(error="already logged in")

@app.route('/register', methods =['POST'])
def      register_user ():
    form_input = request.form
    user = form_input.getlist('username')
    password = form_input.getlist('password')
    _id = form_input.getlist('id')
    controller = Controller()
    result = controller.register(user, password, _id)
    loaded_response = result.data
    if (is_error(loaded_response) == True):
        return (result)
    else:
        member.user_connected = True
        member.name = user[0]
        return render_template('tasks.html',
                                username = member.name,
                                status = "registered")
    return (result)




@app.route('/signin', methods =['GET'])
def     login():
    member.user_connected = False
    if (member.user_connected == False):
        return render_template('login.html')
    else:
        return jsonify(error="already logged in")

@app.route('/signin', methods =['POST'])
def      signin_user():
    form_input = request.form
    user = form_input.getlist('username')
    password = form_input.getlist('password')
    controller = Controller()
    result = controller.signin(user, password)
    loaded_response = result.data
    if (is_error(loaded_response) == True):
        return (result)
    else:
        member.user_connected = True
        member.name = user[0]
        return render_template('tasks.html',
                            username = member.name,
                            status = "connected")
    return (result)




@app.route('/signout', methods =['POST'])
def      signout_user ():
    member.user_connected = False
    return jsonify(result="signout successful")




@app.route('/user', methods =['GET'])
def      route_all_users():
    controller = Controller()
    if (member.user_connected == False):
        abort(401)
    result = controller.fetch_user_infos(member.name)
    return result




@app.route('/user/task', methods =['GET'])
def      route_all_user_tasks():
    controller = Controller()
    if (member.user_connected == False):
        abort(401)
    try:
        result = controller.fetch_all_user_tasks(member.name)
    except:
        abort(400)
    if (len(result) == 0):
        user_tasks = []
    else:
        user_tasks = result
    print(result)
    return render_template("tasks_menu.html",
                            username = member.name,
                            tasks = [
                            ('prepare_my_repo', '1', 'To do'),
                            ('mrclean', '2', 'To do'),
                            ('push_that', '3', 'To do'),
                            ('NormEZ.rb', '4', 'To do')])





@app.route('/user/task/id', methods =['GET'])
def     route_specific_task():
    result = ""
    if (member.user_connected == False):
        abort(401)
    controller = Controller()
    result = controller.view_task()
    return (jsonify(result))

@app.route('/user/task/id', methods =['POST'])
def     mod_specific_task():
    if (member.user_connected == False):
        abort(401)
    result = request.form
    task_id = result.getlist('task_id')
    status = result.getlist('status')
    controller = Controller()
    result = controller.mod_task(task_id, status)
    loaded_response = result.data
    if (is_error(loaded_response) == True):
        return (result)
    else:
        return jsonify(result="update done")
    return (result)




@app.route('/user/task/add', methods =['POST'])
def     add_task():
    if (member.user_connected == False):
        abort(401)
    result = request.form
    title = result.getlist('title')
    task_id = result.getlist('task_id')
    status = "todo"
    controller = Controller()
    result = controller.add_task(member.name, title, task_id, status)
    loaded_response = result.data
    if (is_error(loaded_response) == True):
        return (result)
    else:
        return jsonify(result="new task added")
    return (result)




@app.route('/user/task/del/id', methods =['POST'])
def     del_task():
    result = ""
    if (member.user_connected == False):
        abort(401)
    result = request.form
    task_id = result.getlist('task_id')
    controller = Controller()
    result = controller.del_task(task_id)
    loaded_response = result.data
    if (is_error(loaded_response) == True):
        return (result)
    else:
        return jsonify(result="task deleted")
    return (result)