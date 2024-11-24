from datetime import datetime
from print_results import *

def calc_weight(etfs_return, loop):
	etfs_weight = []
	etf_sum = sum(etfs_return)

	for i in range(len(etfs_return)):
		etfs_weight.append(etfs_return[i] / etf_sum)

	return etfs_weight

def calc_total_interest(etfs_return, etfs_weight):
	total_interest = 0.0

	for i in range(len(etfs_return)):
		total_interest += etfs_return[i] * etfs_weight[i]

	return total_interest

def calc_ann_rate(start_date, end_date, total_interest):
	years = (end_date - start_date).days / 365.25
	ann_rate = (1 + total_interest) ** (1 / years) - 1

	return ann_rate

def precise_calc(etfs_return, start_date, end_date):
	loop = len(etfs_return)
	ann_rate = []
	ann_rate_weight = []

	for i in range(loop):
		ann_rate.append(calc_ann_rate(start_date[0], end_date[0], etfs_return[i]))

	weight = calc_weight(etfs_return, loop)
	total_interest = calc_total_interest(etfs_return, weight)
	ann_rate_interest = calc_ann_rate(start_date[0], end_date[0], total_interest)
	for i in range(loop):
		ann_rate_weight.append(ann_rate[i] * weight[i])

	print_results(weight, ann_rate_interest, ann_rate, ann_rate_weight)

def unprecise_calc(etfs_return, start_date, end_date):
	loop = len(etfs_return)
	ann_rate = []
	ann_rate_weight = []

	for i in range(loop):
		ann_rate.append(calc_ann_rate(start_date[i], end_date[i], etfs_return[i]))

	weight = calc_weight(ann_rate, loop)
	total_interest = calc_total_interest(ann_rate, weight)
	for i in range(loop):
		ann_rate_weight.append(ann_rate[i] * weight[i])

	print_warning()
	print_results(weight, total_interest, ann_rate, ann_rate_weight)