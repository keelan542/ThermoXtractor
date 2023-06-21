# Import statements
import sys

# Found thermo flag
found_thermo = False

# Thermo data list
thermo_data = []

# Open file and read line by line
try:
	with open(sys.argv[1]) as file:
		for line in file:
			if ' Zero-point correction=' in line:
				found_thermo = True
			elif ' Sum of electronic and thermal Free Energies=' in line:
				found_thermo = False
				print(line)
				thermo_data.append(line.split()[-1])
			elif found_thermo:
				print(line)
				thermo_data.append(line.split()[-1])

	print(thermo_data)

except Exception:
	print('File not found.')
	sys.exit()