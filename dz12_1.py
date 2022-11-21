import concurrent.futures
import time

# Function to calculate factorial
def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

# Using ThreadPoolExecutor
def function1(arguments):
    launch1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = {
            executor.submit(factorial, argument): argument for argument in arguments
        }
        for future in concurrent.futures.as_completed(futures):
            argument = futures[future]
            print(f"TPE: {argument}! = {future.result()}")

    finish1 = time.time()

    time_process_thread = finish1 - launch1
    return time_process_thread

# Using ProcessPoolExecutor
def function2(arguments):
    launch2 = time.time()
    with concurrent.futures.ProcessPoolExecutor(5) as executor:
        futures = {
            executor.submit(factorial, argument): argument for argument in arguments
        }
        for future in concurrent.futures.as_completed(futures):
            argument = futures[future]
            print(f"PPE: {argument}! = {future.result()}")

    finish2 = time.time()

    time_process_process = finish2 - launch2
    return time_process_process

# Data for calculations
data_for_calculations = [9, 44, 15, 21, 67]

# Results
if __name__ == '__main__':
    thread_time = function1(data_for_calculations)
    process_time = function2(data_for_calculations)
    print(f"Execution time - ThreadPoolExecutor: {thread_time}")
    print(f"Execution time - ProcessPoolExecutor: {process_time}")
    if thread_time < process_time:
        print(f"CONCLUSION: The calculation speed using ThreadPoolExecutor is higher = {thread_time}")
    else:
        print(f"CONCLUSION: The calculation speed using ProcessPoolExecutor is higher {process_time}")