# Description: Implementation of a MinHeap using a pre-written dynamic array class

# Import pre-written DynamicArray and LinkedList classes
from a5_include import *

class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object to the minheap

        Parameters:
            node(object): The value being added
        """
        index = self.heap.length()
        self.heap.append(node)
        while index > 0:
            parent_index = int((index - 1) / 2)
            parent_val = self.heap.get_at_index(parent_index)
            if node < parent_val:
                self.heap.swap(index, parent_index)
                index = parent_index
            else:
                break

    def get_min(self) -> object:
        """
        Returns the minimum value in min-heap...top-value

        Returns:
            self.heap.get_at_index(0) (object): The top and minimum value of min heap
        """

        if self.is_empty():
            raise MinHeapException
        else:
            return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Removes the minimum/top element from the tree and replaces it correspondingly

        Returns:
            self.heap.pop() (object): The top value if the heap is length one
            val(object): The value of the top element in heap(before removal)
        """
        if self.is_empty():
            raise MinHeapException
        elif self.heap.length() == 1:
            return self.heap.pop()
        else:
            self.heap.swap(0, self.heap.length() - 1)
            val = self.heap.pop()
            index = 0
            while index < self.heap.length():
                leftC = 2 * index + 1
                rightC = 2 * index + 2
                if leftC > self.heap.length() - 1 and rightC > self.heap.length() - 1:  #both children are outside heap(invalid)
                    return val
                elif leftC < self.heap.length() and rightC > self.heap.length() - 1:  #only left child is valid
                    min_val = self.heap.get_at_index(leftC)
                    min_index = leftC
                elif rightC < self.heap.length() and leftC > self.heap.length() - 1: #only right child is valid
                    min_val = self.heap.get_at_index(rightC)
                    min_index = rightC
                else:                                            #both children are valid
                    left_val = self.heap.get_at_index(leftC)
                    right_val = self.heap.get_at_index(rightC)
                    if left_val > right_val:
                        min_val = right_val
                        min_index = rightC
                    else:
                        min_val = left_val
                        min_index = leftC
                curr = self.heap.get_at_index(index)
                if curr > min_val:
                    self.heap.swap(index, min_index)
                    index = min_index
                else:
                    return val
                
    def build_heap(self, da: DynamicArray) -> None:
        """
        Recieves a DynamicArray of objects in any order and builds a min_heap from them

        Parameters:
            da(DynamicArray): The array of unsorted objects
        """
        self.heap = da
        index = int((self.heap.length() - 2) / 2)
        outter_index = index
        for i in range(outter_index, -1, -1):
            index = i
            switch = True
            while switch:
                left_index = 2 * index + 1
                right_index = 2 * index + 2
                if left_index < self.heap.length() and right_index > self.heap.length() - 1:  #only left child is valid
                    min_val = self.heap.get_at_index(left_index)
                    min_index = left_index
                elif right_index < self.heap.length() and left_index > self.heap.length() - 1: #only right child is valid
                    min_val = self.heap.get_at_index(right_index)
                    min_index = right_index
                else:                                            #both children are valid
                    left_val = self.heap.get_at_index(left_index)
                    right_val = self.heap.get_at_index(right_index)
                    if left_val > right_val:
                        min_val = right_val
                        min_index = right_index
                    else:
                        min_val = left_val
                        min_index = left_index
                curr = self.heap.get_at_index(index)
                if curr > min_val:
                    self.heap.swap(index, min_index)
                    index = min_index
                else:
                    switch = False


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
