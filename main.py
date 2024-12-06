import sys
from calc import *
from print_results import *

def calc_with_weight(etfs_return, start_date_list, end_date_list, weight, money):
	if etfs_return == []:
		return

	if all(date == start_date_list[0] for date in start_date_list) and all(date == end_date_list[0] for date in end_date_list):
		precise_calc_with_weight(etfs_return, start_date_list, end_date_list, weight, money)
	else:
		unprecise_calc_with_weight(etfs_return, start_date_list, end_date_list, weight, money)
	
	etfs_return.clear()
	start_date_list.clear()
	end_date_list.clear()
	weight.clear()
	print()

def calc_and_print_portfolio(etfs_return, start_date, end_date, money):
	if etfs_return == []:
		return

	if all(date == start_date[0] for date in start_date) and all(date == end_date[0] for date in end_date):
		precise_calc(etfs_return, start_date, end_date, money)
	else:
		unprecise_calc(etfs_return, start_date, end_date, money)
	
	etfs_return.clear()
	start_date.clear()
	end_date.clear()
	print()

def read_file(file_path, money):
	etfs_return = []
	start_date_list = []
	end_date_list = []
	weight = []

	with open(file_path, 'r') as file:
		print("[Portfolio Weight Calculator]\n")
		for line in file:
			if "[total return in %] | [start_date DD.MM.YY] | [end_date DD.MM.YY] | [OPTIONAL weight in %]" in line.strip():
				return

			if line.strip() == '' and weight == []:
				calc_and_print_portfolio(etfs_return, start_date_list, end_date_list, money)
				continue
			elif line.strip() == '' and weight != []:
				calc_with_weight(etfs_return, start_date_list, end_date_list, weight, money)
				continue

			parts = line.strip().split('|')

			if any(char.isalpha() for char in parts[0].strip()):
				print(line.strip())
				continue

			value = float(parts[0].strip()) / 100
			start_date = datetime.strptime(parts[1].strip(), '%d/%m/%y').date()
			end_date = datetime.strptime(parts[2].strip(), '%d/%m/%y').date()
			if len(parts) == 4:
				fixed_weight = float(parts[3].strip()) / 100
				weight.append(fixed_weight)

			etfs_return.append(value)
			start_date_list.append(start_date)
			end_date_list.append(end_date)
			

	if weight != []:
		calc_with_weight(etfs_return, start_date_list, end_date_list, weight, money)
	else:
		calc_and_print_portfolio(etfs_return, start_date_list, end_date_list, money)

def main():
	if len(sys.argv) != 3:
		print("Usage Example: python main.py portfolio_example.txt 500")
		sys.exit(1)

	file_path = sys.argv[1]
	money = float(sys.argv[2])
	try:	
		read_file(file_path, money)
	except:
		print("Error! File not found or wrong input")
		print("Try: python main.py portfolio_example.txt")

if __name__ == "__main__":
	main()