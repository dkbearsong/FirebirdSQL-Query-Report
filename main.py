import firebirdsql as fbs #firebird script
import csv

#appears this library is meant for Firebird 2.0+. Need to find one for Firebird 1.5

hs = input('Please enter the host name: ')
db = input('Please enter the full path to the fdb file to scan for errors: ')
outfile = open('SQLReport.csv', 'a')

con = fbs.connect(host=hs,
    databse=db,
    port=3050,
    user='SYSADMIN',
    password='XXXXXXXX')# database connection string
cur = con.cursor()

def SQL_report(con, query):
    cur.execute(query)
    result = cur.fetchall()
    return result

def saveFile(desc, header, data, flout):
# returns the output of chartrack to csv file and prints to screen
    flout.write(desc + '\n' + header + '\n')
    file_writer = csv.writer(flout, delimiter=',', lineterminator='\n', quotechar='"')
    for row in data:
        file_writer.writerow(row)
    flout.write('\n\n')
    return()

# List for all the SQL queries to be ran. Each entry should be a sublist containing the description at [0], the column headers for the query
# at [1], and the actual SQL query at [2]
SQL_list = []

for i in SQL_list:
    result = SQL_report(con, i[2])
    saveFile(i[0], i[1], result, outfile)
con.close()
outfile.close()
