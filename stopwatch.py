#!usr/bin/python
# Created by Sagar Uprety at Bengaluru, India on May 14th, 2016.
# This is a simple stopwatch utility implemented as shell. Can be used in absence of a smartphone/smartwatch. 
# Run this file using the python command and then see the list of commands to proceed.
# Any comments/suggestions/feedback is welcomed at sagaruprety@gmail.com

import datetime
import time

class stopwatch():
	# Function to display information regarding current lap.
	def display(self, lap_no, time_elapsed):
		print('Lap '+str(lap_no));
		print(time_elapsed);

	# Function to give a list of commands in case one forgets the exact command name.
	def helpme(self):
		print('\nstart - Starts the stopwatch.\nlap   - Signals completion of lap.\nstop  - Stops the watch and exits.\n');

	# Function which does the actual time computation and stopwatch implementation.
	def timer(self):
		user_input  = raw_input('>>> '); # Shell input.

		lap_no  = 0;      	  # Lap number before start.
		format  = '%H:%M:%S'; #format followed for displaying time.

		while (user_input != 'stop'):  # Loop until stop command is entered.
			if(user_input == 'start'): # Start the stopwatch.
				lap_no  = lap_no + 1;
				t_prev = time.time();
				self.display(lap_no, '00:00:00'); 

			elif(user_input == 'lap'): # Lap signalled.
				lap_no  = lap_no + 1;
				t_lap   = time.time();
				t_diff  = t_lap - t_prev;
				time_elapsed = datetime.timedelta(seconds = t_diff); # Gives the time elaspsed between two laps.
				self.display(lap_no, time_elapsed);
				t_prev  = t_lap; # to compute the time elapsed between current lap and the next.

			elif(user_input == 'help'): # help availed.	
				self.helpme();  		# call help function in case user types a wrong command name.

			else: # Incorrect command typed.
				print('Command not found. Type help to get the list of valid commands.');

			user_input  = raw_input('>>> '); # Next action awaited.

		print('----------Thus ends your watch. Thanks for using it!----------');

def main():
	 print('\n ----------This is a stopwatch shell utility, by Sagar Uprety----------\n');
	 s = stopwatch();
	 s.helpme();
	 s.timer();

if __name__ == '__main__':
	main()
