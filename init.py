def alloc_float_arr(size):
	return [0.0] * size

def get_int(msg):
	while True:
		try:
			return int(input(msg))
		except ValueError:
			continue

def get_float(i):
	while True:
		try:
			return float(input(f"ETF[{i + 1}] total return: "))
		except ValueError:
			continue

def get_date(msg):
	while True:
		try:
			return input(msg)
		except ValueError:
			continue