from flask import Flask,render_template,redirect,url_for
import pandas as pd
import os

app = Flask(__name__)

path = "STOCK CSV FILES"

def filter2(filename):

    print("file",filename)
    df = pd.read_csv(path + "/" + filename)
    attribute_list = list(df)
    attribute_list = attribute_list[1:] #all the attribute-names saved in the list, parallel to which their values will be saved in a separate list(value_list)
    full_list = []
    f = open(path + "/" + filename)
    count = 0
    for line in f:      # this 'line' corresponds to a single row in the file i.e values for a paricular stock code. 'f' is the file object.
        count += 1
        if count == 1: # to skip the first line which is the attribute names
            continue
        reqd_attributes = []
        value_list = line.split(",")
        current_stock = value_list.pop(0) # this give the value of the stock being scanned in this iteration
        value_list = value_list[0:]        # all the values are stored parallel to the attributes list
        i = 0
        for i in range(len(attribute_list)):     #iterating through the attributes list and trying to find the match for required columns
            if 'percentage' in attribute_list[i].lower() and 'price' in attribute_list[i].lower() and 'change' in attribute_list[i].lower():
                reqd_attributes.append([attribute_list[i], value_list[i]])  #once we get the matching attribute we get its value at the same index in the list 'value_list'
            elif 'close' in attribute_list[i].lower():
                reqd_attributes.append([attribute_list[i], value_list[i]])
            elif 'mean' in attribute_list[i].lower() and 'price' in attribute_list[i].lower():
                reqd_attributes.append(["Mean Price", value_list[i]])
            elif 'volatility' in attribute_list[i].lower() and 'of' in attribute_list[i].lower() and 'price' in attribute_list[i].lower():
                reqd_attributes.append([attribute_list[i], value_list[i]])
            elif 'forecasted' in attribute_list[i].lower() and 'price' in attribute_list[i].lower() and 'high' in attribute_list[i].lower():
                reqd_attributes.append(["Max Forecasted Price", value_list[i]])
            elif 'forecasted' in attribute_list[i].lower() and 'price' in attribute_list[i].lower() and 'low' in attribute_list[i].lower():
                reqd_attributes.append(["Min Forecasted Price", value_list[i]])
        reqd_attributes = [current_stock] + reqd_attributes
        full_list = full_list + [reqd_attributes]
    for elem in full_list:
        elem.pop(0)
    return full_list


def filter(filename):
    df = pd.read_csv(path + "/" + filename)
    attribute_list = list(df)
    attribute_list = attribute_list[1:]
    full_list = []
    f = open(path + "/" + filename)
    count = 0
    date = []
    for line in f:
        count += 1
        if count == 1:
            continue
        reqd_attributes = []
        value_list = line.split(",")
        current_stock = value_list.pop(0)
        value_list = value_list[0:]
        for k in range(len(attribute_list)):
            if attribute_list[k].lower() == 'startdate':
                date.append(value_list[k])
        for j in range(len(attribute_list)):
            if attribute_list[j].lower() == 'enddate':
                date.append(value_list[j])
        for i in range(len(attribute_list)):
            if 'stock' in attribute_list[i].lower() and 'growth' in attribute_list[i].lower() and 'rating' in attribute_list[i].lower():
                reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))), int(float(value_list[i]))])
            elif 'financial' in attribute_list[i].lower() and 'health' in attribute_list[i].lower() and 'rating' in attribute_list[i].lower():
                reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])), "☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
        reqd_attributes = [current_stock] + reqd_attributes
        full_list = full_list + [reqd_attributes]
    print("full list ",full_list)
    return full_list,date

def profit(filename):
    df = pd.read_csv(path + "/" + filename)
    attribute_list = list(df)
    attribute_list = attribute_list[1:]
    full_list = []
    f = open(path + "/" + filename)
    count = 0
    s = {""}
    for line in f:
        count += 1
        if count == 1:
            continue
        reqd_attributes = []
        value_list = line.split(",")
        current_stock = value_list.pop(0)
        value_list = value_list[0:]
        i = 0
        for i in range(len(attribute_list)):
            if 'market' in attribute_list[i].lower() and 'cap' in attribute_list[i].lower():
                if value_list[i] == '':
                    value_list[i] = 0
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'enterprise' in attribute_list[i].lower() and 'value' in attribute_list[i].lower() and attribute_list[i].lower()=="Enterprise Value".lower():
                if value_list[i] == '':
                    value_list[i] = 0
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'operating' in attribute_list[i].lower() and 'margin' in attribute_list[i].lower():
                if value_list[i] == '':
                    value_list[i] = 0
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'return' in attribute_list[i].lower() and 'on' in attribute_list[i].lower() and 'assets' in attribute_list[i].lower():
                if value_list[i] == '':
                    value_list[i] = 0
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'return' in attribute_list[i].lower() and 'on' in attribute_list[i].lower() and 'equity' in attribute_list[i].lower():
                if value_list[i] == '':
                    value_list[i] = 0
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
    df = pd.read_csv(path + "/" + filename)
    s = {'Revenue (ttm):','Revenue Per Share (ttm):','EBITDA (ttm)6:','Net Income Avl to Common (ttm):','Diluted EPS (ttm):','Total Cash (mrq):','Book Value Per Share (mrq):'}
    attribute_list = list(df)
    attribute_list = attribute_list[1:]
    full_list = []
    f = open(path + "/" + filename)
    count = 0
    for line in f:
        count += 1
        if count == 1:
            continue
        reqd_attributes = []
        value_list = line.split(",")
        current_stock = value_list.pop(0)
        value_list = value_list[0:]
        for i in range(len(attribute_list)):
            if 'revenue'.lower() in attribute_list[i].lower() and attribute_list[i] in s:
                if value_list[i] == '':
                    value_list[i] = 0
                if attribute_list[i].find("(") != -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'revenue'.lower() in attribute_list[i].lower() and 'per' in attribute_list[i].lower() and 'share' in attribute_list[i].lower() and attribute_list[i] in s:
                if value_list[i] == '':
                    value_list[i] = 0
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'EBITDA'.lower() in attribute_list[i].lower() and attribute_list[i] in s:
                if value_list[i] == '':
                    value_list[i] = 0
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'net'.lower() in attribute_list[i].lower() and 'income'.lower() in attribute_list[i].lower() and 'avl'.lower() in attribute_list[i].lower() and 'to'.lower() in attribute_list[i].lower() and 'common' in attribute_list[i].lower() and attribute_list[i] in s:
                if value_list[i] == '':
                    value_list[i] = 0
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'diluted'.lower() in attribute_list[i].lower() and 'eps'.lower() in attribute_list[i].lower() and attribute_list[i] in s:
                if value_list[i] == '':
                    value_list[i] = 0
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'total'.lower() in attribute_list[i].lower() and 'cash'.lower() in attribute_list[i].lower() and attribute_list[i] in s:
                if value_list[i] == '':
                    value_list[i] = 0
                if attribute_list[i].find("(")!= -1:
                    reqd_attributes.append([attribute_list[i][:attribute_list[i].find("(")],"★ "*int(float(value_list[i])),"☆ "*(10 - int(float(value_list[i]))),int(float(value_list[i]))])
                else:
                    reqd_attributes.append([attribute_list[i],"★ "*int(float(value_list[i])),"☆ "*(10-int(float(value_list[i]))),int(float(value_list[i]))])
            elif 'book'.lower() in attribute_list[i].lower() and 'value'.lower() in attribute_list[i].lower() and 'per'.lower() in attribute_list[i].lower() and 'share'.lower() in attribute_list[i].lower() and attribute_list[i] in s:
                if value_list[i] == '':
                    value_list[i] = 0
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
    all_files = os.listdir(path)
    requested_file = filename
    for file in all_files:
        name = file[:-4]
        if requested_file.lower() in name.lower():
            filename = file
            break
    return filename


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<filename>')
def file(filename):
    try:
        industry_names = {'ConsDis': 'Consumer Discretionary','Energy':'Energy','Utilities':'Utilities', 'ConsStap': 'Consumer Staples','IT': 'Information Technology', 'LargeCap': 'Large Cap', 'MediumCap': 'Medium Cap','SmallCap': 'Small Cap', 'Tele': 'Telecommunication','Industrial':'Industrial','Finance':'Finance','Material': 'Material','Healthcare':'Healthcare'}
        sectorname = industry_names[filename]
        filename = get_file_name(filename)
        full_list1,date = filter(filename)
        stock_names=[]
        flnew = filter2(filename)
        f = filename.split('_')
        full_list3=profit(filename)
        full_list4 = revenue(filename)
    # fore = forecast(filename)
        for elem in full_list1:
            stock_names.append(elem.pop(0))
        return render_template("first.html", full=full_list1,full3=full_list3, st=stock_names,d=date,fn=sectorname,full4=full_list4,flnew=flnew)
    except(FileNotFoundError):
        return render_template("index2.html", sec = sectorname,flag=1)
    except Exception as e:
        return render_template("index2.html",excep=e,flag=2)


if __name__ == '__main__':

    app.run(debug=True)
