# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_cnt = 0

while principal > 0:
	principal = principal * (1+rate/12) - payment
	total_paid = total_paid + payment
	if month_cnt < 12:
		total_paid += 1000
		principal -= 1000
	month_cnt += 1

print('Total paid', total_paid)
