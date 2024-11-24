import sys
import sys
from calc import *
from print_results import *

def calc_and_print(etfs_return, start_date, end_date):
	loop = len(etfs_return)
	annual_rate = []

	for i in range(loop):
		annual_rate.append(calc_annual_rate(start_date[i], end_date[i], etfs_return[i]))

	etfs_weight = calc_weight(annual_rate, loop)
	total_interest = calc_total_interest(annual_rate, etfs_weight)
	calc_weight_precise = calc_weight(etfs_return, loop)

	print_results(total_interest, calc_weight_precise, annual_rate)

	
	calc_total_interest_precise = calc_total_interest(etfs_return, calc_weight_precise)
	calc_annual_rate_based_on_etfs_return = calc_annual_rate(start_date[0], end_date[0], calc_total_interest_precise)

	print_res(calc_annual_rate_based_on_etfs_return)

	etfs_return.clear()
	start_date.clear()
	end_date.clear()
	annual_rate.clear()

def read_file(file_path):
	etfs_return = []
	start_date_list = []
	end_date_list = []

	with open(file_path, 'r') as file:
		print("[Portfolio Weight Calculator]")
		for line in file:
			if line.strip() == '':
				calc_and_print(etfs_return, start_date_list, end_date_list)
				print()
				continue

			parts = line.strip().split('|')

			if any(char.isalpha() for char in parts[0].strip()):
				print(line.strip())
				continue

			value = float(parts[0].strip()) / 100
			start_date = datetime.strptime(parts[1].strip(), '%d.%m.%y').date()
			end_date = datetime.strptime(parts[2].strip(), '%d.%m.%y').date()

			etfs_return.append(value)
			start_date_list.append(start_date)
			end_date_list.append(end_date)

	calc_and_print(etfs_return, start_date_list, end_date_list)

def main():

	if len(sys.argv) != 2:
		print("Usage: python main.py portfolio_example.txt")
		sys.exit(1)

	file_path = sys.argv[1]
	try:
		
		read_file(file_path)
	except:
		print("Error! File not found or wrong input")
		print("Try: python main.py portfolio_example.txt")

if __name__ == "__main__":
	main()