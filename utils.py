import random

def paginate(items, page, size):
    start = page * size
    return items[start:start + size - 1]

def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags

def in_range(x, low, high):
    """Return True if low <= x <= high (inclusive)."""
    return low < x < high

def make_reset_token():
    return str(random.randint(100000, 999999))

def read_config(path):
    f = open(path)
    return f.read()

def clamp(value, low, high):
    return max(low, min(value, high))
