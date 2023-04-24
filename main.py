import time
import gc
from heap import Heap
from graph_maker import combined_3_graph_maker
from create_list import create_list

def main():
    heap_2_insertion_times = {}
    heap_3_insertion_times = {}
    heap_4_insertion_times = {}
    heap_2_removal_times = {}
    heap_3_removal_times = {}
    heap_4_removal_times = {}

    test_lists = {i:create_list(i) for i in range(10000, 100001, 10000)}
    heap_2 = Heap(2)
    heap_3 = Heap(3)
    heap_4 = Heap(4)



    for key, value in test_lists.items():
        heap_2.clear()
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for i in value:
            heap_2.add(i)
        stop = time.process_time()
        insertion_time = stop - start
        if gc_old:
            gc.enable()
        heap_2_insertion_times[key] = insertion_time
    print("Heap 2 insertion times:", heap_2_insertion_times)

    for key, value in test_lists.items():
        heap_3.clear()
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for i in value:
            heap_3.add(i)
        stop = time.process_time()
        insertion_time = stop - start
        if gc_old:
            gc.enable()
        heap_3_insertion_times[key] = insertion_time
    print("Heap 3 insertion times:", heap_3_insertion_times)

    for key, value in test_lists.items():
        heap_4.clear()
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for i in value:
            heap_4.add(i)
        stop = time.process_time()
        insertion_time = stop - start
        if gc_old:
            gc.enable()
        heap_4_insertion_times[key] = insertion_time
    print("Heap 4 insertion times:", heap_4_insertion_times)

    for key, value in test_lists.items():
        heap_2.clear()
        for i in value:
            heap_2.add(i)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for i in range(len(value)):
            heap_2.remove()
        stop = time.process_time()
        removal_time = stop - start
        if gc_old:
            gc.enable()
        heap_2_removal_times[key] = removal_time
    print("Heap 2 removal times:", heap_2_removal_times)

    for key, value in test_lists.items():
        heap_3.clear()
        for i in value:
            heap_3.add(i)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for i in range(len(value)):
            heap_3.remove()
        stop = time.process_time()
        removal_time = stop - start
        if gc_old:
            gc.enable()
        heap_3_removal_times[key] = removal_time
    print("Heap 3 removal times:", heap_3_removal_times)

    for key, value in test_lists.items():
        heap_4.clear()
        for i in value:
            heap_4.add(i)
        gc_old = gc.isenabled()
        gc.disable()
        start = time.process_time()
        for i in range(len(value)):
            heap_4.remove()
        stop = time.process_time()
        removal_time = stop - start
        if gc_old:
            gc.enable()
        heap_4_removal_times[key] = removal_time
    print("Heap 4 removal times:", heap_4_removal_times)

    combined_3_graph_maker(
        heap_2_insertion_times,
        "Heap 2 insertion times",
        heap_3_insertion_times,
        "Heap 3 insertion times",
        heap_4_insertion_times,
        "Heap 4 insertion times",
        "Combined node adding times",
    )

    combined_3_graph_maker(
        heap_2_removal_times,
        "Heap 2 removal times",
        heap_3_removal_times,
        "Heap 3 removal times",
        heap_4_removal_times,
        "Heap 4 removal times",
        "Combined node removal times",
    )


if __name__=="__main__":
    main()