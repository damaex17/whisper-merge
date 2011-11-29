#!/usr/bin/python

import sys, time
import whisper
from optparse import OptionParser

now = int( time.time() )
epoch = 0

option_parser = OptionParser(usage='''%prog [options] path1 path2''')
option_parser.add_option('--from', default=epoch, type='int', dest='_from',
  help=("Unix epoch time of the beginning of "
        "your requested interval (default: 24 hours ago)"))
option_parser.add_option('--until', default=now, type='int',
  help="Unix epoch time of the end of your requested interval (default: now)")

(options, args) = option_parser.parse_args()

if len(args) != 2:
  option_parser.print_usage()
  sys.exit(1)

path1 = args[0]
path2 = args[1]

from_time = int( options._from )
until_time = int( options.until )


(timeInfo, values) = whisper.fetch(path1, from_time, until_time)
(start,end,step) = timeInfo

t = start
for value in values:
  timestr = str(t)
  if value is None:
    next
    #valuestr = "None"
  else:
    valuestr = "%f" % value
    datapoints = [timestr, valuestr]
    print datapoints
    whisper.update(path2, valuestr, timestr)
  t += step
