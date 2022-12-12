import time
from multiprocessing import Process
import socket

# Function to make a socket request to the server
def make_request():
  # Create a socket
  client_socket = socket.socket()
  print("client_socket")
  print(client_socket)

  # Connect to the server using the server's IP address and port
  client_socket.connect(('192.168.2.59', 8000))

  try:
      # Send a request to the server
      client_socket.send(b'Hello from the client!')
  except Exception as e:
      print(e)

  # Receive a response from the server
  # data = client_socket.recv(1024)

  # Print the received data
  # print('Received data from server: {}'.format(data))

  # Close the socket
  client_socket.close()

if __name__ == '__main__':
  start_time = time.time()

  # Create a list of processes
  processes = []

  # Start 200 processes that each make a request to the server
  for i in range(10000):
    p = Process(target=make_request)
    p.start()
    processes.append(p)

  # Wait for all processes to complete
  for p in processes:
    p.join()

  end_time = time.time()

  # Calculate the total time taken to complete all requests
  total_time = end_time - start_time
  print('Total time: {} seconds'.format(total_time))
