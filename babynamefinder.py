import sqlite3
import csv

con = sqlite3.connect('babynames.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS babynames")
cur.execute("CREATE TABLE IF NOT EXISTS babynames (year int, name text, percent real, sex text)")
con.commit()
con.close()

# load data
csvfile = open('data/baby-names.csv','r')
reader = csv.DictReader(csvfile)
data = [row for row in reader]
csvfile.close()

# clean data
for d in data:
    d['year'] = int(d['year'])
    d['percent'] = float(d['percent'])

# format data
nameDict = {}
for d in data:
    if d['name'] in nameDict:
        if d['percent'] > 0.03:
            nameDict[d['name']] = nameDict[d['name']] + 1
    else:
        nameDict[d['name']] = 0
        if d['percent'] > 0.03:
            nameDict[d['name']] = nameDict[d['name']] + 1

# insert in table
con = sqlite3.connect('babynames.db')
cur = con.cursor()
for d in data:
  cur.execute("INSERT INTO babynames VALUES(?,?,?,?)",tuple(d.values()))
con.commit()
con.close()

print(nameDict)
