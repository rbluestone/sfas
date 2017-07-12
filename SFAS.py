#-------------------------------------------------------------------------------
# Name:        Tide Gauge Importer
# Purpose:
#
# Author:      rbluestone
#
# Created:     10/05/2017
# Copyright:   (c) rbluestone 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv

# pull data from csv file

def csvreader(csvfile, gaugeID):
    readings = []
    with open(csvfile, 'rb') as sfasRaw:
        reader = csv.reader(sfasRaw)
        for row in reader:
            if row != [] and row[0] != 'DateTime (ET)':
                readings += [[gaugeID, row[0], row[1], row[2], row[3]]]

    return readings

# write data

def csvwriter(folder, readings):
    # pull date range
    sDate = readings[0][1]
    eDate = readings[-1][1]
    # pull gaugeID
    gaugeID = readings[0][0]
    # create name
    csvname = str(folder + '\\' + gaugeID + '__' + str(sDate.replace('-', "_").replace(' ', '_').replace(':', '_')) + '__' + str(eDate.replace('-', "_").replace(' ', '_').replace(':', '_') + '.csv'))
    # write data to csv
    with open(csvname, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter = ',')
        for x in readings:
            filewriter.writerow(x)
    response = "wrote to Dates: " + sDate + " to " + eDate + ",   " + "Gauge: " + gaugeID + ",   " + "File: " + csvname
    return response