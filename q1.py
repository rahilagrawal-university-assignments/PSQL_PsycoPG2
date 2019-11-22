# COMP3311 19T3 Assignment 3

import cs3311
conn = cs3311.connect()

cur = conn.cursor()

cur.execute("""SELECT course, CAST(((enrolments * 1.00 /quota) * 100) AS INTEGER) as percentage from courseQuota where enrolments > quota""")
rows = cur.fetchall()

for row in rows:
    print('{} {}%'.format(row[0],row[1]))

cur.close()
conn.close()
