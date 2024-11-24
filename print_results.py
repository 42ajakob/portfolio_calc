def print_results(a_weight, total_interest):
	print("WARNING! less precise because each ETFs tracking can start and end on different times + the markets had different highs lows in different times!")
	print("Recommending that you use the same start date and end date for each portfolio to get a precise result!")
	for i in range(len(a_weight)):
		print(f"ETF[{i + 1}] weight: {a_weight[i] * 100:.2f}%")
	#  | Annual rate: {annual_rate[i] * 100:.2f}%
	if a_weight:
		print(f"Annual rate of combined ETFs weight based on each ETFs annual rates: {total_interest * 100:.2f}%")

def print_res(annual_rate, weight):
	print("WARNING! This one is ONLY correct if every ETF has the same starting date and end date!")
	for i in range(len(weight)):
		print(f"ETF[{i + 1}] weight: {weight[i] * 100:.2f}%")
	print(f"Annual rate of combined ETFs weight based on each ETFs total return: {annual_rate * 100:.2f}%")