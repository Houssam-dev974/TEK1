#!/usr/bin/env python3
import mysql.connector
from flask import jsonify
from flask import Flask, request
import pymysql
import numpy as np
from config import my_connexion

cnx = my_connexion()
mycursor = cnx.cursor()

class Models:
    def check_username(self, params):
        mycursor.execute("SELECT username FROM user WHERE username=%s", [params]);
        my_username = mycursor.fetchone()
        conv_username = np.array(my_username, dtype='str')
        if conv_username == params:
            return True
        else:
            return False

    def check_password(self, pwd):
        mycursor.execute("SELECT password FROM user WHERE password=%s", [pwd]);
        my_pwd = mycursor.fetchone()
        conv_pwd = np.array(my_pwd, dtype='str')
        if conv_pwd == pwd:
            return True
        else:
            return False

    def add_data(self, user_id, username, password):
        mycursor.execute("INSERT INTO `user`(user_id, username, password) VALUES ('%s', '%s', '%s')" % (
        user_id, username, password));
        mycursor.execute("COMMIT;");

    def username_info(self, param):
        mycursor.execute("SELECT username FROM user WHERE username=%s", [param]);
        username = mycursor.fetchone()
        conv_username = np.array(username, dtype='str')
        return conv_username

    def pwd_info(self, param):
        mycursor.execute("SELECT password FROM user WHERE username=%s", [param]);
        pwd = mycursor.fetchone()
        conv_pwd = np.array(pwd, dtype='str')
        return conv_pwd

    def id_info(self, param):
        mycursor.execute("SELECT user_id FROM user WHERE username=%s", [param]);
        id = mycursor.fetchone()
        conv_id = np.array(id, dtype='str')
        return conv_id

    def check_task_id(self, params):
        mycursor.execute("SELECT task_id FROM task WHERE task_id=%s", [params]);
        check_id = mycursor.fetchone()
        conv_check = np.array(check_id, dtype='str')
        if conv_check == params:
            return True
        else:
            return False

    def add_task_user(self, username, id, title, status):
        user_id_tab = self.id_info(username)
        user_id = user_id_tab[0]
        mycursor.execute(
            "INSERT INTO `task`(task_id, title, begin, end, status) VALUES ('%s', '%s', 'now', 'friday', '%s')" % (
            id, title, status));
        mycursor.execute("COMMIT;");
        mycursor.execute(
            "INSERT INTO `user_has_task`(fk_user_id, fk_task_id) VALUES ('%s', '%s')" % (
            user_id, id));
        mycursor.execute("COMMIT;");

    def all_tasks(self, username):
        print(username)
        user_id_tab = self.id_info(username)
        user_id = user_id_tab[0]
        print(user_id)
        result = []
        try:
            mycursor.execute("SELECT fk_task_id FROM user_has_task WHERE fk_user_id=%s", [user_id]);
            tasks = mycursor.fetchall()
            conv_tasks = np.array(tasks, dtype='str')
            for i in range(1, len(tasks)):
                result.append('prepare_my_repo', '1', 'To do')
                print(result)
        except:
            return ([])
        return (result)

    def remove_task(self, id):
        mycursor.execute("DELETE FROM task WHERE task_id=%s", [id])
        mycursor.execute("COMMIT;");
        mycursor.execute("DELETE FROM user_has_task WHERE fk_task_id=%s", [id])
        id_task = mycursor.fetchone()
        conv_remove = np.array(id_task, dtype='str')
        mycursor.execute("COMMIT;");
        return (conv_remove)