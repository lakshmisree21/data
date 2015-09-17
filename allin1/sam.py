import sys

for arg in sys.argv:
	print  arg
	webbrowser.open(arg[1:, ])