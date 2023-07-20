# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month_cnt = 0

# How much will Dave pay if he pays an extra $1000/month for 4 years starting after the first five years have already been paid?
extra_payment_start_month = 5 * 12
extra_payment_end_month = (5 + 4) * 12
extra_payment = 1000

while principal > 0:
  principal = principal * (1+rate/12) - payment
  if principal < 0:
    break
  total_paid = total_paid + payment
  if month_cnt >= extra_payment_start_month and month_cnt < extra_payment_end_month:
    total_paid += extra_payment
    principal -= extra_payment
  month_cnt += 1
  #print(month_cnt, round(total_paid, 2), round(principal, 2))

print('Total paid', total_paid)
print('Month', month_cnt)



# Total paid 929965.6199999959

