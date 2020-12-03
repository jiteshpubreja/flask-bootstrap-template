from flask import Flask, render_template, request, redirect, url_for, flash, Response, send_from_directory, g
import os
import re
import json
import datetime


from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())


app = Flask(__name__)
app.secret_key = "thisissomethingsecret"
app.app_context().push()

@app.route('/')
def homepage():
  flash("Info can be added here.","info")
  return render_template("homepage.html")