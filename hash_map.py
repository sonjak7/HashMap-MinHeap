# Description: Implementation of a hash map using a dynamic array, and a singly linked list for collision resolution

# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Clears all items in hash map
        """
        for i in range(self.buckets.length()):
            self.buckets.set_at_index(i, LinkedList())
        self.size = 0

    def get(self, key: str) -> object:
        """
        Returns the value of a node in the hash map given its key

        Parameters:
            key(str): The key of the node being searched for

        Returns:
            node.value(object): Value of the node with the provided key
            None: If the given key was not in the hash map
        """
        for i in range(self.buckets.length()):
            node = self.buckets.get_at_index(i).contains(key)
            if node != None:    #if there was a node with given key in one of the linked lists
                return node.value
        return None     #no node was found with the given key in any of the linked lists

    def put(self, key: str, value: object) -> None:
        """
        Places a new node into the hash map given a key and value

        Parameters:
            key(str): The key location of the new node
            value(object): The value of the node being inserted
        """
        index = self.hash_function(key)
        index = index % self.buckets.length()   #set index to valid spot in array
        links = self.buckets.get_at_index(index)
        existing = links.contains(key)
        if existing != None:            #if there is a node with the same key, put in the new value there
            existing.value = value
        else:                           #if this key is unique, create new node with this value
            links.insert(key, value)
            self.size += 1

    def remove(self, key: str) -> None:
        """
        Removes a node from the hash map given its key

        Parameters:
            key(str): The key of the node being removed   
        """   
        for i in range(self.buckets.length()):
            if (self.buckets.get_at_index(i).remove(key) == True):  #if the remove function found a matching node
                self.size -= 1                                      #in any linked list, and has removed it
                return

    def contains_key(self, key: str) -> bool:
        """
        Returns whether a given key is in the hash map or not

        Parameters:
            key(str): The key being searched for

        Returns:
            True(bool): If the key is in the hash map
            Flase(bool): If the key is not in the hash map
        """
        for i in range(self.buckets.length()):
            if self.buckets.get_at_index(i).contains(key) != None:  #if node with given key was in this one of the
                return True                                         #linked lists in hash map
        return False

    def empty_buckets(self) -> int:
        """
        Returns the number of empty buckets(linked lists) in the hash map

        Returns:
            counter(int): The number of empty buckets at the end of function execution
        """
        counter = 0
        for i in range(self.buckets.length()):
            if self.buckets.get_at_index(i).length() == 0:  #if linked list's length is 0, increment empty counter
                counter += 1
        return counter

    def table_load(self) -> float:
        """
        Returns the load factor of the hash map

        Returns:
            float(filled) / float(self.buckets.length()) (float): The summation of all bucket sizes divided by number of buckets
        """
        if self.buckets.length() == 0:  #if hash map is empty return 0
            return 0
        filled = 0
        for i in range(self.buckets.length()):
            filled += self.buckets.get_at_index(i).size     #add the sizes of each linked list together
        return float(filled) / float(self.buckets.length())

    def resize_table(self, new_capacity: int) -> None:
        """
        Resizes the hash map to fit a new capacity, all existing nodes are rehashed into new table

        Parameters:
            new_capacity(int): The capacity of the new hash table, must be > 1
        """
        if new_capacity < 1:    #invalid capacity
            return
        new_table = DynamicArray()  #new hash table of new capacity
        for _ in range(new_capacity):
            new_table.append(LinkedList())  #initialize new_table with empty linked lists
        for i in range(self.capacity):
            links = self.buckets.get_at_index(i)    #links will iterate through each linked list in old hash table
            for node in links:      #for each node in current linked list...
                index = self.hash_function(node.key) % new_capacity
                location = new_table.get_at_index(index)    #find location in new_table for current node
                location.insert(node.key, node.value)       #insert this node into the new linked list at found location
        self.capacity = new_capacity    #update capacity
        self.buckets = new_table        #update buckets to the newly generated hash map

    def get_keys(self) -> DynamicArray:
        """
        Returns all of the keys stored in the hash map

        Returns:
            key_arr(DynamicArray): Array of all hash map keys
        """

        key_arr = DynamicArray()
        for i in range(self.capacity):  
            links = self.buckets.get_at_index(i)    #links will iterate through each linked list
            for node in links:
                key_arr.append(node.key)    #for each node in linked list, append it's key to key_arr
        return key_arr

# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
