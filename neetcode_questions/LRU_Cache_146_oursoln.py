from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.mydict = {}
        self.usage_order = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.mydict:
            self.usage_order.remove(key)
            self.usage_order.append(key)
        return self.mydict.get(key, -1)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.mydict.get(key):
            self.usage_order.remove(key)
            self.usage_order.append(key)
            self.mydict[key] = value
        elif len(self.mydict) >= self.capacity:
            key_to_evict = self.usage_order.pop(0)
            if key_to_evict in self.mydict:
                del self.mydict[key_to_evict]
            self.mydict[key] = value
            self.usage_order.append(key)
        elif len(self.mydict) < self.capacity:
            self.usage_order.append(key)
            self.mydict[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)