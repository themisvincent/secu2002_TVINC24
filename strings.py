mystr = "david,themis,sharim"
print len('david,themis,sharim')
print len(mystr)
mystr1 = "icecream"
mystr2 = "shit"
print mystr1+mystr2
print mystr[2]
print 't' in mystr
print mystr[0:len(mystr)]
print mystr.index('t')
print mystr.count('i')
long_str = '''line1\tline2\tline3'''
print "trying list operations on strings for testing below"
print mystr.remove(4)
print mystr.sort()
try:
    mystr7 = [1,2,3,4]
    for x in range(0,6):
        print mystr7[x]
except:
    print ‘error: went past end of string’
