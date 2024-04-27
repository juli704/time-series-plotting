import csv
import matplotlib.pyplot as plt

from datetime import datetime
from tqdm import tqdm

def plot_bar_csv_file(csv_file_path):

    ### Load the file's columns into memory ###

    timestamp_column = []
    open_column = []
    high_column  = []
    low_column = []
    close_column  = []
    volume_column  = []

    with open(csv_file_path, 'r') as csv_file:

        # Create a parsing iterator and skip the CSV header
        parsing_iterator = csv.reader(csv_file, delimiter=',')
        next(parsing_iterator, None)

        for line in tqdm(parsing_iterator):

            # Convert timestamps to seconds precision (Prune 8 trailing digits)
            timestamp_column.append(datetime.fromtimestamp(int(line[0]) / 100000000))

            open_column.append(float(line[1]))
            high_column.append(float(line[2]))
            low_column.append(float(line[3]))
            close_column.append(float(line[4]))
            volume_column.append(float(line[5]))


    ### Plot the data ###

    # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html#stacking-subplots-in-one-direction

    fig, (ax1, ax2) = plt.subplots(
        2,
        height_ratios=(0.7, 0.1),
        num='plot_bar_series.py'
    )

    fig.suptitle(csv_file_path)

    # Plot the price column
    ax1.plot(
        timestamp_column,
        open_column,
        linewidth=1,
        markersize=1,
        color='green',
        label='Open price'
    )

    ax1.set_ylabel('Price (U.S. Dollars)')

    ax1.legend()

    # Plot the volume column
    ax2.plot(
        timestamp_column,
        volume_column,
        linewidth=1,
        markersize=1,
        color='green',
        label='Volume'
    )

    ax2.set_xlabel('Timestamp (Securities Information Processor)')
    ax2.set_ylabel('Shares')

    ax2.legend()
    plt.show()


if __name__ == '__main__':

    plot_bar_csv_file('stocks/bars/1_day/VOCS.csv')