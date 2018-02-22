
import datetime

def helloworld(name=None, date=None):
	"""
	Print "hello world" or "hello {name}" and possibly today's date
	"""

	if name != None:
	    print("Hello {}!".format(name))
	else:
	    print("Hello world!")

	if date:
		date = datetime.datetime.today().strftime("%B %d, %Y")
		print("Today's date is " + date)
