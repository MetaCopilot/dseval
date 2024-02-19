# Got inspirations from https://github.com/fortierq/flimit

from contextlib import contextmanager
import time
import signal
import resource
import os, psutil


class TimeLimitError(Exception):
    pass


@contextmanager
def limit_time(seconds: int):
    """Decorator to limit time usage of a function. Raise TimeLimitError when the limit is exceeded.

    Args:
        seconds (int): Maximum computation time of the function, in seconds.

    Raises:
        TimeLimitError: When the function reaches the limit.
    """

    def signal_handler(signum, frame):
        raise TimeLimitError

    prev_handler = signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, prev_handler)


@contextmanager
def limit_memory(megabytes: int):
    """Decorator to limit memory usage of a function. Raise MemoryError when the limit is exceeded.

    Args:
        megabytes (int): Maximum number of megabytes the function can allocate. -1 for no limit.

    Raises:
        MemoryError: When the function reaches the limit.
    """

    if megabytes <= 0:
        yield
        return

    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    soft_new = get_memory() + megabytes * 1048576
    if soft == -1 or soft_new < soft:
        resource.setrlimit(resource.RLIMIT_AS, (soft_new, hard))
    try:
        yield
    finally:
        resource.setrlimit(resource.RLIMIT_AS, (soft, hard))


def get_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss  # octets


class measure_time:
    """Context manager to measure time usage of a block of code."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.interval = self.end - self.start
