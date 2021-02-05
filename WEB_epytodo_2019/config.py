import mysql.connector
from flask import Flask, request

app = Flask(__name__)
def my_connexion():
    cnx = mysql.connector.connect(user='root', password="orika974", host='127.0.0.1', database='epytodo')
    return (cnx)

