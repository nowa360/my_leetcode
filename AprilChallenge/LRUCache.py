from Libraries.DoubleLinkedList import DoubleLinkedList
from Libraries.Node import Node

"""
    Apr.24 Challenge
    146. LRU Cache - M
    https://leetcode.com/problems/lru-cache/

    Doubly linked list + HashMap
    
    Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following 
    operations: get and put. 

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1. 
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
it should invalidate the least recently used item before inserting a new item. 

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache_dict = {}
        self.dll = DoubleLinkedList(None)
        self.length = 0

    def get(self, key):  # O(1)
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache_dict:
            return -1
        else:
            get_node = self.cache_dict[key]
            self.dll.remove_node(get_node)
            self.dll.add_node(get_node)

            # print("get",self.cache_dict)
            return get_node.val[1]

    def put(self, key, value):  # O(1)
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        new_node = Node([key, value])
        if key not in self.cache_dict:
            self.cache_dict[key] = new_node
            self.dll.add_node(new_node)
            self.length += 1

            if self.length > self.capacity:
                # counter-intuition: insert from the tail and pop from the head
                last_node = self.dll.get_first()
                self.dll.remove_node(last_node)
                # print(last_node.val[0])
                del self.cache_dict[last_node.val[0]]

        else:  # in cache
            old_node = self.cache_dict[key]
            self.dll.remove_node(old_node)
            self.dll.add_node(new_node)
            self.cache_dict[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
