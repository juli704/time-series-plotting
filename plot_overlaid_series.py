from csv import reader
from datetime import datetime
import matplotlib.pyplot as plt
from os.path import join

def string_to_datetime_object(string):

	# Convert timestamps to seconds precision (Prune 8 trailing digits)
	return datetime.fromtimestamp(int(string) / 100000000)

def load_timestamps_and_prices_from_csv_file(
	source_file_path,
	out_list_of_timestamps,
	out_list_of_prices):

	lines = []

	with open(source_file_path, 'r') as f:

        # Create a parsing iterator and skip the CSV header
		parsing_iterator = reader(f, delimiter=',')
		next(parsing_iterator, None)

		for line in parsing_iterator:

			out_list_of_timestamps.append(string_to_datetime_object(line[0]))
			out_list_of_prices.append(float(line[1]))


if __name__ == '__main__':

	### Settings ###

	chart_data_folder = 'stocks/bars/1_day/'
	chart_data_files = [ 'OXGN.csv', 'RYT.csv', 'VOCS.csv' ]


	### Create the plot ###

	for file_name in chart_data_files:

		### Load the timestamps and opening prices from the current file ###

		list_of_timestamps = []
		list_of_prices = []

		source_file_path = join(chart_data_folder, file_name)

		load_timestamps_and_prices_from_csv_file(
			source_file_path,
			list_of_timestamps,
			list_of_prices
		)


		### Write the data to the plot instance ###

		plt.xlabel('Timestamp (Securities Information Processor)')
		plt.ylabel('Price (U.S. Dollars)')

		plt.plot(
			list_of_timestamps,
			list_of_prices,
			linewidth=1,
			markersize=1
		)


	### Show the plot ###

	plt.title('Overlaid Series')
	plt.tight_layout()

	plt.show()
