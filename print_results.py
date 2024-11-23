def print_results(total_interest, etfs_weight, annual_rate):
	for i in range(len(etfs_weight)):
		print(f"ETF[{i + 1}] weight: {etfs_weight[i] * 100:.2f}%")
	print(f"Total interest of weight: {total_interest * 100:.2f}%")
	for i in range(len(annual_rate)):
		print(f"Annual rate: {annual_rate[i] * 100:.2f}%")
	print()