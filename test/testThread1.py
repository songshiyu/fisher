"""
    Created by songshiyu on 2020/10/12 上午9:28
    python中的多线程测试
"""
import threading


def worker():
    t = threading.current_thread()
    print(t.getName())


t = threading.current_thread()
print(t.getName())

worker1 = threading.Thread(target=worker, name="test1")
worker1.start()
