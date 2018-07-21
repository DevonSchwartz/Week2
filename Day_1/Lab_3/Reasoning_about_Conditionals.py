def is_leap3 (year):
  if year % 100 == 0:                  return False
  if year % 400 == 0 or year % 4 == 0: return True
  return False

def is_leap2 (year):
  return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def is_leap1 (year):
  if year % 400 == 0: return True
  if year % 100 == 0: return False
  if year %   4 == 0: return True
  return False

Year = 2100

print(is_leap3(Year))
print(is_leap2(Year))
print(is_leap1(Year))
