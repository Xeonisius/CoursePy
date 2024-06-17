import datetime

year, month, day = map(int, input().split())
days = int(input())

start_date = datetime.date(year, month, day)

delta = datetime.timedelta(days=days)

new_date = start_date + delta

print(new_date.year, new_date.month, new_date.day)