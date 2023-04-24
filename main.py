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



if __name__=="__main__":
    main()