# Import statements
import sys
import math
import os

# Found thermo flag
found_thermo = False

try:
	# Print header
	print('\n\tE(Electronic)\tE(+ZPE)\t\tE(Enthalpy)\tE(Gibbs)\tE(ZPVE)\t\tE(G0>298)\n')

	# Looping through files in current directory
	for current_file in os.listdir():

		# Check if current_file is a .log Gaussian output file
		if current_file.endswith('.log'):
			
			# Thermo data list
			thermo_data = []

			# Open the current_file that has been determined as a .log Gaussian output file
			with open(current_file) as file:
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
			formatted_data = '{}\t{}\t{}\t{}\t{}\t{}\t{}'

			# Inserting approporiate data into formatted string, formatted_data and printing
			print(formatted_data.format(current_file[:-4],
										round(thermo_data[4] - thermo_data[0], 6),
										round(thermo_data[4], 6),
										round(thermo_data[6], 6),
										round(thermo_data[7], 6),
										round(thermo_data[0], 6),
										round(thermo_data[3], 6)))

except Exception:
	print('An error has occured.')
	sys.exit()