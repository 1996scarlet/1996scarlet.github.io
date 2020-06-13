import queue
import threading
import time

q = queue.Queue(1)

def producer():
    while True:
        try:
            q.put_nowait("data")  # 非阻塞
        except queue.Full:
            # 即使队列满了也会继续运行到这
            print("Queue Full, Sleep")
            # 方便演示 限制频率
            time.sleep(0.2)

def customer():
    while True:
        print(q.get())  # 阻塞 每秒解除一次
        time.sleep(1)   # 方便演示 限制频率

non_blk = threading.Thread(target=producer)
non_blk.start()

blocking = threading.Thread(target=customer)
blocking.start()