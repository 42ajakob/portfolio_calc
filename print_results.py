def print_results(total_interest, etfs_weight, annual_rate):
	for i in range(len(etfs_weight)):
		print(f"ETF[{i + 1}] weight: {etfs_weight[i] * 100:.2f}% | Annual rate: {annual_rate[i] * 100:.2f}%")
	if etfs_weight:
		print(f"Annual rate of combined ETFs weight based on each ETFs annual rates: {total_interest * 100:.2f}%")

def print_res(total_annual_rate_precise):
	print("WARNING! This one is ONLY correct if every ETF has the same starting date and end date!")
	print(f"Annual rate of combined ETFs weight based on each ETFs total return: {total_annual_rate_precise * 100:.2f}%")