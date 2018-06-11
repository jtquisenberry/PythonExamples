# http://stackabuse.com/command-line-arguments-in-python/

import sys # Required to get arguments.

# count the arguments
arguments = sys.argv
arguments_count = len(sys.argv) - 1

# output argument-wise
position = 1
while (arguments_count >= position):
    #print ("parameter %i: %s" % (position, sys.argv[position]))
    print('Parameter is {0} {1}'.format(sys.argv[position], 'abc'))
    position = position + 1

