import unittest
from LRUCache import LRUCache
from test.utils import (get_key_value_pairs,
                        get_random_key,
                        get_random_string,
                        get_list)
import random


class TestLRUCache(unittest.TestCase):

    def setUp(self):
        self.capacity = 10
        self.lrucache = LRUCache(self.capacity)

    def test_addkey(self):
        # Add Element to cache
        key = get_random_key()
        value = get_random_string()
        self.lrucache.put(key, value)
        self.assertEqual(self.lrucache.store[key].value, value)
        self.assertEqual(self.lrucache.current_size, 1)

    def test_getkey(self):
        # Add Element to cache
        key = get_random_key()
        value = get_random_string()
        self.lrucache.put(key, value)
        self.assertEqual(self.lrucache.get(key), value)
        self.assertEqual(self.lrucache.current_size, 1)

    def test_getnonexistantkey(self):
        # Add Element to cache
        key = get_random_key()
        self.assertEqual(self.lrucache.get(key), -1)
        self.assertEqual(self.lrucache.current_size, 0)

    def test_deletekey(self):
        key = get_random_key()
        value = get_random_string()
        self.lrucache.put(key, value)
        self.assertEqual(self.lrucache.current_size, 1)
        self.lrucache.delete(key)
        self.assertEqual(self.lrucache.get(key), -1)
        self.assertEqual(self.lrucache.head, None)

    def test_deletenonexistantkey(self):
        key = get_random_key()
        self.lrucache.delete(key)

    def test_resetcache(self):
        kv_pairs = get_key_value_pairs(length=5)
        # Insert keys
        for key, value in kv_pairs:
            self.lrucache.put(key, value)

        self.assertEqual(self.lrucache.current_size, len(kv_pairs))
        self.lrucache.reset()
        self.assertEqual(self.lrucache.current_size, 0)
        self.assertEqual(self.lrucache.head, None)
        self.assertEqual(self.lrucache.tail, None)
        self.assertEqual(self.lrucache.store, {})
        # Add get cache list

    def test_updatekey(self):
        key = get_random_key()
        value = get_random_string()
        self.lrucache.put(key, value)
        self.assertEqual(self.lrucache.get(key), value)
        value = get_random_string()
        self.lrucache.put(key, value)
        self.assertEqual(self.lrucache.get(key), value)
        self.assertEqual(self.lrucache.current_size, 1)

    def test_lrukey_addition(self):
        """[Test which is the top key after inital write]
        """
        kv_pairs = get_key_value_pairs(length=5)
        # Insert keys
        for key, value in kv_pairs:
            self.lrucache.put(key, value)

        self.assertEqual(self.lrucache.current_size, len(kv_pairs))
        self.assertEqual(self.lrucache.head.key, kv_pairs[-1][0])

    def test_lrukey_access(self):
        """[Test which is the top key after read key access]
        """
        kv_pairs = get_key_value_pairs(length=5)
        # Insert keys
        for key, value in kv_pairs:
            self.lrucache.put(key, value)

        self.assertEqual(self.lrucache.current_size, len(kv_pairs))
        rand_index = random.randint(*(0, len(kv_pairs)-1))
        self.lrucache.get(kv_pairs[rand_index][0])
        self.assertEqual(self.lrucache.head.key, kv_pairs[rand_index][0])

    def test_lrukey_update(self):
        """[Test whcih is the top key after write key update]
        """
        kv_pairs = get_key_value_pairs(length=5)
        # Insert keys
        for key, value in kv_pairs:
            self.lrucache.put(key, value)

        self.assertEqual(self.lrucache.current_size, len(kv_pairs))
        rand_index = random.randint(*(0, len(kv_pairs)-1))
        value = get_random_string()
        self.lrucache.put(kv_pairs[rand_index][0], value)
        self.assertEqual(self.lrucache.head.key, kv_pairs[rand_index][0])
        self.assertEqual(self.lrucache.head.value, value)


class TestLRUCacheOverflow(unittest.TestCase):

    def setUp(self):
        self.capacity = 10
        self.lrucache = LRUCache(self.capacity)

    def test_addmaxcapacity(self):
        kv_pairs = get_key_value_pairs(length=self.capacity)
        # Insert keys
        for key, value in kv_pairs:
            self.lrucache.put(key, value)

        self.assertEqual(self.lrucache.current_size, self.capacity)

    def test_addovermaxcapacity(self):
        kv_pairs = get_key_value_pairs(length=self.capacity*2)
        # Insert keys
        for key, value in kv_pairs:
            self.lrucache.put(key, value)

        self.assertEqual(self.lrucache.current_size, self.capacity)
        self.assertEqual(self.lrucache.head.key, kv_pairs[-1][0])

    def test_queuesnapshot(self):
        kv_pairs = get_key_value_pairs(length=self.capacity*2)
        # Insert keys
        for key, value in kv_pairs:
            self.lrucache.put(key, value)

        # Keep track of key order manually
        keys = list(map(
            lambda item: item[0],
            kv_pairs[self.capacity:])
            )[::-1]

        # Add new element
        key = get_random_key()
        value = get_random_string()
        self.lrucache.put(key, value)
        keys.pop(-1)
        keys.insert(0, key)

        # Access last element
        self.lrucache.get(keys[-1])
        keys.insert(0, keys.pop(-1))

        # Update an element
        rand_index = random.randint(*(0, len(keys)-1))
        self.lrucache.put(keys[rand_index], get_random_string())
        keys.insert(0, keys.pop(rand_index))

        # Check Linked List
        self.assertListEqual(keys, get_list(self.lrucache.head))
