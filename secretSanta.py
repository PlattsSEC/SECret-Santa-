# secret santa boiii
# poppin pills wit a poppin bitch boiiiiii

# urBoi Justin Grizzle. in the hizzle. Don't get it fuckin
#twizzled



#Secret Santa Algorithm


import random


people = ['JustinTheAwesome', 'TylerTheBitch', 'DannyTheGay', 'AlexTheFuckboy',
          'PrithajTheTurtle']
dicManBaby = {}

def match(friends, dicManBaby):
    random.shuffle(friends)
    #print friends
    for i in range(len(friends) - 1):
        #print friends[i]
        dicManBaby[friends[i]] = friends[i + 1]
    #print friends[-1]
    #print friends[0]
    dicManBaby[friends[-1]] = friends[0]    
    return dicManBaby
            
        


a = match(people, dicManBaby)

for key, value in a.iteritems():
    print key,value
