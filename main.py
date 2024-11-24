import sys
import sys
from calc import *
from print_results import *

def calc_and_print(etfs_return, start_date, end_date):
	loop = len(etfs_return)
	a_annual_rate = []

	for i in range(loop):
		a_annual_rate.append(calc_annual_rate(start_date[i], end_date[i], etfs_return[i]))

	a_weight = calc_weight(a_annual_rate, loop)
	a_total_interest = calc_total_interest(a_annual_rate, a_weight)

	print_results(a_weight, a_total_interest)

	weight = calc_weight(etfs_return, loop)
	total_interest = calc_total_interest(etfs_return, weight)
	annual_rate = calc_annual_rate(start_date[0], end_date[0], total_interest)

	print_res(annual_rate, weight)

	etfs_return.clear()
	start_date.clear()
	end_date.clear()
	a_annual_rate.clear()

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