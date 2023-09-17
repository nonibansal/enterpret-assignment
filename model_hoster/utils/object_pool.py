from typing import List
from queue import Queue


class ObjectPool:
    def __init__(self, objects: List[object]):
        self._pool = Queue(len(objects))

        for obj in objects:
            self._pool.put(obj)

    def acquire(self) -> object:
        return self._pool.get()

    def release(self, obj: object):
        self._pool.put(obj)
