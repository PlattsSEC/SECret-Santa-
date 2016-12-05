#Secret Santa Algorithm


import random




def parseEmails(guests):
    fobj = open(guests, 'r')
    data = fobj.read().decode("utf-8-sig").encode("utf-8")
    emails = {}
    doods = data.split('\n')
    del doods[-1]

    for i in doods:
        p = i.split(',')
        p[0] = p[0][1:-1]
        emails[p[0]] = p[1] + '@plattsburgh.edu'

    return emails



def match(friends, dicManBaby):
    random.shuffle(friends)
    for i in range(len(friends) - 1):
        dicManBaby[friends[i]] = friends[i + 1]
    dicManBaby[friends[-1]] = friends[0]    
    return dicManBaby


            

guestFile = 'guestList.txt'
a = parseEmails(guestFile)

b = a.values()

matches = {}

c = match(b, matches)

for key, value in c.iteritems():
    print key, value


