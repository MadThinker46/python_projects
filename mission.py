import random

print"""\n\nDuring WWII, a bomber crew had a 1/4 chance of being 
shot down on each mission. A man had to fly ten 
missions, before being allowed to return home.

What was the survival rate as missions progressed?\n"""

starting_men = 100000
surviving_men = starting_men

print "A total of",starting_men,"started at the begining"

for mission in range(1,11):
    trials = surviving_men
    while (trials >= 1):
        trials = trials -1
        chance = random.randrange(4) 
        if (chance < 1):
                surviving_men = surviving_men -1
    print "Only total",surviving_men,"surived through mission",mission,
    print "giving a survival rate of",100*surviving_men/starting_men,"%."
print "\nWar is hell."

