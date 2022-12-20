from functools import lru_cache

@lru_cache()
def f():
	return 1