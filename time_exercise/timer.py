from datetime import datetime
from datetime import timedelta
from datetime import date

t = timedelta(days=10, hours=3)
today = datetime.today().date()

print(today)

eta = timedelta(hours=1)
timer = today + eta

print("The timer is up at ", timer)

anniversary = date(2019, 11, 11)

print("Our anniversary is on ", anniversary)

daysleft = (anniversary - today).days

print("daysleft", daysleft)

