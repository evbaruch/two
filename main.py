# מבנה שפות תוכנה - תרגיל 2 

# name: Evyatar Baruch 
# I.D: 323916403

# name: Sapir Bashan
# I.D: 214103368

from functools import reduce
from itertools import accumulate
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from convertdate import hebrew
from time import time
import math

# 1. Linear function with lambda usage
print("1. Linear function with lambda usage")

linear_func = lambda x: x / 2 + 2

start_time = time()
result_map = list(map(linear_func, range(10001)))
end_time_map = time()

sum_result = reduce(lambda x, y: x + y, result_map)

start_time_imp = time()
result_imp = []
for i in range(10001):
    result_imp.append(linear_func(i))
sum_result_imp = sum(result_imp)
end_time_imp = time()

print(f"Runtime with map: {end_time_map - start_time}")
print(f"Imperative runtime: {end_time_imp - start_time_imp}")

# now with higher-order functions
# it's a higher-order function because it takes another function as an argument
result_single = list(accumulate(range(10001), lambda acc, x: acc + linear_func(x)))
sum_result_single = result_single[-1]

print(f"Sum with single higher-order function: {sum_result_single}")

# 2. Splitting list into even and odd numbers
print("\n2. Splitting list into even and odd numbers")

numbers = list(range(1, 1001))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

even_func = lambda acc, x: acc * x
odd_func = lambda acc, x: acc / 2 + 2 + x

even_result = reduce(even_func, even_numbers, 1)
odd_result = reduce(odd_func, odd_numbers, 0)

print(f"Product of even numbers: {even_result}")
print(f"Result for odd numbers: {odd_result}")

# 3. Date calculation function
print("\n3. Date calculation function")

def date_calculator(start_date, num_dates, skip_days):
    start = datetime.strptime(start_date, "%d/%m/%Y")
    date_generator = map(lambda i: start + timedelta(days=i * skip_days), range(num_dates))
    return list(map(lambda d: d.strftime("%d/%m/%Y"), date_generator))

result = date_calculator("01/01/2024", 5, 7)
print(result)

# 4. Power functions
print("\n4. Power functions")

def power_function(exponent):
    return lambda base: base ** exponent

def power_map(n):
    return map(lambda i: lambda x: x**i, range(n))

def taylor_e_x(x, n):
    factorial = lambda n: reduce(lambda a, b: a * b, range(1, n + 1), 1)
    return sum(map(lambda i: (x**i) / factorial(i), range(n)))

power_of_2 = power_function(2)
print(f"2^3 = {power_of_2(3)}")
print(f"2^5 = {power_of_2(5)}")

power_functions = list(power_map(5))
print(f"[x^0, x^1, x^2, x^3, x^4] for x=2: {[f(2) for f in power_functions]}")

print(f"Approximation of e^1: {taylor_e_x(1, 10)}")

# 5. Task manager (Closure)
print("\n5. Task manager (Closure)")

def task_manager():
    tasks = {}
    
    def add_task(task, status="incomplete"):
        tasks[task] = status
        return f"Task '{task}' added with status '{status}'"
    
    def get_tasks():
        return tasks
    
    def complete_task(task):
        if task in tasks:
            tasks[task] = "complete"
            return f"Task '{task}' marked as complete"
        return f"Task '{task}' not found"
    
    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }

tasks_manager = task_manager()

print(tasks_manager['add_task']("Write email"))
print(tasks_manager['add_task']("Shopping", "in progress"))
print(tasks_manager['add_task']("Homework"))

print("\nInitial tasks:")
print(tasks_manager['get_tasks']())

print(tasks_manager['complete_task']("Write email"))

print("\nTasks after completing 'Write email':")
print(tasks_manager['get_tasks']())
