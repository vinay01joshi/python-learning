from datetime import datetime
from time import time

dt1 = datetime(2019, 1, 1)
dt2 = datetime.now()
dt = datetime.strptime("2019-08-22", "%Y-%m-%d")
print(dt)

dt = datetime.fromtimestamp(time())
print(dt)

print(f"{dt.year}/{dt.month}/{dt.day}")
print(dt.strftime("%Y-%m-%d"))

print(dt2 > dt1)
