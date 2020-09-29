from flask import Flask,render_template,request
import mysql.connector

homee=Flask(__name__)
@homee.route('/')
def hello_world():
    return "home"