#!/bin/python

def plot(date, weight):
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy import stats
    prevdays = 31
    medindex = len(weight)/2
    q1 = weight[int(medindex/2)]
    q3 = weight[int(3*medindex/2)]
    k=1.5
    lower,upper=(q3-k*(q1-q3), q1+k*(q1-q3))
    newweight, newdate  = zip(*[(i,j) for (i,j) in zip(weight, date) if i>=lower and i<=upper])

    slope, intercept, r, p, std_err = stats.linregress(range(0,len(newdate)), newweight)
    average=[intercept + slope*i  for i in range(0, len(newdate))]
    # plt.plot(newdate, newweight, "ko-", newdate, expectnewweight, "bo-",  newdate, expectHigh, "g-",newdate, expectLow, "r-")
    dayleft = int((190-intercept)/slope  )
    plt.title(f"There are {dayleft} days left appoxmaitly until you're a chad")
    # plt.fill_between(newdate, expectLow, expectHigh, alpha=.5, facecolor='blue')
    tmpdate=newdate[len(newdate)-prevdays:len(newdate)] 
    expectnewweight=[sum(newweight[len(newweight)-prevdays:len(newweight)])/prevdays -i/7 for i in range(0, prevdays)]
    # plt.plot(newdate, newweight, "ko-",   newdate, average, "-k", tmpdate, expectnewweight, "-b")
    tmpRANGE = lambda i: i[len(i)-prevdays:len(i)]
    plt.plot(tmpRANGE(newdate), tmpRANGE(newweight), "ko-",   tmpRANGE(newdate), tmpRANGE(average), "-k", tmpdate, expectnewweight, "-b")
    plt.fill_between(tmpdate, expectnewweight, max(newweight), alpha=.5, facecolor='red')
    plt.fill_between(tmpdate, expectnewweight, min(newweight), alpha=.5, facecolor='green')
    plt.ylabel('expectnewweight in lBS')
    plt.xlabel('newdate')
    plt.grid()
    plt.show()
def getWeight():
    import dmenu
    weight = dmenu.show('', lines=25, case_insensitive=False, prompt="Enter your weight 🎂")
    return weight
def addEntry(weight):
    import csv
    import datetime
    with open('/home/zaki/.local/share/Weight.csv', 'a+') as file:
        write = csv.writer(file)
        write.writerow([datetime.date.today().strftime("%D"), weight] )
def read():
    import csv
    date=[]
    weight=[]
    with open('/home/zaki/.local/share/Weight.csv', 'r') as file:
        read = csv.reader(file)
        for row in read:
            date.append(row[0])
            weight.append(float(row[1]))
    return (date, weight)
def run():
    _weight=getWeight()
    if(_weight != None):
        addEntry(_weight)
        date, weight = read()
        plot(date, weight)


run()

# date , weight = read()
# plot(date, weight)
