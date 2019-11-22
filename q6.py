# COMP3311 19T3 Assignment 3

import cs3311
import re
conn = cs3311.connect()

cur = conn.cursor()

def getWeeks(weeks):
    weeks = weeks.replace('1-2', '1,2')
    weeks = weeks.replace('1-3', '1,2,3')
    weeks = weeks.replace('1-4', '1,2,3,4')
    weeks = weeks.replace('1-5', '1,2,3,4,5')
    weeks = weeks.replace('1-6', '1,2,3,4,5,6')
    weeks = weeks.replace('1-7', '1,2,3,4,5,6,7')
    weeks = weeks.replace('1-8', '1,2,3,4,5,6,7,8')
    weeks = weeks.replace('1-9', '1,2,3,4,5,6,7,8,9')
    weeks = weeks.replace('1-10', '1,2,3,4,5,6,7,8,9,10')
    weeks = weeks.replace('1-11', '1,2,3,4,5,6,7,8,9,11')
    weeks = weeks.replace('2-3', '2,3')
    weeks = weeks.replace('2-4', '2,3,4')
    weeks = weeks.replace('2-5', '2,3,4,5')
    weeks = weeks.replace('2-6', '2,3,4,5,6')
    weeks = weeks.replace('2-7', '2,3,4,5,6,7')
    weeks = weeks.replace('2-8', '2,3,4,5,6,7,8')
    weeks = weeks.replace('2-9', '2,3,4,5,6,7,8,9')
    weeks = weeks.replace('2-10', '2,3,4,5,6,7,8,9,10')
    weeks = weeks.replace('2-11', '2,3,4,5,6,7,8,9,10,11')
    weeks = weeks.replace('3-4', '3,4')
    weeks = weeks.replace('3-5', '3,4,5')
    weeks = weeks.replace('3-6', '3,4,5,6')
    weeks = weeks.replace('3-7', '3,4,5,6,7')
    weeks = weeks.replace('3-8', '3,4,5,6,7,8')
    weeks = weeks.replace('3-9', '3,4,5,6,7,8,9')
    weeks = weeks.replace('3-10', '3,4,5,6,7,8,9,10')
    weeks = weeks.replace('3-11', '3,4,5,6,7,8,9,10,11')
    weeks = weeks.replace('4-5', '4,5')
    weeks = weeks.replace('4-6', '4,5,6')
    weeks = weeks.replace('4-7', '4,5,6,7')
    weeks = weeks.replace('4-8', '4,5,6,7,8')
    weeks = weeks.replace('4-9', '4,5,6,7,8,9')
    weeks = weeks.replace('4-10', '4,5,6,7,8,9,10')
    weeks = weeks.replace('4-11', '4,5,6,7,8,9,10,11')
    weeks = weeks.replace('5-6', '5,6')
    weeks = weeks.replace('5-7', '5,6,7')
    weeks = weeks.replace('5-8', '5,6,7,8')
    weeks = weeks.replace('5-9', '5,6,7,8,9')
    weeks = weeks.replace('5-10', '5,6,7,8,9,10')
    weeks = weeks.replace('5-11', '5,6,7,8,9,10,11')
    weeks = weeks.replace('6-7', '6,7')
    weeks = weeks.replace('6-8', '6,7,8')
    weeks = weeks.replace('6-9', '6,7,8,9')
    weeks = weeks.replace('6-10', '6,7,8,9,10')
    weeks = weeks.replace('6-11', '6,7,8,9,10,11')
    weeks = weeks.replace('7-8', '7,8')
    weeks = weeks.replace('7-9', '7,8,9')
    weeks = weeks.replace('7-10', '7,8,9,10')
    weeks = weeks.replace('7-11', '7,8,9,10,11')
    weeks = weeks.replace('8-9', '8,9')
    weeks = weeks.replace('8-10', '8,9,10')
    weeks = weeks.replace('8-11', '8,9,10,11')
    weeks = weeks.replace('9-10', '9,10')
    weeks = weeks.replace('9-11', '9,10,11')
    weeks = weeks.replace('10-11', '10,11')
    #print(weeks)
    return weeks

query = "select id, weeks from meetings order by id"
cur.execute(query);
rows = cur.fetchall()
updates = []
for row in rows:
    week = row[1]
    binaryStr = ""
    if 'N' in week or '<' in week:
        #updates.append("UPDATE meetings SET weeks_binary = '00000000000' WHERE id = {};".format(row[0]))
        cur.execute("UPDATE meetings SET weeks_binary = '00000000000' WHERE id = {};".format(row[0]))
        continue
    week = getWeeks(row[1])
    if  '1,' in week or (week[0] == '1' and len(week) == 1):
        binaryStr += "1"
    else: 
        binaryStr += "0"
    if '2' in week:
        binaryStr += "1"
    else:
        binaryStr += "0"
    if '3' in week:
        binaryStr += "1"
    else:
        binaryStr += "0"
    if '4' in week:
        binaryStr += "1"
    else:
        binaryStr += "0"
    if '5' in week:
        binaryStr += "1"
    else:
        binaryStr += "0"
    if '6' in week:
        binaryStr += "1"
    else:
        binaryStr += "0"
    if '7' in week:
        binaryStr += "1"
    else:
        binaryStr += "0"
    if '8' in week:
        binaryStr += "1"
    else:
        binaryStr += "0"
    if '9' in week:
        binaryStr += "1"
    else:
        binaryStr += "0"
    if '10' in week:
        binaryStr += "1"
    else:
        binaryStr += "0"
    if '11' in week:
        binaryStr += "1"
    else:
        binaryStr += "0"
    #updates.append("UPDATE meetings SET weeks_binary = '{}' WHERE id = {};".format(binaryStr, row[0]))
    cur.execute("UPDATE meetings SET weeks_binary = '{}' WHERE id = {};".format(binaryStr, row[0]))
    
#for update in updates:
#    print(update)
conn.commit()
cur.close()
conn.close()
