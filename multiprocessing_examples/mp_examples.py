from multiprocessing import Pool, TimeoutError, Manager
import multiprocessing
import time
import os


def f(x):
    print('PID: {0}, x: {1}'.format(os.getpid(), x))
    return x * x


def f2(xs):
    for x in xs:
        print('PID: {0}, x: {1}'.format(os.getpid(), x))


def work_with_manager(work):
    number = work[0]
    my_list_a = work[1]
    my_list_a[number] = number


if __name__ == '__main__':

    print("CPU Count", multiprocessing.cpu_count())

    # start 4 worker processes
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        # list of results
        # map applies function f to each element in the list of range(10)
        # print(pool.map(f, range(10)))

        # print same numbers in arbitrary order
        # iterator of results
        # for i in pool.imap_unordered(f, range(10)):
        #    print(i)

        # evaluate "f(20)" asynchronously
        # res = pool.apply_async(f, (20,))  # runs in *only* one process
        # print(res.get(timeout=1))  # prints "400"

        # evaluate "f()" asynchronously
        # res = pool.apply_async(f2, (range(0,1000),))  # runs in *only* one process
        # print(res.get(timeout=1000))

        # evaluate "os.getpid()" asynchronously
        # res = pool.apply_async(os.getpid, ())  # runs in *only* one process
        # print(res.get(timeout=1))  # prints the PID of that process

        # launching multiple evaluations asynchronously *may* use more processes
        # multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        # print([res.get(timeout=1) for res in multiple_results])

        '''
        processes = list()
        a = pool.apply_async(func=f, args=(2,))
        b = pool.apply_async(func=f, args=(3,))
        c = pool.apply_async(func=f, args=(4,))
        d = pool.apply_async(func=f, args=(5,))
        processes.append(a)
        processes.append(b)
        processes.append(c)
        processes.append(d)
        for res in processes:
            res.get(timeout=100000)
        '''

        # Use a manager with the pool.
        with Manager() as manager:
            #list attached to the manager. The following would not work
            #my_list = list(range(11, 20))
            my_list = manager.list(range(11,20))
            processes = list()
            a = pool.apply_async(func=work_with_manager, args=([1,my_list],))
            b = pool.apply_async(func=work_with_manager, args=([2,my_list],))
            c = pool.apply_async(func=work_with_manager, args=([3,my_list],))
            d = pool.apply_async(func=work_with_manager, args=([4,my_list],))
            processes.append(a)
            processes.append(b)
            processes.append(c)
            processes.append(d)
            for res in processes:
                res.get(timeout=100000)
            print(my_list)


        '''
        # make a single worker sleep for 10 secs
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")
        '''

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")