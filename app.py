from flask import Flask,render_template,redirect,url_for
import pandas as pd
import os

app = Flask(__name__)


def get_close(filename):


    df = pd.read_csv("STOCK CSV FILES/"+filename)
    attribute_list = list(df)
    f = open("STOCK CSV FILES/" + filename)
    count=0
    full_list=[]
    for line in f:
        count += 1
        if count == 1:
            continue
        reqd_attributes = []
        value_list = line.split(",")
        reqd_attributes.append(["close",value_list[1]])
        full_list = full_list + [reqd_attributes]
    return full_list


def filter(filename):
    # Stock Growth Rating
    # Financial Health Rating
    df = pd.read_csv("STOCK CSV FILES/"+filename)
    attribute_list = list(df)
    attribute_list = attribute_list[1:52]
    full_list = []
    f = open("STOCK CSV FILES/"+filename)
    count = 0
    date = "-"
    for line in f:
        count += 1
        if count == 1:
            continue
        reqd_attributes = []
        value_list = line.split(",")
        current_stock = value_list.pop(0)
        date = value_list[-2:]
        value_list = value_list[0:51]
        i = 0
        reqd_attributes.append([attribute_list[1],"★ "*int(float(value_list[1])),"☆ "*(10-int(float(value_list[1]))), int(float(value_list[1]))])
        reqd_attributes.append([attribute_list[2],"★ "*int(float(value_list[2])), "☆ "*(10-int(float(value_list[2]))),int(float(value_list[2]))])
#        reqd_attributes.append([attribute_list[2],int(float(value_list[2]))])
        #reqd_attributes.append([attribute_list[0], value_list[0]])
        reqd_attributes = [current_stock] + reqd_attributes
        full_list = full_list + [reqd_attributes]
    return full_list,date


@app.route('/efef')
def error():
        return render_template("error.html")


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
        if attribute_list[27].find("(")!= -1:
            reqd_attributes.append([attribute_list[27][:attribute_list[27].find("(")],"★ "*int(float(value_list[27])),"☆ "*(10 - int(float(value_list[27]))),int(float(value_list[27]))])
        else:
            reqd_attributes.append([attribute_list[27],"★ "*int(float(value_list[27])),"☆ "*(10-int(float(value_list[27]))),int(float(value_list[27]))])
        if attribute_list[29].find("(")!= -1:
            reqd_attributes.append([attribute_list[29][:attribute_list[29].find("(")], "★ " * int(float(value_list[29])),"☆ " * (10 - int(float(value_list[29]))), int(float(value_list[29]))])
        else:
            reqd_attributes.append([attribute_list[29],"★ " * int(float(value_list[29])),"☆ " *(10 - int(float(value_list[29]))),int(float(value_list[29]))])
        if attribute_list[30].find("(")!= -1:
            reqd_attributes.append([attribute_list[30][:attribute_list[30].find("(")], "★ " * int(float(value_list[30])),"☆ " * (10 - int(float(value_list[30]))), int(float(value_list[30]))])
        else:
            reqd_attributes.append([attribute_list[30], "★ " * int(float(value_list[30])), "☆ " * (10 - int(float(value_list[30]))),int(float(value_list[30]))])

        if attribute_list[31].find("(")!= -1:
            reqd_attributes.append([attribute_list[31][:attribute_list[31].find("(")], "★ " * int(float(value_list[31])),"☆ " * (10 - int(float(value_list[31]))), int(float(value_list[31]))])
        else:
            reqd_attributes.append([attribute_list[31], "★ " * int(float(value_list[31])), "☆ " *(10-int(float(value_list[31]))),int(float(value_list[31]))])
        if attribute_list[32].find("(")!= -1:
            reqd_attributes.append([attribute_list[32][:attribute_list[32].find("(")], "★ " * int(float(value_list[32])),"☆ " * (10 - int(float(value_list[32]))), int(float(value_list[32]))])
        else:
            reqd_attributes.append([attribute_list[31], "★ " * int(float(value_list[32])), "☆ " * (10 - int(float(value_list[32]))),int(float(value_list[32]))])
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
        if attribute_list[33].find("(") != -1:
            reqd_attributes.append([attribute_list[33][:attribute_list[33].find("(")],"★ "*int(float(value_list[33])),"☆ "*(10 - int(float(value_list[33]))),int(float(value_list[33]))])
        else:
            reqd_attributes.append([attribute_list[33],"★ "*int(float(value_list[33])),"☆ "*(10 - int(float(value_list[33]))),int(float(value_list[33]))])
        if attribute_list[34].find("(") != -1:
            reqd_attributes.append([attribute_list[34][:attribute_list[34].find("(")],"★ "*int(float(value_list[34])),"☆ "*(10 - int(float(value_list[34]))),int(float(value_list[34]))])
        else:
            reqd_attributes.append([attribute_list[34],"★ "*int(float(value_list[34])),"☆ "*(10 - int(float(value_list[34]))),int(float(value_list[34]))])
        if attribute_list[35].find("(") != -1:
            reqd_attributes.append([attribute_list[35][:attribute_list[35].find("(")],"★ "*int(float(value_list[35])),"☆ "*(10 - int(float(value_list[35]))),int(float(value_list[35]))])
        else:
            reqd_attributes.append([attribute_list[35],"★ "*int(float(value_list[35])),"☆ "*(10 - int(float(value_list[35]))),int(float(value_list[35]))])
        if attribute_list[36].find("(") != -1:
            reqd_attributes.append([attribute_list[36][:attribute_list[36].find("(")],"★ "*int(float(value_list[36])),"☆ "*(10 - int(float(value_list[36]))),int(float(value_list[36]))])
        else:
            reqd_attributes.append([attribute_list[36],"★ "*int(float(value_list[36])),"☆ "*(10 - int(float(value_list[36]))),int(float(value_list[36]))])
        if attribute_list[28].find("(") != -1:
            reqd_attributes.append([attribute_list[28][:attribute_list[28].find("(")],"★ "*int(float(value_list[28])),"☆ "*(10 - int(float(value_list[28]))),int(float(value_list[28]))])
        else:
            reqd_attributes.append([attribute_list[28],"★ "*int(float(value_list[28])),"☆ "*(10 - int(float(value_list[28]))),int(float(value_list[28]))])
        if attribute_list[40].find("(")!= -1:
            reqd_attributes.append([attribute_list[40][:attribute_list[40].find("(")],"★ "*int(float(value_list[40])),"☆ "*(10 - int(float(value_list[40]))),int(float(value_list[40]))])
        else:
            reqd_attributes.append([attribute_list[40],"★ "*int(float(value_list[40])),"☆ "*(10 - int(float(value_list[40]))),int(float(value_list[40]))])
        if attribute_list[39].find("(")!= -1:
            reqd_attributes.append([attribute_list[39][:attribute_list[39].find("(")], "★ "*int(float(value_list[39])),"☆ "*(10 - int(float(value_list[39]))),int(float(value_list[39]))])
        else:
            reqd_attributes.append([attribute_list[39],"★ "*int(float(value_list[39])),"☆ "*(10 - int(float(value_list[39]))),int(float(value_list[39]))])
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
    industry_names = {'ConsDis':'Consumer Discretionary','ConsStap':'Consumer Staples','IT':'Information Technology','LargeCap':'Large Cap','MediumCap':'Medium Cap','SmallCap':'Small Cap','Tele':'Telecommunication'}
    full_list1,date = filter(filename)
    stock_names=[]
    f = filename.split('_')
    full_list3=profit(filename)
    full_list4 = revenue(filename)
    close = get_close(filename)
    f=f[1]
    if f in industry_names.keys():
        sectorname = industry_names[f]
        sectorsc = f
    else:
        sectorname = f
        sectorsc= f
    for elem in full_list1:
        stock_names.append(elem.pop(0))
    return render_template("first.html", full=full_list1,full3=full_list3, st=stock_names,d=date,sc=sectorsc,fn=sectorname,full4=full_list4,close=close)


if __name__ == '__main__':

    app.run(debug=True)

