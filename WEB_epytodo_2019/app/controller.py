#!/usr/bin/env python3
from app import app
from flask import jsonify
from flask import abort
from flask import render_template
from app.models import Models

class Controller:
    def register(self, user, password, _id):
        model = Models()
        if (model.check_username(user[0]) == True):
            return (jsonify(error="account already exists"))
        try:
            model.add_data(_id[0], user[0], password[0])
        except Exception  as e :
            print("Caught an exception : ", e)
            return (jsonify(error="internal error"))
        return (jsonify(result="account created"))

    def signin(self, user, password):
        model = Models()
        try:
            if (model.check_username(user[0]) == True and model.check_password(password[0]) == True):
                return (jsonify(result="signin successful"))
            else:
                return (jsonify(error="login or password does not match"))
        except:
            return (jsonify(error="internal error"))

    def fetch_user_infos(self, name):
        model = Models()
        try:
            user = model.username_info(name)
            pwd = model.pwd_info(name)
            user_id = model.id_info(name)
            return jsonify(username=user[0],
                           password=pwd[0],
                           id=user_id[0])
        except:
            return (jsonify(error="internal error"))

    def view_task(self):
        model = Models()
        try:
            if (model.find_task() == True):
                result = model.get_task()
                return (jsonify(result))
            else:
                abort(500)
        except:
            return (jsonify(error="internal error"))

    def fetch_all_user_tasks(self, username):
        model = Models()
        result = model.all_tasks(username)
        return (result)

    def mod_task(self, task_id, status):
        model = Models()
        # if (model.check_task_id_exist(task_id[0]) == False):
        #     return (jsonify(error="task id does not exist"))
        # try:
        #     model.modify_task(task_id[0], status)
        # except:
        #     return (jsonify(error="internal error"))
        return jsonify(result="update done")

    def add_task(self, username, title, task_id, status):
        model = Models()
        if (model.check_task_id(task_id[0]) == True):
            return (jsonify(error="task id already exists"))
        try:
            model.add_task_user(username, task_id[0], title[0], status)
        except:
            return (jsonify(error="internal error"))
        return jsonify(result="new task added")

    def del_task(self, task_id):
        model = Models()
        if (model.check_task_id(task_id[0]) == False):
            return (jsonify(error="task id does not exist"))
        try:
            model.remove_task(task_id[0])
        except:
            return (jsonify(error="internal error"))
        return jsonify(result="task deleted")