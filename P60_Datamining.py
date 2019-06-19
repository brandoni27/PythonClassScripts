


myFile = open('table.csv','r')
listOfLines = myFile.read().splitlines()
print('numberOfLines', len(listOfLines))
print(listOfLines[0])
print(listOfLines[1])
print(listOfLines[len(listOfLines)-1])
#  ONE LINE ONLY
aLine = listOfLines[1]
print(aLine)
lineItems = aLine.split(',')
print(lineItems)
data = lineItems[len(lineItems)-1]
date = lineItems[ 0].split('-')year = date[0]
oldMonth = date[1]
print('data=',data)
print('date=',date)
print('year=', year)
print('oldMonth=',oldMonth)
##############
sum = 0
count = 0
for i in range(1, 17, 1):aLine = listOfLines[i]
print(aLine)
lineItems = aLine.split(',')
print(lineItems)
data = lineItems[len(lineItems)-1]

date = lineItems[ 0].split('-')year = date[0]
curMonth = date[1]
print('data=',data)
print('date=',date)
print('year=', year)
print('month=',month)
if oldMonth == curMonth:
    sum += float(data)
    count += 1
    if oldMonth != curMonth:
# or if you are at the end of the file
#  show the results
#  reset the sum
#  reset the counter
#  make old month equal new month
#  RESULTS
print('sum=', sum)
print('count=',count)
avg = sum/count
print('avg=',avg)
