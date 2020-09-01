class CacheNode:
    """[Class to represent cache node]
    """
    def __init__(self, key, value):
        """[Initiate empty node]

        Args:
            key ([int]): [key in hash table]
            value ([str]): [data to store]
        """
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
