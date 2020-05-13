# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def homepage():
    return render_template("index.html")

#static route
@app.route("/assignments.html")
def second_page():
    return render_template("assignments.html")

#static route
@app.route("/classes.html")
def third_page():
    return render_template("classes.html")

#static route
@app.route("/1006")
def extra_exercise():
    return render_template("1006.html")

#start the server
if __name__ == "__main__":
    app.run()
