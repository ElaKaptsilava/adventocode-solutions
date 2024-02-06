import csv
import os

filename = 'aapl.csv'
field = ['username', 'password', 'email']
d = ['axzxvzd', 'azvxb sd', 'zxsd']

with open(filename, 'a', newline='\n') as f:
    if os.path.getsize(filename) == 0:
        csvwriter = csv.DictWriter(f, fieldnames=field)
        csvwriter.writeheader()
    csvwriter = csv.writer(f)
    csvwriter.writerow(d)
print(os.path.getsize(filename))
