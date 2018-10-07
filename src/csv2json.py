#!/usr/bin/python

import sys, getopt
import csv
import json
import os
import logging
import datetime
import time

# python csv2json.py C:\\Test\\PurchaseOrders.csv PurchaseOrders.dat 

#Get Command Line Arguments
def main(argv):
    input_file = 'PurchaseOrders.csv'
    output_file = 'PurchaseOrders.dat '
    format = ''
       
    logging.basicConfig(filename='C:\\Test\\csv2json.log', filemode='w',level=logging.INFO)

    try:
        logging.info("*************************************************************")
        logging.info('Script started at : %s' %time.strftime("%Y/%d/%m %H:%M:%S"))
        os.remove(output_file)
        logging.info ("Existing File has been deleted.....")

    except OSError:
        pass    
        logging.info("Script started at--------- ",datetime.datetime.now())
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","format="])
    except getopt.GetoptError:
        print ('csv2json.py -i <path to inputfile> -o <path to outputfile> -f <dump/userformat>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('csv2json.py -i <path to inputfile> -o <path to outputfile> -f <dump/userformat>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-f", "--format"):
            format = arg
    read_csv(input_file, output_file, format)
    logging.info('Script completed at : %s' %time.strftime("%Y/%d/%m %H:%M:%S"))
    print ("File generate with JSON format : ",output_file) 
    

#Read CSV File
def read_csv(inputfile, json_file, format):
    csv_rows = []
    with open(inputfile) as csvfile:
        file_csv = csv.DictReader(csvfile)
        # title = file_csv.fieldnames
        print ("columns are : ",file_csv.fieldnames)
        output = ''
        rec_count=0
        logging.info("Converting the data into JSON format" )
        for row in file_csv:
            # print (row[file_csv.fieldnames[0]] + '|' + row[file_csv.fieldnames[1]])
            # csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
            csv_col = row[file_csv.fieldnames[0]] + '|' + row[file_csv.fieldnames[1]] + '|' #+ json.dumps(row)
            rec_count=rec_count+1
            
            csv_col = csv_col.rstrip(',')
            write_json(csv_col,row, json_file, format)
        print ("Total number of records in file is : ",rec_count)  
        logging.info("Records count : %s" % (rec_count) )

#Convert csv data into json and write it
def write_json(csv_col,data, json_file, format):
    with open(json_file, "a") as f:
        if format == "userformat":
            f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
            # f.write(json.dumps(data, sort_keys=True, separators=(',', ': '),encoding="utf-8",ensure_ascii=False))
            # json.dump(data, json_file)
            # json_file.write('\n')
        else:
            # f.truncate()
            
            csv_col = csv_col.rstrip(',')
            f.write(csv_col+json.dumps(data)+'\n')
            # f.write('\n')
    f.close()

if __name__ == "__main__":
   main(sys.argv[1:])
