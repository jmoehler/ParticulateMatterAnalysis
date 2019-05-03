import csv
import time

from datetime import datetime

start = time.time()
i=0
o=0

with open('./data/Stuttgart/clear_S-Mitte-SZ-Halbstd-Werte_2019(bis 30.4.).csv',
    'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';')

    for datafile in ['./data/Stuttgart/S-Mitte-SZ-Halbstd-Werte_2019(bis 30.4.).csv',
        './data/Stuttgart/Halbstd-Werte-Stuttgart-Mitte-SZ_1987-2018.csv']:
        with open(datafile,newline = '') as f:
            readers = csv.reader(f, delimiter= ';')
            for row in readers:
                i += 1

                if len(row) < 20:
                    continue
                
                timeStr = row[0]
                try:
                    datetime.strptime(timeStr, '%Y-%m-%d 00:00:00') 
                except: 
                    continue

                try:
                    datetime.strptime(timeStr, '%m/%d/%y') 
                except: 
                    continue

                # csv programm schreiben
                o += 1
                if (o%10000==0):
                    print(o)
                spamwriter.writerow(row)

        f.close()


ende = time.time()
diff = ende-start

print ("wrote %d (of %d) rows" % (o,i))
print("runtime: %.5fs" %(diff)) 
            


