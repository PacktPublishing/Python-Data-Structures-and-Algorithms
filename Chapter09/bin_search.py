

def binary_search(ordered_list, term):

    size_of_list = len(ordered_list) - 1

    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element)/2

        if ordered_list[mid_point] == term:
            return mid_point

        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1


store = []
for i in range(1000000):
    store.append(i)

import time
start_time = time.time()
binary_search(store, 999333333)
print("--- %s seconds ---" % (time.time() - start_time))

import time
start_time = time.time()
binary_search(store, 933)
print("--- %s Found: seconds ---" % (time.time() - start_time))


"""
import time
start_time = time.time()
print(search(store, 999))
print("--- %s seconds ---" % (time.time() - start_time))


"""

store = []
for i in range(1000000):
    store.append(i)

import time
start_time = time.time()
results = "Found at {}".format(binary_search(store, 999333333))
print("--- %s seconds ---: %s" % ((time.time() - start_time), results))

store = []
for i in range(1000000):
    store.append(i)



start_time = time.time()
results = "Found at {}".format(binary_search(store, 993))
print("--- %s seconds --- %s" % ((time.time() - start_time),results))

store = []
for i in range(1000000):
    store.append(i)


start_time = time.time()
results = "Found at {}".format(binary_search(store, -4999999999995))
print("--- %s seconds --- %s" % ((time.time() - start_time),results))
