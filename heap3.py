class Heap3:
    def __init__(self):
        self.heap = []

    def add(self, value):
        self.heap.append(value)
        index = len(heap) - 1
        parent_index = (index - 1) // 3
        while (index > 0) and (heap[index] > heap[parent_index]):
            pass

    def remove(self, value):
        pass

    def print_heap(self):
        pass
