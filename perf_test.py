import requests         # for sending HTTP requests
import time             # for timing

# service hosted ip
HOST_IP = "vm-148-1.ise.luddy.indiana.edu"

# get the total number of requests
n_requests = int(input("Number of requests: "))

# check if input is valid
if n_requests < 1:
    print("Please enter a valid number of requests.")
    exit(1)

# start the timer
start_time = time.time()

# send the specified number of requests
for i in range(0, n_requests):
    response = requests.get('http://' + HOST_IP + ':8080/engr-222/cpu')

# get the final time
end_time = time.time()

# calculate total run time
total_run_time = end_time - start_time

# calculate the avg run time
avg_run_time = total_run_time/n_requests

# print the results
print("Number of requests: ", n_requests)
print("Total run time: {}s ".format(total_run_time))
print("Average run time (per request): {}s".format(avg_run_time))

