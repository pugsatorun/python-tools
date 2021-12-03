import csv
import sys
 
with open(sys.argv[1], 'r', newline='') as filein, \
        open('out.csv', 'w', newline='') as fileout:
 
        reader = csv.reader(filein, delimiter=' ', skipinitialspace=True)
        writer = csv.writer(fileout)
 
        writer.writerows(reader)

#print('file_out.csvへの出力完了')