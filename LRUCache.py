import pprint
from CacheNode import CacheNode


class LRUCache:
    """Class that represents an Least Recently Used
       Cache
    """

    def __init__(self, size):

        if size <= 0:
            raise ValueError('Total size must be greater than 0')

        self.size = size

        # Hashmap to store key/valye pair
        self.store = {}

        # Pointer to start of linked list to increase
        self.head = None

        # Pointer to end of linked list to speed remove access
        self.tail = None

        # Store current size
        self.current_size = 0

    def put(self, key, value):
        """[method to put value in cache]

        Args:
            key ([str, int]): [key to access cached value]
            value ([type]): [value to place in cache]
        """

        # If key is in hash, update and insert at head
        if key in self.store:
            cache_node = self.store.get(key)
            # Update Value
            cache_node.value = value
            # Remove the node from position and place insert it as head
            self._remove_node(cache_node)
            self._insert_node(cache_node)
        else:
            # Create new node instance
            cache_node = CacheNode(key, value)

            # Check if Space is avaiable for the node
            if self.current_size == self.size:
                # Remove last node from queue and map
                self.delete(self.tail.key)

            # Add Key to Storage
            self.store[key] = cache_node

            # Insert Node to Queue
            self._insert_node(cache_node)

    def get(self, key):
        """[method to get value of given cache_nodekey from cache]

        Args:
            key ([int]): [key to access cached value]

        Returns:
            [str]: [cached value]
        """
        # Check if value is in cache if not return -1
        cache_node = self.store.get(key)
        if not cache_node:
            return -1

        # If node is in cache, return node value and add value to queue head
        self._remove_node(cache_node)
        self._insert_node(cache_node)
        return cache_node.value

    def delete(self, key):
        """[method to delete a key from the cache]

        Args:
            key ([int]): [key to delete]
        """
        # Check if key exists in dictionary
        if key not in self.store:
            return

        # Remove Node Instance
        self._remove_node(self.store.get(key))

        # Remove key from instance
        self.store.pop(key)

    def reset(self):
        """[method to clear cache]
        """

        # Reset Hashmap
        self.store.clear()

        # Clear refrences for GC
        self.head = None
        self.tail = None

        # Reset Current size
        self.current_size = 0

    def _remove_node(self, cache_node):
        """[method to remove node from double linked list if in queue]

        Args:
            cache_node ([CacheNode]): [cache node to remove from linked list]
        
        Returns:
            [type]: [description]
        """
        # Check if size if greater than 0
        if (self.current_size == 0):
            return cache_node

        # Check if node is in queue
        if (cache_node.prev is None and cache_node.next is None):
            if self.head == cache_node:
                self.head = None
                self.tail = None
                self.current_size -= 1

            return cache_node

        # Delete Node
        if (cache_node.next):
            cache_node.next.prev = cache_node.prev
        if (cache_node.prev):
            cache_node.prev.next = cache_node.next

        # Update head and tail
        # End of Queue
        if (cache_node.prev is None):
            self.tail = cache_node.next

        # Start of Queue
        if (cache_node.next is None):
            self.head = cache_node.prev

        # Set Cache Node to None
        cache_node.next = None
        cache_node.prev = None

        self.current_size -= 1
        return cache_node

    def _insert_node(self, cache_node):
        """[method to add cache node to the double linked list]

        Args:
            cache_node ([CacheNode]): \
                [cache node to add to the head of the linked list]

        Returns:
            [CacheNode]: [cache node that is added]
        """
        # Check if node is in DLL
        if (cache_node.next or cache_node.prev):
            return cache_node

        if self.head == cache_node:
            return cache_node

        # If head is not empty
        if self.head:
            cache_node.prev = self.head
            self.head.next = cache_node

        # Inital case with no nodes
        if not self.head:
            self.tail = cache_node

        # Set Head to current node
        self.head = cache_node

        # Update size
        self.current_size += 1

        return cache_node

    def print_cache_queue(self):
        """[method to print double linked linked content]
        """
        print(
            f'Current Size: {self.current_size}'
        )
        current = self.head
        print("HEAD-->", end=' ')
        while current:
            print(f'[Key: {current.key}, Value: {current.value}]-->', end=' ')
            current = current.prev
        print("NULL")
