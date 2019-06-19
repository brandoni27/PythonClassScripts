# P49_Datamining.py
# Brandon Washington
# 5/22/2019
# Python 3.6
# Description: Data mining project where we read and extract date from spreadsheets.



def get_data_list(FILE_NAME):
    myFile = open(FILE_NAME, 'r')
    listOfLines = myFile.read().splitlines()
    print('numberOfLines', len(listOfLines))
    return listOfLines

def get_monthly_averages(data_list):
    aLine = data_list[1]
    lineItems = aLine.split(',')
    date = lineItems[0]
    data = lineItems[len(lineItems) - 1]
    dateSplit = date.split('-')
    year = dateSplit[0]
    month = dateSplit[1]
    oldMonth = month
    sum = 0
    count = 0
    listOfAverages = []

    for i in range(1, len(data_list), 1):
        aLine = data_list[i]
        lineItems = aLine.split(',')
        date = lineItems[0]
        data = lineItems[len(lineItems) - 1]
        dateSplit = date.split('-')
        year = dateSplit[0]
        month = dateSplit[1]
        if month == oldMonth:
            count = count + 1
            sum = sum + float(data)
            avg = sum / count
        if month != oldMonth or i == 1030:
            subList = [year, oldMonth, avg]
            listOfAverages.append(subList)
            sum = float(data)
            count = 1
            oldMonth = month

    return listOfAverages


def print_info(monthly_average_list):
    finalList = get_monthly_averages(newList)
    for i in range(0,len(finalList),1):
        print(finalList[i])




newList = get_data_list("table.csv")
last = get_monthly_averages(newList)
print_info(last)


'''
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "/Users/Brando/Desktop/Python Code/P49_Datamining.py"
numberOfLines 1031
['2008', '09', 437.7042857142857]
['2008', '08', 485.9066666666667]
['2008', '07', 510.0277272727273]
['2008', '06', 556.3152380952381]
['2008', '05', 575.9180952380952]
['2008', '04', 497.57772727272726]
['2008', '03', 440.334]
['2008', '02', 503.7955]
['2007', '01', 611.8104761904763]
['2007', '12', 695.3980000000003]
['2007', '11', 676.3652380952382]
['2007', '10', 635.3908695652173]
['2007', '09', 540.4268421052631]
['2007', '08', 509.83043478260885]
['2007', '07', 532.4799999999999]
['2007', '06', 515.0209523809524]
['2007', '05', 473.0109090909091]
['2007', '04', 472.49800000000016]
['2007', '03', 452.91181818181826]
['2007', '02', 467.2173684210527]
['2006', '01', 490.581]
['2006', '12', 473.497]
['2006', '11', 485.63238095238097]
['2006', '10', 440.53454545454554]
['2006', '09', 397.062]
['2006', '08', 377.08869565217395]
['2006', '07', 403.5345]
['2006', '06', 393.59363636363634]
['2006', '05', 383.79545454545456]
['2006', '04', 413.7778947368421]
['2006', '03', 358.8682608695653]
['2006', '02', 370.00052631578956]
['2005', '01', 445.7119999999999]
['2005', '12', 418.95190476190476]
['2005', '11', 399.1352380952381]
['2005', '10', 322.4704761904762]
['2005', '09', 304.23952380952375]
['2005', '08', 286.9234782608696]
['2005', '07', 298.2115]
['2005', '06', 287.54545454545456]
['2005', '05', 239.70999999999998]
['2005', '04', 199.21476190476187]
['2005', '03', 181.1581818181818]
['2005', '02', 195.01368421052635]
['2004', '01', 192.846]
['2004', '12', 181.76999999999998]
['2004', '11', 177.4952380952381]
['2004', '10', 153.23095238095237]
['2004', '09', 113.22714285714288]
['2004', '08', 105.26222222222222]

Process finished with exit code 0

'''