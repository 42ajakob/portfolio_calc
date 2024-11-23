from datetime import datetime
from init import alloc_float_arr

def calc_weight(etfs_return, loop):
	etfs_weight = alloc_float_arr(loop)
	etf_sum = sum(etfs_return)

	for i in range(len(etfs_return)):
		etfs_weight[i] = etfs_return[i] / etf_sum

	return etfs_weight

def calc_total_interest(etfs_return, etfs_weight):
	total_interest = 0.0

	for i in range(len(etfs_return)):
		total_interest += etfs_return[i] * etfs_weight[i]

	return total_interest / 100

def calc_annual_rate(start_date, end_date, total_interest):
	years = (end_date - start_date).days / 365.25
	annual_rate = (1 + total_interest) ** (1 / years) - 1

	return annual_rate * 100