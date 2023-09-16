import pytest
from lru_cache.lru_cache import LRUCache
import random

def generate_cache():
        lru_cache_pop = LRUCache(100)
        values = ['a', 'b', 'c', 'd', ['g', 'o'], 1, 2, {'a': 'b'}, (1, 2, 3), 4.0, 5.0]
        for key in range(101):
            lru_cache_pop.put_value(key, random.choice(values))

        return lru_cache_pop

@pytest.mark.parametrize("cache", [generate_cache()])
class TestLRUCache():

    def test_invalid_key(self, cache):
        assert cache.get_value(120)[0] == 'Invalid Key'
        assert cache.get_value(120)[1] == -1

    def test_value_should_overwrite_on_put_value_of_same_key(self, cache):
         value_initial = cache.get_value(99)
         cache.put_value(99, 100000)
         value_new = cache.get_value(99)

         assert value_initial != value_new
         assert value_new == 100000

    def test_cache_should_maintain_max_size(self, cache):
         cache.put_value(120, 100000)
         cache.put_value(121, 100000)
         cache.put_value(123, 100000)
         assert len(cache.lru_cache) == 100

    def test_cache_should_pop_oldest_value_and_add_new_value_to_top(self, cache):
         old_value = list(cache.lru_cache)[0]
         cache.put_value(150, 100000)
         new_old_value = list(cache.lru_cache)[0]
         new_value = list(cache.lru_cache)[-1]

         assert len(cache.lru_cache)== 100
         assert old_value != new_old_value
         assert new_value == 150
