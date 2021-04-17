import threading
import time
import random


class ReadWriteMonitor(object):
    def __init__(self):
        self.readlock = threading.Condition()
        self.writelock = threading.Condition()
        self.readers = 0
        self.data = 0


class Reader(threading.Thread):
    def __init__(self, mon):
        super(Reader, self).__init__()
        self.mon = mon

    def run(self) -> None:
        time.sleep(random.randrange(2, 6) / 100)
        # Magic!
        with self.mon.writelock:
            pass
        with self.mon.readlock:
            self.mon.readers += 1
            readers = self.mon.readers
        print(self.mon.data, readers)
        time.sleep(0.1)
        with self.mon.readlock:
            self.mon.readers -= 1
            self.mon.readlock.notify()


class Writer(threading.Thread):
    def __init__(self, mon):
        super(Writer, self).__init__()
        self.mon = mon

    def run(self) -> None:
        time.sleep(random.randrange(1, 6) / 100)
        done = False
        with self.mon.writelock:
            while not done:
                with self.mon.readlock:
                    while self.mon.readers != 0:
                        self.mon.readlock.wait()
                    else:
                        temp = self.mon.data + 1
                        time.sleep(random.randrange(5) / 1000)
                        self.mon.data = temp
                        print("Data Set to", temp, self.mon.readers)
                        done = True


rwmon = ReadWriteMonitor()
arr = ([0] * 80) + ([1] * 20)
random.shuffle(arr)
print(arr)
for n in arr:
    if n == 1:
        Writer(rwmon).start()
    else:
        Reader(rwmon).start()
