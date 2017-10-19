#!/usr/bin/env python2

###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#If you have spare time you can implement: Command Line Interface, generators, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck


#will generate random angles from normal distribution around 0.0
#	with st.dev of 30 deg.
#fix will be applied analogously, with the mean at -angle and st.dev of 5.0

from random import gauss
from time import sleep

print("Keyboard Interrupt (CTRL+C) to stop.")

angle = 0.0
i = 1

while True:
	print("Starting step {0:d}\nInitial angle: {1:2.3f} deg.".format(i,angle))
	tilt = gauss(0.0,30.0)
	angle += tilt
	print( "Tilting by {0:2.3f} deg.\nCurrent angle: {1:2.3f}".format(tilt,angle) )
	fix = gauss(-angle,5.0)	#centered around minus current angle
									#so it already gives a compensating value
	print( "Applying fixing tilt of {:2.3f} deg.".format(fix) )
	angle += fix
	print( "Angle at the end of the step: {:2.3f}\n".format(angle) )

	print("Reminder: To stop the program, please do a keyboard interrupt (CTRL+C)")
	i += 1
	sleep(2)

#Jakub Ahaddad
#github username ahdyqb
