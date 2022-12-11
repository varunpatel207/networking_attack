import requests
from multiprocessing.dummy import Pool

import requests

pool = Pool(20) # Creates a pool with ten threads; more threads = more concurrency.
                # "pool" is a module attribute; you can be sure there will only
                # be one of them in your application
                # as modules are cached after initialization.

# Constants
URL = 'https://fad3-142-189-202-112.ngrok.io/user/all'

def send_fake_data():
    request_data = requests.get("https://192.168.2.23")
    print("request_data.text")
    print(request_data.text)

    # futures = []
    # for x in range(1000):
    #     futures.append(pool.apply_async(requests.get, [""]))
    # for future in futures:
    #     print(future.get())


send_fake_data()


