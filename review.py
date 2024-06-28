# Review 1
def add_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

# Review 2
def format_greeting(name, age):
    # return "Hello, my name is {name} and I am {age} years old.
    # here we should use %s or %d to match params, for float we can use %.1f
    return "Hello, my name is %s and I am %d years old." % (name, age)


# Review 3
class Counter:
    # class param
    count = 0

    def __init__(self):
        # self pointed to the instance of this class
        # self.count += 1
        Counter.count += 1

    def get_count(self):
        return self.count

# Review 4
import threading

threadLock = threading.Lock()

class SafeCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


def worker(counter):
    for _ in range(1000):
        # use lock to assure only one thread can count at a time
        threadLock.acquire()
        counter.increment()
        threadLock.release()


counter = SafeCounter()
threads = []
for _ in range(10):
    # each thread will count 1000 times for counter, then final counter should be 10000
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)


for t in threads:
    t.join()



# Review 5
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            # counts[item] =+ 1
            # count[item] += 1 is as the as count[item]=count[item]+1
            counts[item] += 1
        else:
            counts[item] = 1
    return counts
