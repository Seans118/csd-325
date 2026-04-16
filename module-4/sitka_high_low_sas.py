import csv
from datetime import datetime

from matplotlib import pyplot as plt

# program loop
again = 'yes'
while again.lower() == 'yes':
    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Menu options
        choice = input('See highs, lows, or exit?')
        if choice.lower() == 'highs' or choice.lower() == 'lows':
            temp_type = choice.lower()
        else:
            print("Goodbye!")
            exit()
        
        # Get dates and temperatures from this file.
        dates, temps = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)

            if temp_type == 'highs':
                temp = int(row[5])
            else:
                temp = int(row[6])
            temps.append(temp)
        
        # Plot the temperatures. Red for highs, blue for lows.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        if temp_type == 'highs':
            c = 'red'
        else:
            c = 'blue'
        ax.plot(dates, temps, c)

        # Format Plot
        plt.title(f"daily {choice.rstrip('s')} temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()

        again = input('Would you like to try again? (yes/no)')