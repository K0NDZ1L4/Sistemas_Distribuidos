import logging
import threading


def thread_function(thread_index, thread_name):
    logging.info("Thread %s: starting", thread_index)
    thread_name()
    logging.info("Thread %s: finishing", thread_index)


def main(thread_name):
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = list()
    for index in range(4):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index, thread_name))
        threads.append(x)
        x.start()

'''
for index, thread in enumerate(threads):
    logging.info("Main    : before joining thread %d.", index)
    thread.join()
    logging.info("Main    : thread %d done", index)
'''
