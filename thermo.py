# Import statements
import sys

# Found thermo flag
found_thermo = False

# Open file and read line by line
try:
	with open(sys.argv[1]) as file:
		for line in file:
			if ' Zero-point correction=' in line:
				found_thermo = True
			elif ' Sum of electronic and thermal Free Energies=' in line:
				found_thermo = False
				print(line)

			if found_thermo:
				print(line)

except Exception:
	print('File not found.')
	sys.exit()