from flask import Flask,render_template,request
import os,glob
import datetime


f=open('/Users/chucklapress/tiy-projects/lunarosa/flavors.txt','r')
g= f.read()


app= Flask(__name__)
@app.route('/')
def index():
    now = datetime.datetime.now()
    date = now.strftime("%m-%d-%Y")
    return render_template('index.html',n=g, **locals())


if __name__=="__main__":
    app.run(debug=True)
