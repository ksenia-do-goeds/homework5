import random
import datetime
import array

def generate_random_date(start_date, end_date):
    return start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))

end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=5*365)
dates = array.array('d', [generate_random_date(start_date, end_date).toordinal() for _ in range(10)])

for i in range(len(dates) - 1):
    date1 = datetime.date.fromordinal(int(dates[i]))
    date2 = datetime.date.fromordinal(int(dates[i + 1]))
    difference = abs((date2 - date1).days)
    print(f"Разница между {date1} и {date2}: {difference} дней")
