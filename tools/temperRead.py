#!/usr/bin/env python
# TODO: Move to django command
import re
import subprocess
import sys
import pymysql

try:
    text = subprocess.check_output('pcsensor')
except Exception, e:
    sys.exit(1)

temp = re.search('(\d{2}\.\d{2})C', text).groups()

conn = pymysql.connect(user='minxy', passwd='umpalumpa', db='Minxy', host='192.168.178.50')
cur = conn.cursor()
cur.execute('insert into flatcontrol_tempsensor (time, temp) values (now(), %s)' % (temp))
conn.commit()
conn.close()
