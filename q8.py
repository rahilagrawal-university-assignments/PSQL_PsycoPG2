# COMP3311 19T3 Assignment 3

import cs3311
import sys

# Get the subjects from Command Line
if len(sys.argv) < 2 :
    courses = ['COMP1511', 'MATH1131']
else:
    courses = []
    for i in range (1, len(sys.argv)):
        courses.append(sys.argv[i])

# Create SQL Query to get all classes
coursesString = "s.code in ('{}'".format(courses[0])
if len(courses) > 1:
    for i in range(1, len(courses)):
        coursesString += ",'{}'".format(courses[i])
coursesString += ")"

# Connect to Database
conn = cs3311.connect()
cur = conn.cursor()

# Get subjects that have only 1 lecture stream and total types of classes for each course
lectureStreams = {}
courseClasses = {course: [] for course in courses}

for course in courses:
    cur.execute("select count (distinct cl.tag) from classes cl join classtypes ct on ct.id = cl.type_id join  courses c on cl.course_id = c.id join terms t on t.id = c.term_id join subjects s on s.id = c.subject_id join meetings m on m.class_id = cl.id where ct.name = 'Lecture' and t.name = '19T3' and s.code = '{}'".format(course))
    lectureStreams[course] = (cur.fetchall()[0])[0]	
    cur.execute("select distinct ct.name from classes cl join classtypes ct on ct.id = cl.type_id join  courses c on cl.course_id = c.id join terms t on t.id = c.term_id join subjects s on s.id = c.subject_id join meetings m on m.class_id = cl.id where t.name = '19T3' and s.code = '{}'".format(course))
    for c in cur.fetchall():
        courseClasses[course].append(c[0])	

# Get all classes
cur.execute("select s.code, ct.name, m.day, m.start_time, m.end_time, cl.tag from classes cl join classtypes ct on ct.id = cl.type_id join  courses c on cl.course_id = c.id join terms t on t.id = c.term_id join subjects s on s.id = c.subject_id join meetings m on m.class_id = cl.id where t.name = '19T3' and {} order by s.code, m.day, ct.name, m.start_time".format(coursesString))
rows = cur.fetchall()

# Create Timetable
timetable = {day: [] for day in ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')}

# Fix lectures that only have 1 stream
for row in rows:
    subj, classType, day, start, end, tag = row[0], row[1], row[2], row[3], row[4], row[5]
    if(classType == 'Lecture' and lectureStreams[subj] == 1):
        timetable[day].append(("{} {}: {}-{}".format(subj, classType, start, end), start, end))        
        #total_hours += round((end - start)/100 * 2)/2
        if classType in courseClasses[subj]:
            courseClasses[subj].remove(classType)

def noClash(day, start, end):
    for classes in timetable[day]:
        if (start <= classes[1] <= end) or (start <= classes[2] <= end):
            return False
    return True

# Fix lectures that have more than 1 stream
for i in range(len(rows)):
    row = rows[i]
    subj, classType, day, start, end, tag = row[0], row[1], row[2], row[3], row[4], row[5]
    
    # do not add same lectures again
    if(classType == 'Lecture' and lectureStreams[subj] == 1):
        continue

    # Do not add if this type has been added
    if(classType not in courseClasses[subj]):
        continue

    # Add classes for this type
    temp = {day: [] for day in ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')}
    temp_hours = 0
    addClasses = True
    for j in range(len(rows)):
         sRow = rows[j]
         if sRow[5] == tag and sRow[0] == subj:
            if noClash(sRow[2], sRow[3], sRow[4]):
                 temp[sRow[2]].append(("{} {}: {}-{}".format(subj, classType, sRow[3], sRow[4]), sRow[3], sRow[4]))
            else:
                addClasses = False
                break
    if addClasses:
        for key in temp.keys():
            for classes in temp[key]:
                timetable[key].append(classes)
        if classType in courseClasses[subj]:
            courseClasses[subj].remove(classType)

# count hours             
total_hours = 0

for day in timetable.keys():
    if(len(timetable[day]) == 0):
        continue
    times = sorted(timetable[day], key=lambda x: x[1])
    start = (times[0])[1]
    end = (times[len(times) - 1])[2]
    total_hours += round((end - start) / 100 * 2) / 2   
    total_hours +=  2

print("Total hours: {}".format(total_hours))

m = ["Mon", "Tue", "Wed", "Thu", "Fri"]

for day in sorted(timetable.keys(), key=m.index):
    if(len(timetable[day]) == 0):
        continue
    print("  ",day)
    for classes in sorted(timetable[day], key=lambda x: x[1]):
        print("    ",classes[0]) 

cur.close()
conn.close()
