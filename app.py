import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
import csv

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
#GETはアクセスしたとき、POSTはデータを追加するとき
def index():

    with open('questions.csv') as f:
        kaisetu2=[]
        reader = csv.reader(f)

        #csvファイルのデータをループ
        for row in reader:
            kaisetu2.append(str(row[2]))

    aa=[]
    #print(kaisetu2)
    for index in range(len(kaisetu2)):
        aa.append(kaisetu2[index])
    f.close()
    return render_template("grade.html",kaisetu=aa)