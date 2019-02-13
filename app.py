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
        reqd_attributes.append([attribute_list[0],int(float(value_list[0]))])
        reqd_attributes.append([attribute_list[1],int(float(value_list[1]))])
        reqd_attributes = [current_stock] + reqd_attributes
        full_list = full_list + [reqd_attributes]
    return full_list,date

def profit(filename):
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

        reqd_attributes.append([attribute_list[27],int(float(value_list[27]))])
        reqd_attributes.append([attribute_list[29],int(float(value_list[29]))])
        reqd_attributes.append([attribute_list[30],int(float(value_list[30]))])
        reqd_attributes.append([attribute_list[31],int(float(value_list[31]))])
        reqd_attributes.append([attribute_list[32],int(float(value_list[32]))])
        reqd_attributes = [current_stock] + reqd_attributes
        full_list = full_list + [reqd_attributes]
    for elem in full_list:
            elem.pop(0)
    return full_list

def revenue(filename):
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

        reqd_attributes.append([attribute_list[33], int(float(value_list[33]))])
        reqd_attributes.append([attribute_list[34], int(float(value_list[34]))])
        reqd_attributes.append([attribute_list[35], int(float(value_list[35]))])
        reqd_attributes.append([attribute_list[36], int(float(value_list[36]))])
        reqd_attributes.append([attribute_list[28], int(float(value_list[28]))])
        reqd_attributes.append([attribute_list[40], int(float(value_list[40]))])
        reqd_attributes.append([attribute_list[39], int(float(value_list[39]))])
        reqd_attributes = [current_stock] + reqd_attributes
        full_list = full_list + [reqd_attributes]

    for elem in full_list:
            elem.pop(0)
    return full_list

def get_file_name(filename):
    all_files = os.listdir('STOCK CSV FILES')
    requested_file = filename
    for file in all_files:
        name = file[:-4]
        name = name.split("_")
        if requested_file in name:
            filename = file
            break
    return filename


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<filename>')
def file(filename):
    filename = get_file_name(filename)
    industry_names = {'ConsDis':'Consumer Discretionary','ConsStap':'Consumer Staples','IT':'Information Technology','LargeCap':'Large Capital','MediumCap':'Medium Capital','SmallCap':'Small Capital','Tele':'Tele-communication'}
    full_list1,date = filter(filename)
    stock_names=[]
    f = filename.split('_')
    full_list3=profit(filename)
    full_list4 = revenue(filename)
    f=f[1]
    if f in industry_names.keys():
        sectorname = industry_names[f]
        sectorsc = f
    else:
        sectorname = f
        sectorsc= f
    for elem in full_list1:
        stock_names.append(elem.pop(0))
    return render_template("first2.html", full=full_list1,full3=full_list3, st=stock_names,d=date,sc=sectorsc,fn=sectorname,full4=full_list4)


if __name__ == '__main__':

    app.run(debug=True)

