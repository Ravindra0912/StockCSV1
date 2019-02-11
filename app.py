from flask import Flask,render_template
import pandas as pd
import os

app = Flask(__name__)

# function to get all the attributes for each stock in a file.
def filter(filename):

    df = pd.read_csv("STOCK CSV FILES/"+filename)
    attribute_list = list(df)
    attribute_list = attribute_list[2:52]
    full_list = []
    f = open("STOCK CSV FILES/"+filename)
    count = 0
    for line in f:
        count += 1
        if count == 1:
            continue
        reqd_attributes = []
        value_list = line.split(",")
        current_stock = value_list.pop(0)
        date = value_list[-2:]
        value_list = value_list[1:51]
        i = 0
        for i in range(len(value_list)):
            if value_list[i] >= '8':
                reqd_attributes.append([attribute_list[i], value_list[i]])
        reqd_attributes = [current_stock] + reqd_attributes
        full_list = full_list + [reqd_attributes]
    return full_list,date


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<filename>')
def file(filename):
    all_files = os.listdir('STOCK CSV FILES')
    requested_file = filename
    for file in all_files:
        name = file[:-4]
        name = name.split("_")
        if requested_file in name:
            filename = file
            break
    Industry_names={'ConsDis':'Consumer Discretionary','Constap':'Consumer Staples','IT':'Information Technology','LargeCap':'Large Capital','MediumCap':'Medium Capital','SmallCap':'Small Capital','Tele':'Tele-communication'}
    full_list,date = filter(filename)
    stock_names=[]
    f = filename.split('_')
    f=f[1]
    if f in Industry_names.keys():
        f = Industry_names[f]
    for elem in full_list:
        stock_names.append(elem.pop(0))
    return render_template("first2.html", full=full_list, st=stock_names,fn=f,d=date)


if __name__ == '__main__':

    app.run(debug=True)

