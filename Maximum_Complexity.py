print ('hello world')

# This will be the most complex program I have written so far.
# It will have:
#	variables
#	strings
#		string manipulations
#			.lower() .upper() .title() .capitalize()?
#	methods
#	booleans
#	if-else statemens
#	parameters
#	comparison operators
#		'<'  '>'  '>='  '<='  '=='   '!='

#This will be a basic TRPG. Amazing adventures and exciting experiences.

##############################################################################

import time

###VARIABLES###

##BASICS##
HP = 100
MONEY = 0
##BASICS##

#WEAPONS AND GEAR#
    #For example: 0=no weapon, 10=weak weapon, 200=strong weapon
SWORD = 0

PROTECTIVE_GEAR = SHIELD + HELMET
SHIELD = 0
HELMET = 0

#WEAPONS AND GEAR#


##############################################################################

#Story management: the basic method I used was a function which had if-else branches, which called other functions, which called other functions.
#Death: it should be handled with a While loop at the beginning, like: 'While HP > 0:'

#Make a wait() function with a configurable parameter, like: wait(1) or wait(2).
#Source: https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
def wait(sec):
    time.sleep(sec)

def test_wait():
    print('1')
    wait(1)
    print('2')
    wait(2)
    print('3')
    wait(3)

#test_wait()

#Riddles, see below:

def riddle_sun():
    print("Here's a riddle for you:")
    answer = input("A shining disk in the sky, it is shining but we don't know why.").lower()
    if 'sun' in answer:
        print("Well done.")
    else:
        print("Wrong answer.")

riddle_sun()
