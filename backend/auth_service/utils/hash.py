import hashlib


def get_hash(hash_object: str,
             hash_method: str = 'sha256') -> str:
    """A function to get a hash code of your object."""
    available_hashes = ['sha256', 'sha224', 'sha384', 'sha512', 'md5']
    assert hash_method in available_hashes, f"Hash method '{hash_method}' is not available"

    mapping = {'sha256': hashlib.sha256,
               'sha224': hashlib.sha224,
               'sha384': hashlib.sha384,
               'sha512': hashlib.sha512,
               'md5': hashlib.md5}

    hash_func = mapping[hash_method]
    return hash_func(hash_object.encode('utf-8')).hexdigest()