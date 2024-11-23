from calc import *
from init import *

def main():
	print("Portfolio Weight Calculator")

	loop = get_int("Number of Index Funds: ")
	etfs_return = alloc_float_arr(loop)
	etfs_weight = None
	for i in range(loop):
		etfs_return[i] = get_float(i)
	start_date_str = get_date("Enter the start date (YYYY-MM-DD): ")
	end_date_str = get_date("Enter the end date (YYYY-MM-DD): ")

	try:
		etfs_weight = calc_weight(etfs_return, loop)
		total_interest = calc_total_interest(etfs_return, etfs_weight)
		annual_rate = calc_annual_rate(start_date_str, end_date_str, total_interest)
	except ValueError as e:
		print(f"Error: {e}")

	print(f"total interest of weight over the period: {total_interest:.2f}%")
	for i in range(loop):
		print(f"ETF[{i + 1}] weight: {etfs_weight[i] * 100:.2f}%")
	print(f"Annual rate: {annual_rate:.2f}%")

if __name__ == "__main__":
	main()