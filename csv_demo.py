import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "text_folder/data.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column in enumerate(header_row):
        print(index, column)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates,highs,lows=[],[],[]

    for row in reader:
        try:
            date = datetime.strptime(row[2],'%Y-%m-%d')
        except ValueError:
            print(f"Incorrect date -- {row[2]}")
        else:
            highs.append(row[5])
            lows.append(row[6])
            dates.append(date)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red',alpha=0.5)
    ax.plot(dates,lows,c='blue',alpha=0.5)
    ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
    ax.set_title('High Temp', fontsize=24)
    ax.set_xlabel("Date", fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Tempeture", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
