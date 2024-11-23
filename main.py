from calc import *
from init import *
from print_results import *

def main():
	print("Portfolio Weight Calculator")

	loop = get_int("Number of Index Funds [1-100]: ")
	etfs_return = alloc_float_arr(loop)
	for i in range(loop):
		etfs_return[i] = get_float(i)
	start_date = get_date("Enter the start date [DD.MM.YY]: ")
	end_date = get_date("Enter the end date [DD.MM.YY]: ")

	etfs_weight = calc_weight(etfs_return, loop)
	total_interest = calc_total_interest(etfs_return, etfs_weight)
	annual_rate = calc_annual_rate(start_date, end_date, total_interest)

	print_results(total_interest, etfs_weight, annual_rate)

if __name__ == "__main__":
	main()