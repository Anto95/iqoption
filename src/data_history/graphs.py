import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import shutil

# Generate graphs with data trend with day of the week as a title
# Todo: Adapt to all the months of the year

def get_graphs():
	if len(sys.argv) == 2:
	  ticker_data = pd.read_csv("../../price_dataset/" + sys.argv[1] + ".csv", index_col = 0)
	else:
	  ticker_data = pd.read_csv("../resources/price_dataset/AAPL.csv", index_col = 0)

	fig_path = "../resources/graphs"
	if(os.path.isdir(fig_path)):
		shutil.rmtree(fig_path)
		os.mkdir(fig_path)

	days = "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31".split()
	names = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
	for cnt, day in enumerate(days):
		if cnt < 16:
			data = ticker_data[ticker_data.index <= "2020-01-" + days[cnt+1]]
			data = data[data.index >= "2020-01-" + day]
			plt.plot(data.values)
			plt.title(names[cnt%7])
			plt.savefig(os.path.join(fig_path, day + "_" + names[cnt%7]) + ".png")
			plt.close()

if __name__ == "__main__":
	get_graphs()