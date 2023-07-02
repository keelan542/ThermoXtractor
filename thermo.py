# Import statements
import sys
import math
import os

# Found thermo flag
found_thermo = False

energies = []

try:
	# Print header
	print('{:30s}E(Electronic)\tE(+ZPE)\t\tE(Enthalpy)\tE(Gibbs)\tE(ZPVE)\t\tE(G0>298)\n'.format(' '))

	# Looping through files in current directory
	for current_file in os.listdir():

		# Check if current_file is a .log Gaussian output file
		if current_file.endswith('.log'):
			
			# Thermo data list
			thermo_data = []

			# Open the current_file that has been determined as a .log Gaussian output file
			with open(current_file) as file:
				for line in file:
					if 'SCF Done' in line:
						energies.append(float(line.split()[4]))

					if ' Zero-point correction=' in line:
						found_thermo = True
						thermo_data.append(float(line.split()[-2]))
					elif ' Sum of electronic and thermal Free Energies=' in line:
						found_thermo = False
						thermo_data.append(float(line.split()[-1]))
					elif found_thermo:
						thermo_data.append(float(line.split()[-1]))

			# Building formatted string so that thermochemistry can be displayed in an easy to read manner
			formatted_data = '{:30s}{:.6f} \t{:.6f}\t{:.6f}\t{:.6f}\t{:.6f}\t{:.6f}'

			# Inserting approporiate data into formatted string, formatted_data and printing
			current_file = current_file[:-4]
			if len(current_file) > 30:
				current_file = current_file[:30]

			if len(thermo_data) > 0:
				print(formatted_data.format(current_file,
											energies[-1],
											thermo_data[4],
											thermo_data[6],
											thermo_data[7],
											thermo_data[0],
											thermo_data[3]))
			else:
				print(formatted_data.format(current_file, energies[-1], 0.0, 0.0, 0.0, 0.0, 0.0))

except Exception:
	print('No .log files found.')
	sys.exit()