# COMP3311 19T3 Assignment 3

import cs3311
import sys

if len(sys.argv) != 2 :
        course = 'ENGG'
else:
        course = sys.argv[1]
conn = cs3311.connect()

cur = conn.cursor()
query = "create or replace view buildingCodes(building, course) as select distinct b.name, s.code from buildings b inner join rooms r on b.id = r.within inner join meetings m on m.room_id = r.id inner join classes cl on cl.id = m.class_id inner join courses c on c.id = cl.course_id inner join subjects s on s.id = c.subject_id inner join terms t on c.term_id = t.id where s.code like '{}%' and t.name = '19T2' order by b.name, s.code".format(course);
cur.execute(query);
query = "select building, string_agg(course, ' ') from buildingCodes group by building"
cur.execute(query);
rows = cur.fetchall()
for row in rows:
	if len(row[1].split(' ')) == 0:
		next
	print(row[0])
	for courseCode in row[1].split(' '):
		print(' {}'.format(courseCode))

cur.close()
conn.close()
