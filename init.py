import sys
from datetime import datetime

def alloc_float_arr(size):
	return [0.0] * size

def get_int(msg):
	while True:
		try:
			user_in = int(input(msg))
			if user_in < 1 or user_in > 100:
				continue
			return user_in
		except ValueError:
			continue

def get_float(i):
	while True:
		try:
			user_in = float(input(f"ETF[{i + 1}] total return: "))
			if -sys.float_info.max <= user_in <= sys.float_info.max:
				return user_in
		except ValueError:
			continue

def get_date(msg):
	while True:
		try:
			return datetime.strptime(input(msg), '%d.%m.%y')
		except ValueError:
			continue