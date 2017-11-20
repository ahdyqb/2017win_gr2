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

from __future__ import division
from math import fabs
from random import gauss
from time import sleep

class Turbulence:
	def __init__(self,st_dev=30.0):
		self.tilt_backlog = []
		self.st_dev = st_dev
	
	def get_new_tilt(self):
		tilt = gauss(0.0,self.st_dev)
		self.tilt_backlog.append(tilt)
		if len(self.tilt_backlog) > 100:
			del self.tilt_backlog[0]
		return tilt

class Airplane:
	def __init__(self,wind_st_dev=30.0,pilot_st_dev=5.0):
		self.wind = Turbulence(wind_st_dev)
		self.pilot_st_dev = pilot_st_dev
		self.roll_backlog = [ 0.0 ]
		self.correction_backlog = []
		self.starting_roll = 0.0
		self.current_roll = 0.0
		self.iteration = 0
	
	def print_status(self):
		print 'Step {0:d}'.format(self.iteration)
		print 'Initial roll: {0:2.3f} degrees'.format(self.starting_roll)
		print 'Turbulence change: {0:2.3f}'.format(self.wind.tilt_backlog[-1])
		print 'Compensation: {0:2.1f} %'.format(self.correction_backlog[-1])
		print 'Final roll: {0:2.3f} degrees'.format(self.current_roll)
		
	def apply_wind(self):
		tilt = self.wind.get_new_tilt()
		self.current_roll += tilt
	
	def get_compensation(self):
		fix = gauss(-self.current_roll,self.pilot_st_dev)
		self.correction_backlog.append(fabs(fix/self.current_roll)*100)
		if len(self.correction_backlog) > 100:
			del self.correction_backlog[0]
		self.current_roll += fix
	
	def run_iteration(self):
		self.iteration += 1
		self.starting_roll = self.roll_backlog[-1]
		self.apply_wind()
		self.get_compensation()
		self.roll_backlog.append(self.current_roll)
		if len(self.roll_backlog) > 100:
			del self.roll_backlog[0]
		self.print_status()
		

if __name__=='__main__':
	print 'Simple flight simulation.\n'
	print 'Input standard deviation for wind tilt (default: 30.0 deg)'
	wind_stdev = 30.0
	user_input_wind_stdev = raw_input()
	if user_input_wind_stdev:
		try:
			wind_stdev = float(user_input_wind_stdev)
		except ValueError:
			print 'Incorrect input. Setting the value to default.\n'
	
	print 'Input standard deviation for pilot correction (default: 5.0 deg)'
	pilot_stdev = 5.0
	user_input_pilot_stdev = raw_input()
	if user_input_pilot_stdev:
		try:
			pilot_stdev = float(user_input_pilot_stdev)
		except ValueError:
			print 'Incorrect input. Setting the value to default.\n'
	
	airplane = Airplane(wind_stdev,pilot_stdev)
	
	print 'All ready. Starting simulation.\n'
	sleep(1)
	
	try:
		while True:
			airplane.run_iteration()
			sleep(2)
	except KeyboardInterrupt:
		print '\nProgram stopped.'
		sleep(0.5)
		print 'Final simulation status:'
		sleep(0.5)
		airplane.print_status()

#Jakub Ahaddad
#github username ahdyqb
