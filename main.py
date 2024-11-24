import sys
from calc import *
from print_results import *

def calc_and_print_portfolio(etfs_return, start_date, end_date):

	if all(date == start_date[0] for date in start_date) and all(date == end_date[0] for date in end_date):
		precise_calc(etfs_return, start_date, end_date)
	else:
		unprecise_calc(etfs_return, start_date, end_date)
	
	etfs_return.clear()
	start_date.clear()
	end_date.clear()

def read_file(file_path):
	etfs_return = []
	start_date_list = []
	end_date_list = []

	with open(file_path, 'r') as file:
		print("[Portfolio Weight Calculator]")
		for line in file:
			if "[total return in %] | [start_date DD.MM.YY] | [end_date DD.MM.YY]" in line.strip():
				return

			if line.strip() == '':
				calc_and_print_portfolio(etfs_return, start_date_list, end_date_list)
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

	calc_and_print_portfolio(etfs_return, start_date_list, end_date_list)

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