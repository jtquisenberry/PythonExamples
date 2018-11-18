**Definition of Semaphore**

Semaphore is a process synchronization tool. Semaphore is typically an integer variable S that is initialized to the number of resources present in the system and the value of semaphore can be modified only by two functions wait() and signal() apart from initialization.

The wait() and signal() operation modify the value of the semaphore indivisibly. It means that when a process is modifying the value of the semaphore, no other process can simultaneously modify the value of the semaphore. Semaphore are distinguished by the operating system in two categories Counting semaphores and Binary semaphore.

In Counting Semaphore, the semaphore S value is initialized to the number of resources present in the system. Whenever a process wants to access the resource it performs wait() operation on the semaphore and decrements the value of semaphore by one. When it releases the resource, it performs signal() operation on the semaphore and increments the value of semaphore by one. When the semaphore count goes to 0, it means all resources are occupied by the processes. If a process need to use a resource when semaphore count is 0, it executes wait() and get blocked until the value of semaphore becomes greater than 0.

In Binary semaphore, the value of semaphore ranges between 0 and 1. It is similar to mutex lock, but mutex is a locking mechanism whereas, the semaphore is a signalling mechanism. In binary semaphore, if a process wants to access the resource it performs wait() operation on the semaphore and decrements the value of semaphore from 1 to 0. When it releases the resource, it performs a signal() operation on the semaphore and increments its value to 1. If the value of semaphore is 0 and a process want to access the resource it performs wait() operation and block itself till the current process utilizing the resources releases the resource.

**Definition of Mutex**

Mutual Exclusion Object is shortly termed as Mutex. From the term mutual exclusion, we can understand that only one process at a time can access the given resource. The mutex object allows the multiple program threads to use the same resource but one at a time not simultaneously.

When a program starts it request the system to creates a mutex object for a given resource. The system creates the mutex object with a unique name or ID. Whenever the program thread wants to use the resource it occupies lock on mutex object, utilizes the resource and after use, it releases the lock on mutex object. Then the next process is allowed to acquire the lock on mutex object.

Meanwhile, a process has acquired the lock on mutex object no other thread/process can access that resource. If the mutex object is already locked, the process desiring to acquire the lock on mutex object has to wait and is queued up by the system till the mutex object is unlocked.

**Key Differences Between Semaphore and Mutex**

1. Semaphore is a signalling mechanism as wait() and signal() operation performed on semaphore variable indicates whether a process is acquiring the resource or releasing the resource. On the other hands, the mutex is a locking mechanism, as to acquire a resource, a process needs to lock the mutex object and while releasing a resource process has to unlock mutex object.
2. Semaphore is typically an integer variable whereas, mutex is an object.
3. Semaphore allows multiple program threads to access the finite instance of resources. On the other hands, Mutex allows multiple program threads to access a single shared resource but one at a time.
4. Semaphore variable value can be modified by any process that acquires or releases resource by performing wait() and signal() operation. On the other hands, lock acquired on the mutex object can be released only by the process that has acquired the lock on mutex object.
5. Semaphore are of two types counting semaphore and binary semaphore which is quite similar to the mutex.
6. Semaphore variable value is modified by wait() and signal() operation apart from initialization. However, the mute object is locked or unlocked by the process acquiring or releasing the resource.
7. If all the resources are acquired by the process, and no resource is free then the process desiring to acquire resource performs wait() operation on semaphore variable and blocks itself till the count of semaphore become greater than 0. But if a mutex object is already locked then the process desiring to acquire resource waits and get queued by the system till the resource is released and mutex object gets unlocked.

**Conclusion:**

Semaphore is a better option in case there are multiple instances of resources available. In the case of single shared resource mutex is a better choice.


**Spinlocks**

https://stackoverflow.com/questions/5869825/when-should-one-use-a-spinlock-instead-of-mutex

In theory, when a thread tries to lock a mutex and it does not succeed, because the mutex is already locked, it will go to sleep, immediately allowing another thread to run. It will continue to sleep until being woken up, which will be the case once the mutex is being unlocked by whatever thread was holding the lock before. When a thread tries to lock a spinlock and it does not succeed, it will continuously re-try locking it, until it finally succeeds; thus it will not allow another thread to take its place (however, the operating system will forcefully switch to another thread, once the CPU runtime quantum of the current thread has been exceeded, of course).
