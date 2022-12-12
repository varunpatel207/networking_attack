import time
from multiprocessing import Process
import requests


def send_request():
  response = requests.get('http://192.168.2.59:8000/user/all')
  if response.status_code == 200:
    print('Success!')
  else:
    print('Request failed')


if __name__ == '__main__':
  start_time = time.time()

  # Create a list of processes
  processes = []

  # Start 200 processes that each make a request to the server
  for i in range(200):
    p = Process(target=send_request)
    p.start()
    processes.append(p)

  # Wait for all processes to complete
  for p in processes:
    p.join()

  end_time = time.time()

  # Calculate the total time taken to complete all requests
  total_time = end_time - start_time
  print('Total time: {} seconds'.format(total_time))
