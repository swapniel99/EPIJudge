import threading


class OddEvenMonitor(threading.Condition):
    ODD_TURN = True
    EVEN_TURN = False

    def __init__(self):
        super(OddEvenMonitor, self).__init__()
        self.turn = self.ODD_TURN  # First Turn

    def toggle_turn(self):
        with self:
            self.turn ^= True
            self.notify()

    def wait_turn(self, turn):
        with self:
            while self.turn != turn:
                self.wait()


class AltThread(threading.Thread):
    def __init__(self, monitor, first, last, turn):
        super(AltThread, self).__init__()
        self.monitor = monitor
        self.first = first
        self.last = last
        self.turn = turn

    def run(self) -> None:
        for i in range(self.first, self.last, 2):
            self.monitor.wait_turn(self.turn)
            print(i)
            self.monitor.toggle_turn()


mon = OddEvenMonitor()
AltThread(mon, 1, 100, OddEvenMonitor.ODD_TURN).start()
AltThread(mon, 2, 102, OddEvenMonitor.EVEN_TURN).start()
