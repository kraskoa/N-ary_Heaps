class Heap:
    def __init__(self, n):
        self.heap = []
        self.n = n

    def add(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def remove(self):
        if not self.heap:
            return
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        value = self.heap.pop()
        self.heapify_down(0)

    def heapify_up(self, index):
        parent = (index - 1) // self.n
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)

    def heapify_down(self, index):
        largest = index
        for i in range(1, self.n + 1):
            child = self.n * index + i
            if child < len(self.heap) and self.heap[child] > self.heap[largest]:
                largest = child
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def print_heap(self):
        if not self.heap:
            print("Empty heap")
            return
        queue = [(0, None)]  # Start with the root node
        depth = 0
        while queue:
            level_nodes = []  # Store nodes at the current level
            for _ in range(len(queue)):
                index, parent_index = queue.pop(0)
                if parent_index is not None:
                    level_nodes.append(
                        f"{self.heap[index]} {'─' * 2}> {self.heap[parent_index]}"
                    )
                else:
                    level_nodes.append(str(self.heap[index]))
                for i in range(1, self.n + 1):
                    child_index = self.n * index + i
                    if child_index < len(self.heap):
                        queue.append((child_index, index))
            print(
                "    " * depth + " ".join(level_nodes)
            )  # Print nodes at the current level
            depth += 1

    def clear(self):
        self.heap = []


def main():
    heap = Heap(2)
    heap.add(1)
    heap.add(2)
    heap.add(3)
    heap.add(4)
    heap.add(5)
    heap.add(6)
    heap.add(7)
    heap.print_heap()
    heap.remove()
    heap.print_heap()
    heap.remove()
    heap.print_heap()
    heap.remove()
    heap.print_heap()


if __name__=="__main__":
    main()
