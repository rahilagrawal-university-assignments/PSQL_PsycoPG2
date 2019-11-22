# COMP3311 19T3 Assignment 3

import cs3311
import sys
if len(sys.argv) != 2 :
        course = 'COMP1521'
else:
        course = sys.argv[1]
conn = cs3311.connect()

cur = conn.cursor()

query = "create or replace view courseCE(type, tag, quota, enrolments) as select ct.name, cl.tag, cl.quota, count(ce.class_id) from classtypes ct inner join classes cl on cl.type_id = ct.id inner join class_enrolments ce on ce.class_id = cl.id inner join courses c on c.id = cl.course_id inner join subjects s on c.subject_id = s.id where s.code = '{}'group by ce.class_id, ct.name, cl.tag, cl.quota".format(course)
cur.execute(query);
query = "create or replace view courseCEP(type, tag, percentage) as select type, tag, (CAST (enrolments*1.00/quota*100 AS INTEGER)) as percentage from courseCE order by type, tag, percentage"
cur.execute(query);
query = "select * from courseCEP where percentage < 50"
cur.execute(query);
rows = cur.fetchall()
for row in rows:
    print('{} {} is {}% full'.format(row[0], row[1], row[2]))

cur.close()
conn.close()
