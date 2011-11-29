#!/usr/bin/python
import time
import datetime
import sys
#
# script calculates the time sind epoch (1970-01-01 00:00am UTC)
#

if len(sys.argv) < 2:
        print "Usage: %s 2011-10-25 [19:30:00]" % (sys.argv[0])
        sys.exit(1)
elif len(sys.argv) !=3:
	u_time = "00:00:00"
else:
	 u_time = sys.argv[2]
  
u_date = sys.argv[1]
u_input = "%s %s"  % (u_date, u_time)
print "epoch for given time: \t %s" % (int(time.mktime(time.strptime(u_input, '%Y-%m-%d %H:%M:%S'))))
now = int( time.time() )
print "epoch timezone: \t %s" % (now)

