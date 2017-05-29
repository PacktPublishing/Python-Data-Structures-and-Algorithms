
def nearest_mid(input_list, lower_bound_index, upper_bound_index, search_value):
    return lower_bound_index + (( upper_bound_index - lower_bound_index)/ (input_list[upper_bound_index] - input_list[lower_bound_index])) * (search_value - input_list[lower_bound_index])

def interpolation_search(ordered_list, term):

    size_of_list = len(ordered_list) - 1

    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        mid_point = nearest_mid(ordered_list, index_of_first_element, index_of_last_element, term)

        if mid_point > index_of_last_element or mid_point < index_of_first_element:
            return None

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
results = "Found at {}".format(interpolation_search(store, 999333333))
print("--- %s seconds ---: %s" % ((time.time() - start_time), results))

store = []
for i in range(1000000):
    store.append(i)



start_time = time.time()
results = "Found at {}".format(interpolation_search(store, 993))
print("--- %s seconds --- %s" % ((time.time() - start_time),results))

store = []
for i in range(1000000):
    store.append(i)


start_time = time.time()
results = "Found at {}".format(interpolation_search(store, -4999999999995))
print("--- %s seconds --- %s" % ((time.time() - start_time),results))
