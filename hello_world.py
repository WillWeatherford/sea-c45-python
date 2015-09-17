import sys

lang = 'English'

if len(sys.argv) > 1:
    lang = sys.argv[1]

if lang == 'English':
    print 'Hello, world.'

elif lang == 'binary':
    print '01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100 00100001'



else:
    raise RuntimeError("This shouldn't happen!")
