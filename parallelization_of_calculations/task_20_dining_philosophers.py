import threading
import time


class Waiter(object):

    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def service(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1


class Fork(object):

    def __init__(self, fork_num):
        self.fork_num = fork_num
        self.fork_user = -1
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, fork_user):
        with self.lock:
            while self.taken:
                self.lock.wait()
            self.fork_user = fork_user
            self.taken = True
            print(f"Philosopher no. {fork_user}, took fork no. {self.fork_num}\n")
            self.lock.notifyAll()

    def drop(self, fork_user):
        with self.lock:
            while not self.taken:
                self.lock.wait()
            self.fork_user = -1
            self.taken = False
            print(f"Philosopher no. {fork_user}, dropped fork no. {self.fork_num}\n")
            self.lock.notifyAll()


class Philosopher (threading.Thread):

    def __init__(self, fork_num, left_fork, right_fork, avoid):
        threading.Thread.__init__(self)
        self.fork_num = fork_num
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.avoid = avoid

    def run(self):
        for i in range(20):
            self.avoid.down()
            time.sleep(0.5)
            self.left_fork.take(self.fork_num)
            time.sleep(0.5)
            self.right_fork.take(self.fork_num)
            time.sleep(0.5)
            self.right_fork.drop(self.fork_num)
            self.left_fork.drop(self.fork_num)
            self.avoid.service()
        print(f"Philosopher stops eating and stops thinking {self.fork_num}\n")


def main():
    fork_philo_amount = 5

    avoid = Waiter(fork_philo_amount-1)

    fork_list = [Fork(i) for i in range(fork_philo_amount)]


    philo_list = [Philosopher(i, fork_list[i], fork_list[(i+1)%fork_philo_amount], avoid) for i in range(fork_philo_amount)]

    for i in range(fork_philo_amount):
        philo_list[i].start()


if __name__ == "__main__":
    main()