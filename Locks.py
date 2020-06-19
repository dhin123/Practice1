import threading


class Lock:
    def __init__(self):
        self.flag = 0

    def lock(self):
        while self.flag == 1:
            pass
        self.flag = 1

    def unlock(self):
        self.flag = 0





def increment():

    global x
    #l.lock()
    x += 1
    #l.unlock()


def thread_task():
    increment()


def main_task():



    # creating threads

    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()


if __name__ == "__main__":
    l = Lock()
    global x
    x = 0
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))