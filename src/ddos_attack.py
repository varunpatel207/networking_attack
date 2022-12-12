import threading
import requests

def send_request():
    url = "http://localhost:8000/user/all"
    response = requests.get(url)
    print(response.status_code)

num_requests = 10000

threads = []
for i in range(num_requests):
    thread = threading.Thread(target=send_request)
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
