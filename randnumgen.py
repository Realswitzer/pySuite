#!/usr/bin/env python3
import random, sys, getopt, platform
import dearpygui.dearpygui as dpg

def infloop():
	a = input("Enter the first number of the range that you want the number generator to generate: ")
	b = input("Enter the second number of the range that you want the number generator to generate: ")
	try:
		print('Here is your random number from',a,'to',b,":",(random.randint(int(a), int(b))))
	except ValueError:
		print("Variable(s) contained non-integers!\n")
		infloop()
	c = input(("Would you like to generate another random number? (y/n)\n"))
	if c == ("y" or "yes"):
		infloop()
	elif c == ("n" or "no" or "exit" or "quit" or "q"):
		exit()

#def dpgfunc():
#	# pysuite#4
#	range1 = 0
#	range2 = 0
#
#	def rand_gen(s=None, data=None):
#		r = 0
#		try:
#			r = random.randint(range1, range2)
#		except Exception:
#			dpg.set_value("rand", "(invalid)")
#			return
#		dpg.set_value("rand", str(r))
#
#	def rand_cb(s, data):
#		print(globals())
#		if not s in globals():
#			raise ValueError("invalid sender " + s)
#		globals()[s] = data
#		rand_gen()
#
#	dpg.create_context()
#
#	with dpg.window(tag="rng", label="Random Generator"):
#		with dpg.group(tag="rgroup", width=200, horizontal=True):
#			dpg.add_text("Range:")
#			dpg.add_input_int(tag="range1", callback=rand_cb)
#			dpg.add_text("-")
#			dpg.add_input_int(tag="range2", callback=rand_cb)
#		with dpg.group(tag="result", horizontal=True):
#			dpg.add_text("Output:")
#			dpg.add_text(tag="rand", default_value="(uninitialized)")
#		dpg.add_button(label="Regenerate", callback=rand_gen)
#
#	dpg.create_viewport(width=640, height=480)
#	dpg.setup_dearpygui()
#	dpg.set_primary_window("rng", True)
#	dpg.show_viewport()
#	dpg.start_dearpygui()
#	dpg.destroy_context()

# I skidded most of the code below. Manually typed, don't know why.
# https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# Enjoy I guess. -swiss cheese

def main(argv):
	a = ''
	b = ''
	try:
		opts, args = getopt.getopt(argv,"hn:x:",["help","min=","max=","headless"])
	except getopt.GetoptError:
		print("I don't know how you triggered the opt error, but here we are. Exiting")
		exit()
	if opts == []:
		print("No arguments! Launching GUI version...because apparently #4 exists")
		#if platform.system() == 'Darwin':
		#	print("Sorry, dearpygui doesn't seem to work on Mac, at least for me (developer).")
		#	print("I hope that pygame works, but there's no implementation of that.")
		#	print("Please use --headless (cli gui-thing) or --help for other options. -switz")
		#	exit(1)
		#exec(open("randomnumbergenerator.py").read())
		print("Sorry, the GUI doesn't work. Just use --headless or --help for options")
		exit()
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print('Usage: [file name] [args]')
			print('args: ')
			print('')
			print('   -n --min <minimum value>')
			print('   -x --max <maximum value>')
			exit()
		elif opt in ("-n", "--min"):
			a = str(arg)
		elif opt in ("-x", "--max"):
			b = str(arg)
		elif opt == "--headless":
			infloop()
	try:
		print('Here is your random number from',a,'to',b,':',(random.randint(int(a), int(b))))
	except ValueError:
		print("Variable(s) contained non-integers!\n")
		exit()
	exit()


if __name__ == "__main__":
	main(sys.argv[1:])
