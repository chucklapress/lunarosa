from flask import Flask,render_template,request
import os,glob
import datetime

app= Flask(__name__)
@app.route('/')
def index():
    now = datetime.datetime.now()
    date = now.strftime("%m-%d-%Y")
    a_file = open('/Users/chucklapress/tiy-projects/lunarosa/flavors.txt')
    file_contents = a_file.read()
    sample_list = file_contents.splitlines(True)
    converted_list = []

    for element in sample_list:
        converted_list.append(element.strip())
    for flavor in converted_list:
        print(flavor)
    return render_template('index.html', **locals())


if __name__=="__main__":
    app.run(debug=True)
