#!/usr/bin/env python
__author__ = 'Klius'
import sys
import argparse

def main(argv):
	parser = argparse.ArgumentParser(description='Here goes Description')
	parser.add_argument("to",help="Destination email address.")
	parser.add_argument("--From",help="Alias for the sender.")
	parser.add_argument("subject", help="Subject of the email.")
	parser.add_argument("--bodyhtml", help="Path of the HTML to use as template for the body of the email.")
	parser.add_argument("--textmessage", help="Text to use as body of the email.")
	args = parser.parse_args()
	
	#Logic ensues!
	if bool( args.bodyhtml ):
		print True
	elif bool( args.textmessage ):
		print True
	else:
		print( "You haven't especified a path to an html nor a plain text body." )
		sys.exit(2)

if __name__ == "__main__":
	main(sys.argv[1:])