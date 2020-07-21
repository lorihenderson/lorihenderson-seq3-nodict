#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = "Lori Henderson"



class Node:
    """Stores keys and values using hashing."""
    def __init__(self, key, value=None):
        """Takes key which is required and value which is optional."""
        self.key = key
        self.hash = hash(self.key)
        self.value = value

    def __repr__(self):
        """Returns a human-readable representation of its key/value contents."""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """Allows key/values to be compared."""
        return self.key == other.key


class NoDict:
    """Implements key features of a dictionary without using the `dict` keyword """
    def __init__(self, num_buckets=10):
        """
        Takes in an optional number of buckets.
        Implements the buckets to be a list of lists.
        Ten buckets is the default value.
        """
        self.buckets = [[] for _ in range(num_buckets)]
        self.size = num_buckets


    def __repr__(self):
        """Return a string representing the NoDict contents."""
        # We want to show all the buckets vertically
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}' for i, bucket in enumerate(self.buckets)])


    def add(self, key, value=None):
        """
        Accepts a new key and value.
        Stores it into the NoDict instance.
        Should not allow duplicate keys.
        """
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.size]

        for k_v in bucket:
            if k_v == new_node:
                bucket.remove(k_v)
        bucket.append(new_node)


    def get(self, key):
        """
        Returns value of key, value pair.
        If the key is not found, raise a KeyError exception.
        """
        node_to_find = Node(key)
        bucket = self.buckets[new_node.hash % self.size]

        for k_v in bucket:
            if k_v == node_to_find:
                return k_v.value

        raise KeyError(f"{key} not found")


    def __getitem__(self, key):
        """Allows user to enable square-bracket notation to get the value of a key."""
        return self.get(key)


    def __setitem__(self, key, value):
        """Allows user to enable square-bracket notation to set the value of a key."""
        self.add(key, value)