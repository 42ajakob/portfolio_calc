def print_warning():
	print("WARNING! less precise because of the different [start_date] and [end_date] accross all ETFs!")
	print("RECOMMEND to use the same [start_date] and [end_date] across all ETFs to get a precise result!")

def print_results(weight, ann_rate_interest, ann_rate, ann_rate_weight):
	for i in range(len(weight)):
		print(f"ETF[{i + 1}] annual rate without weight: {ann_rate[i] * 100:.2f}%")
		print(f"ETF[{i + 1}] weight: {weight[i] * 100:.2f}% annual rate with weight: {ann_rate_weight[i] * 100:.2f}%")
	if weight:
		print(f"Annual rate of combined ETFs weight based on each ETFs annual rates: {ann_rate_interest * 100:.2f}%")