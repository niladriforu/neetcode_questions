class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Key -> Value storage
        self.usage_order = []  # Stores keys in order of usage (Least Recently Used at index 0)

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the key to the end to mark it as recently used
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache[key]
        return -1  # Key not found

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move key to the end
            self.usage_order.remove(key)
        elif len(self.cache) >= self.capacity:
            # Remove the least recently used key (first in usage_order)
            lru_key = self.usage_order.pop(0)
            del self.cache[lru_key]

        # Add new key-value pair
        self.cache[key] = value
        self.usage_order.append(key)
