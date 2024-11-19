import threading

def print_numbers():
    for i in range(10):
        print(i)

t = threading.Thread(target=print_numbers)
t.start()
t.join()
