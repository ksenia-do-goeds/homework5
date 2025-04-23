import random
import math
import statistics

random_numbers = [random.randint(1, 100) for _ in range(100)]

mean = statistics.mean(random_numbers)
median = statistics.median(random_numbers)
standard_deviation = statistics.stdev(random_numbers)
sum_of_numbers = sum(random_numbers)
sqrt_sum = round(math.sqrt(sum_of_numbers), 2)

print(f"Среднее: {mean:.2f}, Медиана: {median:.2f}, "
      f"Стандартное отклонение: {standard_deviation:.2f}, "
      f"Корень из суммы: {sqrt_sum:.2f}")
