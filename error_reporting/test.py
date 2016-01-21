import error_logging
import logging
program_name = "test.py"
# imports the loggign module, creates a logging file called "ProgramLog.txt"
logging.basicConfig(filename='log.txt', level=logging.DEBUG,
					format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug("Start of program")
a = 1
logging.debug(a)
b = 0
logging.debug(b)
logging.debug("Trying to divide by 0")
logging.debug("wtf is this 5 yet")
logging.debug("yes!!!")

error = "zero divison"
error_logging.main(program_name, error)

