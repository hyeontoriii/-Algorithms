import datetime, sys
M, D = map(int, sys.stdin.readline().split())
print(datetime.date(2007,M,D).strftime('%a').upper())
