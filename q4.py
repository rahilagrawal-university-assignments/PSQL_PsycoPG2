# COMP3311 19T3 Assignment 3

import cs3311
import sys
if len(sys.argv) != 2 :
        course = 'ENGG'
else:
        course = sys.argv[1]
conn = cs3311.connect()

cur = conn.cursor()

query = "select t.name, s.code, count(e.course_id) from terms t inner join courses c on c.term_id = t.id inner join subjects s on s.id = c.subject_id inner join course_enrolments e on e.course_id = c.id where s.code like '{}%' group by e.course_id, t.name, s.code order by t.name, s.code".format(course)
cur.execute(query);
rows = cur.fetchall()
currCourse = ""
for row in rows:
	if row[0] != currCourse:
		currCourse = row[0]
		print(row[0])
	print(' {}({})'.format(row[1], row[2]))

cur.close()
conn.close()
