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
#option_parser.add_option('--json', default=False, action='store_true',
#  help="Output results in JSON form")
#option_parser.add_option('--pretty', default=False, action='store_true',
#  help="Show human-readable timestamps instead of unix times")

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

#if options.json:
#  values_json = str(values).replace('None','null')
#  print '''{
#    "start" : %d,
#    "end" : %d,
#    "step" : %d,
#    "values" : %s
#  }''' % (start,end,step,values_json)
#  sys.exit(0)

t = start
for value in values:
  #if options.pretty:
  #  timestr = time.ctime(t)
  #else:
  timestr = str(t)
  if value is None:
    next
    #valuestr = "None"
  else:
    valuestr = "%f" % value
    datapoints = [timestr, valuestr]
    print datapoints
    #whisper.update(path2, valuestr, timestr)
    #whisper.update_many(path2, datapoints)
  t += step

#datapoints = [tuple(point.split(':')) for point in datapoint_strings]

#if len(datapoints) == 1:
#  timestamp,value = datapoints[0]
#  whisper.update(path, value, timestamp)
#else:
#  print datapoints
#  whisper.update_many(path, datapoints)

