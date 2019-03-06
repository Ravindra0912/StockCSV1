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
def filter2(filename):
    # Stock Growth Rating
    # Financial Health Rating
    print("file",filename)
    df = pd.read_csv("STOCK CSV FILES/"+filename)
    attribute_list = list(df)
    attribute_list = attribute_list[1:62]
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
        value_list = value_list[0:62]
        i = 0
    #    print("AAAAAAAA",attribute_list)
        flag1=0
        flag2=0

        for i in range(len(attribute_list)):
            attr=[]
            attr = attribute_list[i].split()
            for j in range(len(attr)):
                attr[j] = attr[j].lower()
            if 'percentage'.lower() in attr and 'price'.lower() in attr and 'change'.lower() in attr and 'over'.lower() in attr and 'last'.lower() in attr and '20'.lower() in attr and 'days'.lower() in attr:
                reqd_attributes.append([attribute_list[i], value_list[i]])
            elif 'close'.lower() in attr:
                reqd_attributes.append([attribute_list[i], value_list[i]])
            elif 'mean'.lower() in attr and 'price'.lower() in attr  and 'over'.lower() in attr and 'last'.lower() in attr and '20'.lower() in attr and 'days'.lower() in attr:
                reqd_attributes.append([attribute_list[i], value_list[i]])
                mean_price = int(value_list[i])
                flag1 =1
            elif 'volatility'.lower() in attr and 'of'.lower() in attr and 'price'.lower() in attr:
                reqd_attributes.append([attribute_list[i], value_list[i]])
                volatility = int(value_list[i])
                flag2 =1

        if flag1 ==1 and flag2==1:
            #Forecasted_Price = str(mean_price+(3*volatility))+"/"+str(mean_price+(3*volatility))
            fp1 = mean_price +(3*volatility)
            fp2 = mean_price - (3*volatility)
            Forecasted_Price = str(fp1)+"/"+str(fp2)
            reqd_attributes.append(["Forecasted Price",Forecasted_Price])
        reqd_attributes = [current_stock] + reqd_attributes
        full_list = full_list + [reqd_attributes]
    print("flnew ",full_list)
    for elem in full_list:
        elem.pop(0)
    return full_list


def filter(filename):
    # Stock Growth Rating
    # Financial Health Rating
    print("file",filename)
    df = pd.read_csv("STOCK CSV FILES/"+filename)
    attribute_list = list(df)
    attribute_list = attribute_list[1:52]
    print("attrlist",attribute_list)
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
    #    print("AAAAAAAA",attribute_list)
        for i in range(len(attribute_list)):
            attr=[]
            attr = attribute_list[i].split()

            for j in range(len(attr)):
                attr[j] = attr[j].lower()
            if 'Stock'.lower() in attr and 'Growth'.lower() in attr and 'rating'.lower() in attr:
                reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))), int(float(value_list[i]))])
            elif 'financial'.lower() in attr and 'health'.lower() in attr and 'rating'.lower() in attr:
                reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])), "☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
        reqd_attributes = [current_stock] + reqd_attributes
        full_list = full_list + [reqd_attributes]
    print("full list ",full_list)
    return full_list,date

@app.route('/efef')
def error():
        return render_template("error.html")


def profit(filename):
    df = pd.read_csv("STOCK CSV FILES/"+filename)
    attribute_list = list(df)
    attribute_list = attribute_list[2:52]
    print("atr_list",attribute_list)
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
        attr = []
        for i in range(len(attribute_list)):
            attr=[]
            attr = attribute_list[i].split()
            for j in range(len(attr)):
                attr[j] = attr[j].lower()
            if 'market'.lower() in attr and 'cap' in attr:
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'enterprise'.lower() in attr and 'value' in attr:
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'operating'.lower() in attr and 'margin' in attr:
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'return'.lower() in attr and 'on'.lower() in attr and 'assets'.lower():
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'return'.lower() in attr and 'on'.lower() in attr and 'equity'.lower():
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
        reqd_attributes = [current_stock] + reqd_attributes
        full_list = full_list + [reqd_attributes]
    print("PROFIT",full_list)
    for elem in full_list:
            elem.pop(0)
    return full_list


def revenue(filename):
    df = pd.read_csv("STOCK CSV FILES/"+filename)
    s = {'Revenue (ttm):','Revenue Per Share (ttm):','EBITDA (ttm)6:','Net Income Avl to Common (ttm):','Diluted EPS (ttm):','Total Cash (mrq):','Book Value Per Share (mrq):'}
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
        for i in range(len(attribute_list)):
            attr=[]
            attr = attribute_list[i].split()
            for j in range(len(attr)):
                attr[j] = attr[j].lower()
            if 'Revenue'.lower() in attr and attribute_list[i] in s:
                if attribute_list[i].find("(") != -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'revenue'.lower() in attr and 'per' in attr and 'share' in attr and attribute_list[i] in s:
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'EBITDA'.lower() in attr and attribute_list[i] in s:
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'net'.lower() in attr and 'income'.lower() in attr and 'avl'.lower() in attr and 'to'.lower() in attr and 'common' in attr and attribute_list[i] in s:
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'diluted'.lower() in attr and 'eps'.lower() in attr and attribute_list[i] in s:
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'total'.lower() in attr and 'cash'.lower() in attr and attribute_list[i] in s:
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'book'.lower() in attr and 'value'.lower() in attr and 'per'.lower() in attr and 'share'.lower() in attr and attribute_list[i] in s:
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
        reqd_attributes = [current_stock] + reqd_attributes
        full_list = full_list + [reqd_attributes]
    print("revenue",full_list)
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
    flnew = filter2(filename)
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
    return render_template("first.html", full=full_list1,full3=full_list3, st=stock_names,d=date,sc=sectorsc,fn=sectorname,full4=full_list4,flnew=flnew)


if __name__ == '__main__':

    app.run(debug=True)

