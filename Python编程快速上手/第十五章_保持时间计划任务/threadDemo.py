import threading, time


print('start of program')

def takeANap():
    time.sleep(5)
    print('wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('end of program')