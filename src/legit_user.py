import requests


def request_network():
    url = "https://fad3-142-189-202-112.ngrok.io/user/all"
    request_data = requests.get(url)
    print("request_data")
    print(request_data)

request_network()
# request_network()