import glob
import smtplib
import os
import datetime

#######
#TODO#
######
# Yag mail implementation (add log files too)

####################
# Global variables #
####################
YOUR_GMAIL =
YOUR_GMAIL_PASSWORD = 
# Default value
# program_name = "Sorry, the program name is not specified!"


def main(program_name, error):
	date_and_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	error_logs = check_for_error_log()
	if error_logs == None:
		error_logs = "There is no error logs, sorry!"
	if program_name == None:
		program_name = "There is no Program Name, sorry!"
	if error == None:
		error = "There is no error, sorry!"

	msg = ("An Error has occured!\n"
		   "\nThe error occured at {}"
		   "\nThese are the Error Logs"
		   "\n{}"
		   "\n"
		   "\nThe program which crashed is called {}"
		   "\nThe exact error is {}".format(date_and_time, error_logs, program_name, error))


	send_email(msg)

def check_for_error_log():
	try:
		file = open("log.txt", 'r')
	except Exception as e:
		try:
			file = open("program_log.txt")
		except Exception as e:
			return None

	file_read = file.readlines()
	try:
		file_read = file_read[-30]
		print("30")
	except Exception as e:
		file_read = file_read[-5]

	return None or file_read


def send_email(msg):
	# The actual mail send
	print(msg)
	server = smtplib.SMTP('smtp.gmail.com:587')
	print("started server")
	server.starttls()
	print("start tls")
	server.login(YOUR_GMAIL,YOUR_GMAIL_PASSWORD)
	print("logged in")
	server.sendmail(YOUR_GMAIL, YOUR_GMAIL, msg)
	print("sent")
	server.quit()
