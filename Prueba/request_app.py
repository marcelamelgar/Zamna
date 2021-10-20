import threading, time

def f(n = 1):
    print("f started")
    time.sleep(3)
    print("f finished", n)

threading.Thread(target=f, args=(8)).start()
print("ALV")