import unittest
from CacheNode import CacheNode


class TestCacheNode(unittest.TestCase):
    def setUp(self):
        test_key = 10
        test_value = "Hello World"
        self.cache_node = CacheNode(test_key, test_value)

    def test_getKey(self):
        self.assertEqual(self.cache_node.key, 10)

    def test_getValue(self):
        self.assertEqual(self.cache_node.value, "Hello World")
