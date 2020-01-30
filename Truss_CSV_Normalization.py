import sys, csv, datetime, pytz
from argparse import ArgumentParser


#Handles formatting timestamp to ISO8601 and changes TimeZone
#TODO: Split this, this function does multiple things, which is generally not great
#Assumption listed in ReadMe made here
def timestampManipulation(data):
    
    dateTimeFormatted = datetime.datetime.strptime(data, "%m/%d/%y %H:%M:%S %p")

    #assigns all timestamps to Pacific
    timezonePST = pytz.timezone("America/Los_Angeles")
    dateTimeFormattedPST = timezonePST.localize(dateTimeFormatted)
        
    timezoneEST = pytz.timezone("America/New_York")
    dateTimeFormattedEST = dateTimeFormattedPST.astimezone(timezoneEST)
    
    return dateTimeFormattedEST

#Pads leading 0s to zipcode
def zipCodeManipulation(data):

    return str(data).zfill(5)

#Changes all letters to uppercase
#Assumption listed in ReadMe made here 
def fullNameConversion(data):

    return data.upper()

#Converts duration into seconds
def durationConversion(data):

    h, m, s = [float(i) for i in data.split(':')]
    return 3600.0*h + 60.0*m + s


#creating the parsers    
parser = ArgumentParser()                                                                 
parser.add_argument('fname', metavar='FILE', help='Please provide an input file to process')
parser.add_argument('newName', metavar="FILE", help='Please provide an output file name')
args = parser.parse_args()

#opening the input file
with open(args.fname, encoding='utf-8', errors='replace') as f:
    readCSV = csv.reader(f, delimiter=',')
    data = []

    #grabbing header
    header = next(readCSV, None)
    for row in readCSV:
        data.append(row)
        #print(row)

    #Disposing of Header Data
    data.pop(0)

#iterating through data for manipulation
for row in data:

    #calling for timestamp conversions
    row[0] = timestampManipulation(row[0])
    #print(row[0])

    #reminding myself of addresses
    #row[1] 
    #print(row[1])

    #calling for zipcode manipulation
    row[2] = zipCodeManipulation(row[2])
    #print(row[2])
    
    #calling for FullName conversion
    row[3] = fullNameConversion(row[3])
    #print(row[3])

    #calling for fooDuration conversion
    row[4] = durationConversion(row[4])
    #print(row[4])

    #calling for barDuration conversion    
    row[5] = durationConversion(row[5])
    #print(row[5])
    
    #calling for totalDuration mathiness
    row[6] = row[4] + row[5] #will be added to be totalDuration
    #print(row[6])

    #reminding myself of notes
    #row[7] 
    #print(row[7])

#opening the output file
#TODO: Not seeing proper replacement characters in all .csv displaying programs
#TODO: Remove broken rows!
with open(args.newName, mode='w', encoding='utf-8', errors='replace',  newline='') as n:
    writeCSV = csv.writer(n, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    writeCSV.writerow(header)
    #print(header)

    #iterating through data for file
    for r in data:
        writeCSV.writerow(r)
        #print(r)
        

