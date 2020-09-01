# LRU Cache

# Summary
This project demonstrates the basic functionality of an Least Recently Used (LRU) Cache that can be initialized with a constant max capacity, with the following properties.
    
The user can place a (key, value) pair in the cache using the .put(key, value) method and the last key to be placed in the cache has the highest priority in the cache. When the user updates the value of a key that is already in the cache, the value is updated and that key has the highest cache priority. If the cache has reached its max capacity and a new (key,value) pair needs to be inserted, the key with the lowest priority (LRU) is evicted from the cache and the new (key, value) pair is added to the cache with the rules above. 

The user can obtain a value from the cache with the .get(key) method. If the key is not in the cache a -1 response is returned. If the key is present in the cache the value is returned and that key is placed in the cache with the highest priority

The user can delete a key from cache with the .delete(key) method. If the key is not in the cache no operation is performed and nothing is returned. Otherwise, the key is deleted from the cache. 

The user can reset the cache with the method .reset(). This clears the cache of all key, value pairs as well the cache key priorities. 

## Installation

### Environment

First create a fresh Python 3 virtual environment. This can be done without any additional dependencies via:

```sh
# Create a new Python virtual environment
python3 -m venv NAME
```

This will create the virtual environment within the folder _NAME_ in your current directory.

To activate the virtual environment you need to execute the activate shell script within that virtual environment.

```sh
# Activate a virtual environment
source ./NAME/bin/activate
```

### Dependencies

With the environment setup and activated, change the directory to the root LRUCache folder. Then install runtime dependencies by executing:

```sh
# Install runtime dependencies
pip3 install -e .
```

## Testing

To run the complete test suite run the following command in the root LRUCache folder:

```sh
# Run entire test suite
python3 -m unittest -v
```
