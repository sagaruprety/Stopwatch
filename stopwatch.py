#!usr/bin/python
# Created by Sagar Uprety at Bengaluru, India on May 14th, 2016.
# This is a simple stopwatch utility implemented as shell. Can be used in absence of a smartphone/smartwatch. 
# Run this file using the python command and then see the list of commands to proceed.
# Any comments/suggestions/feedback is welcomed at sagaruprety@gmail.com

import datetime
import time
from config import conf_exit_message
from config import conf_welcome_message
from config import conf_help_message

class stopwatch():
	# Function to display information regarding current lap.
	def display(self, lap_no, time_elapsed):
		print('Lap '+str(lap_no));
		print(time_elapsed);

	# Function to give a list of commands in case one forgets the exact command name.
	def helpme(self):
		print(conf_help_message);

	# Function which does the actual time computation and stopwatch implementation.
	def timer(self):
		user_input  = 'start'; 				 # Shell input default.

		lap_no  = 0;      	   				 # Lap number before start.
		format  = '%H:%M:%S';  				 # format followed for displaying time.
		t_prev  = time.time(); 				 # default time starts with the start of the app.

		while (user_input != 'stop'):  	     # Loop until stop command is entered.
			user_input  = raw_input('>>> '); # Shell input from user.
			if (user_input == 'start'):      # Start the stopwatch.
				lap_no  = lap_no + 1;
				t_prev  = time.time();
				self.display(lap_no, '00:00:00'); 

			elif (user_input == 'lap'): 	 # Lap signalled.
				lap_no  = lap_no + 1;
				t_lap   = time.time();
				t_diff  = t_lap - t_prev;
				time_elapsed = datetime.timedelta(seconds = t_diff); # Gives the time elaspsed between two laps.
				self.display(lap_no, time_elapsed);
				t_prev  = t_lap; 			 # to compute the time elapsed between current lap and the next.

			elif (user_input == 'help'): 	 # Help availed.	
				self.helpme();  		 	 # Call help function in case user types a wrong command name.

			elif (user_input == 'stop'): 	 # Quitting the stopwatch.
				t_lap   = time.time();
				t_diff  = t_lap - t_prev;
				time_elapsed = datetime.timedelta(seconds = t_diff); # Gives the time elaspsed between two laps.
				self.display(time_elapsed, conf_exit_message);

			elif (user_input == 'license'):  # Displaying the license agreement.
				f = open('LICENSE', 'r');
				for line in f.readlines():
					print line;
				f.close();

			else: 							 # Incorrect command typed.
				print('Command not found. Type help to get the list of valid commands.');

		

def main():
	print(conf_welcome_message);
	s = stopwatch();
	s.helpme();
	s.timer();

if __name__ == '__main__':
	main()