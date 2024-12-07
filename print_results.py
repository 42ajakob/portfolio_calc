def print_warning():
	print("WARNING! Bad precision! Read README.md!")

def print_results(weight, total_interest, ann_rate_interest, ann_rate, ann_rate_weight, money):
	for i in range(len(weight)):
		print(f"ETF[{i + 1}] annual rate: {ann_rate[i] * 100:.2f}% | weight: {weight[i] * 100:.2f}% | annual rate weighted: {ann_rate_weight[i] * 100:.2f}% | money: {money * weight[i]:.2f}")
	if weight:
		print(f"Total interest of portfolio: {total_interest * 100:.2f}%")
		print(f"Annual rate of portfolio: {ann_rate_interest * 100:.2f}%")