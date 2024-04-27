from csv import reader
from datetime import datetime
from tqdm import tqdm

import matplotlib.pyplot as plt

def plot_quote_csv_file(quote_csv_file_path):

    ### Load the file's columns into memory ###

    timestamp_column = []
    ask_price_column = []
    ask_size_column  = []
    bid_price_column = []
    bid_size_column  = []

    with open(quote_csv_file_path, 'r') as csv_file:

        # Create a parsing iterator and skip the CSV header
        parsing_iterator = reader(csv_file, delimiter=',')
        next(parsing_iterator, None)

        # For every line of the file
        for line in tqdm(parsing_iterator):

            # Convert timestamps to seconds precision (Prune 9 trailing digits)
            timestamp_column.append(datetime.fromtimestamp(int(line[0]) / 1000000000))

            ask_price_column.append(float(line[1]))
            ask_size_column.append(int(line[2]))
            bid_price_column.append(float(line[3]))
            bid_size_column.append(int(line[4]))


    ### Plot the data ###

    # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html#stacking-subplots-in-one-direction

    fig, (ax1, ax2) = plt.subplots(
        2,
        height_ratios=(0.7, 0.1),
        num='plot_quote_series.py'
    )

    fig.suptitle(quote_csv_file_path)

    # Plot the ask price column
    ax1.plot(
        timestamp_column,
        ask_price_column,
        linewidth=1,
        markersize=1,
        color='green',
        label='Ask price'
    )

    # Plot the bid price column
    ax1.plot(
        timestamp_column,
        bid_price_column,
        linewidth=1,
        markersize=1,
        color='blue',
        label='Bid price'
    )

    ax1.set_ylabel('Price (U.S. Dollars)')

    ax1.legend()

    # Plot the ask size column
    ax2.plot(
        timestamp_column,
        ask_size_column,
        linewidth=1,
        markersize=1,
        color='green',
        label='Ask size'
    )

    # Plot the bid size column
    ax2.plot(
        timestamp_column,
        bid_size_column,
        linewidth=1,
        markersize=1,
        color='blue',
        label='Bid size'
    )

    ax2.set_xlabel('Timestamp (Securities Information Processor)')
    ax2.set_ylabel('Shares')

    ax2.legend()
    plt.show()

if __name__ == '__main__':

    plot_quote_csv_file('stocks/quotes/HTBX.csv')