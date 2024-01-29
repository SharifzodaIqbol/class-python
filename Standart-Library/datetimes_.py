from datetime import date

now = date.today()

print(now)# 2024-01-29

birthday = date(2006, 2, 23)

age = now - birthday

print(age.days)# 6549
