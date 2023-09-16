from collections import OrderedDict

class LRUCache():
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.lru_cache = OrderedDict()

    def get_value(self, key: int | str):
        try:
            value = self.lru_cache.get(key)
            self.lru_cache.move_to_end(key)
            return value
        except KeyError:
            return ('Invalid Key', -1)
        except Exception as e:
            return (f'Unknown exception: {e}', -1)

    def put_value(self, key: int | str, value: any):
        if len(self.lru_cache) >= self.max_size:
            print(f'Max cache size met, current cache size: {len(self.lru_cache)}')
            self.lru_cache.popitem(last=False)
            self._add_object(key, value)
        else:
            print(f'Max cache size not met, current cache size: {len(self.lru_cache)}')
            self._add_object(key, value)
        
    def _add_object(self, key: int | str, value: any):
        self.lru_cache.update({key: value})
