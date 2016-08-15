import sys
import time

print "processing...\\",
syms = ['\\', '|', '/', '-']
bs = '\b'

for i in range(10):
    for sym in syms:
        sys.stdout.write("\b%s" % sym)
        sys.stdout.flush()
        time.sleep(.5)
