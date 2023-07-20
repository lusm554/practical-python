# bounce.py
#
# Exercise 1.5

height = 100 # meters
bounce = height * .6 # 3/5 is 60 percent
bounce_cnt = 10

for i in range(bounce_cnt):
  print(i+1, round(bounce, 4))
  height = bounce
  bounce = height * .6

