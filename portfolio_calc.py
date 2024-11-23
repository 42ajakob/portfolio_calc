def allocate_list(size):
	return [0.0] * size

def get_int(msg):
	while True:
		try:
			return int(input(msg))
		except ValueError:
			continue

def get_etf(i):
	while True:
		try:
			return float(input(f"ETF[{i + 1}] total return: "))
		except ValueError:
			continue

def calc_all_returns(etfs, etfs_alloc_percent):
	etf_sum = sum(etfs)
	total_return = 0.0

	for i in range(len(etfs)):
		etfs_alloc_percent[i] = etfs[i] / etf_sum
		total_return += etfs[i] * etfs_alloc_percent[i]
		print(f"ETF[{i + 1}] weight: {etfs_alloc_percent[i]:.2f}%")

	return total_return

def calc_yearly_interest(total_return, yearly):
	interest_decimal = total_return / 100
	yearly_interest = (1 + interest_decimal) ** (1 / yearly) - 1
	yearly_interest_percent = yearly_interest * 100

	return yearly_interest_percent

# inflation missing
def main():
	print("Portfolio Calculator")

	loop = get_int("Number of Index Funds: ")
	etfs = allocate_list(loop)
	etfs_alloc_percent = allocate_list(loop)

	for i in range(loop):
		etfs[i] = get_etf(i)

	total_return = calc_all_returns(etfs, etfs_alloc_percent)
	print(f"total interest: {total_return:.2f}%")

	yearly = get_int("Years: ")
	yearly_interest = calc_yearly_interest(total_return, yearly)
	print(f"Yearly interest: {yearly_interest:.2f}%")

if __name__ == "__main__":
	main()