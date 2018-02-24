from multiprocessing import Process, Queue
import multiprocessing

if __name__ == '__main__':
    q = Queue()
    m = multiprocessing.Manager()
    print(id(m))
    #q.put('aaa')
    print(q.get())
    print('done')
