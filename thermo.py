# Import statements
import sys

# Open file and read line by line
try:
	with open(sys.argv[1]) as file:
		for line in file:
			if ' - Thermochemistry -' in line:
				print('Found Thermochemistry')
except Exception:
	print('File not found.')
	sys.exit()