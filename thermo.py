# Import statements
import sys
import math

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
				thermo_data.append(float(line.split()[-2]))
			elif ' Sum of electronic and thermal Free Energies=' in line:
				found_thermo = False
				thermo_data.append(float(line.split()[-1]))
			elif found_thermo:
				thermo_data.append(float(line.split()[-1]))

	# Building formatted string so that thermochemistry can be displayed in an easy to read manner
	formatted_data = 'E(Electronic)\tE(+ZPE)\t\tE(Enthalpy)\tE(Gibbs)\tE(ZPVE)\t\tE(G0>298)\n{}\t{}\t{}\t{}\t{}\t{}'

	# Inserting approporiate data into formatted string, formatted_data and printing
	print(formatted_data.format(round(thermo_data[4] - thermo_data[0], 6),
								round(thermo_data[4], 6),
								round(thermo_data[6], 6),
								round(thermo_data[7], 6),
								round(thermo_data[0], 6),
								round(thermo_data[3], 6)))

except Exception as e:
	print('File not found.')
	sys.exit()