# COMP3311 19T3 Assignment 3

import cs3311
import sys
if len(sys.argv) != 2 :
	courseLen = 2
else:
	courseLen = int(sys.argv[1])

conn = cs3311.connect()

cur = conn.cursor()

cur.execute("""select digits, string_agg(subj, ' ') from courseDigits group by digits order by digits""");
rows = cur.fetchall()
for row in rows:
	if(len(row[1].split(' ')) == courseLen):
		print('{}: {}'.format(row[0],row[1]))

cur.close()
conn.close()
