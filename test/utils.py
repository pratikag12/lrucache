import random
import string


keyrange = (0, 100)
alphabet = string.ascii_lowercase


def get_random_key(range=keyrange):
    return random.randint(*range)


def get_random_string(length=5):
    return ''.join(random.choice(alphabet) for i in range(length))


def get_key_value_pairs(length=10):
    """[Generate a random unique set of (key, value) pairs]

    Args:
        length (int, optional): [total length of unique pairs]. Defaults to 10.

    Returns:
        [List]: [unique (key, value) pairs]
    """
    kv_pairs = []
    keys = []
    for i in range(length):
        key = get_random_key()
        generation_count = 1
        while (key in keys):
            key = get_random_key()
            generation_count += 1
            # To ensure we are not stuck in loop to create random keys
            if generation_count > 10:
                raise RuntimeError('Unable to generate random values')
        value = get_random_string()
        kv_pairs.append((key, value))
        keys.append(key)

    return kv_pairs


def get_list(head):
    """[Get list of ordered keys from linked list]

    Args:
        linked_list ([object]): [pointer to cacheNode objects]
    """
    # Return empty list of key
    if not head:
        return []

    keys = []
    current = head
    while current:
        keys.append(current.key)
        current = current.prev

    return keys
