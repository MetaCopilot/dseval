import sys
import time

import pytest

from .limit import TimeLimitError, get_memory, limit_memory, limit_time


def test_memory_error():
    memory = get_memory()

    @limit_memory(1)
    def f():
        L = [0 for _ in range(2 * 10**6 // sys.getsizeof(0))]  # allocate 2 Mo

    try:
        f()
    except MemoryError:
        return
    else:
        assert False


def test_memory_noerror():
    memory = get_memory()

    @limit_memory(1)
    def f():
        L = [0 for _ in range(10**5 // sys.getsizeof(0))]  # allocate 100 Ko

    f()


def test_limit_time():
    @limit_time(1)
    def f():
        time.sleep(2)

    with pytest.raises(TimeLimitError):
        f()


def test_time_nolimit():
    @limit_time(2)
    def f():
        time.sleep(1)

    f()
