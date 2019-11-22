# COMP3311 19T3 Assignment 3

import cs3311
import sys
if len(sys.argv) != 2 :
        term = '19T1'
else:
        term = sys.argv[1]
conn = cs3311.connect()

cur = conn.cursor()
cur.execute("select id from rooms where code like 'K-%'")
roomIds = cur.fetchall()
rooms = len(roomIds)
cur.execute("select (m.end_time-m.start_time) as time, SUBSTRING(m.weeks_binary, 1, 10), r.id from meetings m join rooms r on r.id = m.room_id join classes cl on cl.id = m.class_id join courses c on c.id = cl.course_id join terms t on c.term_id = t.id where t.name = '{}' and r.code like 'K-%' order by r.id".format(term));
rows = cur.fetchall()

def roundHours(hours):
    hours = (hours/100)
    return round(hours*2)/2

hoursDict = {}

for id in roomIds:
    hoursDict[id[0]] = 0

for row in rows:
    hoursDict[row[2]] += roundHours(int(row[0])) * (row[1].count('1'))

nRooms = 0

for item in hoursDict.values():
    if(item >= 200):
        nRooms += 1

nRooms = rooms - nRooms
percentage = round((nRooms * 100 / rooms), 1)
print("{}%".format(percentage))

cur.close()
conn.close()
