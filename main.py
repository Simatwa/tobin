#!/usr/bin/python3
def error_handler():
	def decorator(func):
		def main(*args,**kwargs):
			try:
				return func(*args,**kwargs)
			except Exception as e:
				from sys import exit
				exit(f'Error  : {e if not len(e.args)>1 else e.args[1]}')
		return main
	return decorator

@error_handler()				
def to_bin(text):
	# Convert each character to its ASCII code and then to binary
	binary_list = [bin(ord(char))[2:].zfill(8) for char in text]
	# Join the binary strings together with a space between each byte
	binary_string = " ".join(binary_list)
	#print("The text represents the following binary string: ")
	return binary_string
	
@error_handler()	
def to_text(binary_string):
	binary_string="".join(binary_string.split(' '))
	# Split the binary string into groups of 8 bits
	byte_list = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
	# Convert each byte from binary to decimal and then to ASCII character
	text = ""
	for byte in byte_list:
	   decimal = int(byte, 2)
	   character = chr(decimal)
	   text += character
	return text;print(text)
	
@error_handler()
def get_content(fnm):
	with open(fnm) as fh:
		return fh.read()
			
@error_handler()		
def main():
	import argparse
	from os import getlogin
	last_shot=to_bin("Hello "+getlogin())
	parser=argparse.ArgumentParser(description="Convert text to binary and vice versa",epilog="\n".join([last_shot,to_text(last_shot)]))
	parser.add_argument('message',nargs='?',help='Message to be converted')
	parser.add_argument('-f','--file',help='Path to file containing message')
	parser.add_argument('-b','--bin',help='Convert message to binary',action='store_true', dest='to_bin')
	args=parser.parse_args()
	msg=args.message if not args.file else get_content(args.file)
	if not msg:
		raise Exception("Pass filepath or message")
	if args.to_bin:
	  fd=(to_bin(msg))
	else:
	  fd=(to_text(msg))
	print(f"\033[32m{fd}\033[0m")

if __name__=='__main__':
	  main()
