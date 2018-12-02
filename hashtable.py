#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
         Running time: O(n) since it will have to iterate through buckets of size n"""
 
        all_values = []
        for bucket in self.buckets: # Will have to iterate through n buckets
            for key, value in bucket.items():
                all_values.append(value)
        return all_values        




    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) since it will have to iterate through buckets of size n"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:  # Will have to iterate through n buckets
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
         Running time: O(n) since it will have to iterate through buckets of size n """

        len_counter = 0
        for bucket in self.buckets: # Will have to iterate through n buckets
            len_counter += len(bucket.items())
        return len_counter


    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
         Best Case: O(1) with no collisions Worst Case: O(m) lots of collisions and will have to iterate through linked list"""

        keys = self.keys()
        if key in keys:
            return True
        else:
            return False

        


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
         Best Case: O(1) no collisions Worst Case: O(m) with lots of collisions and will have to iterate through linked list of size m"""

        if self.contains(key):
            index = self._bucket_index(key)
            bucket = self.buckets[index]
            for key_search,value in bucket.items():
                if key_search == key:
                    return value
                else:
                    continue
            raise KeyError('Key not found: {}'.format(key))             

        else:
            raise KeyError('Key not found: {}'.format(key))
            

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(1) with no collisions Worst Case: O(m) with lots of collisions and will have to iterate through an entire list of size m"""

        bucket = self.buckets[self._bucket_index(key)]
                    
        old_key = bucket.find(lambda possible_key: possible_key[0] == key)
        if old_key is not None:
            bucket.delete(old_key)
        
        bucket.append((key,value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""


        bucket = self.buckets[self._bucket_index(key)]

        delete_key = bucket.find(lambda possible_key: possible_key[0] == key)
        
        if delete_key is not None:
            value = self.get(delete_key[0])
            bucket.delete(delete_key)
        else:
            raise KeyError('Key not found: {}'.format(key))
        
                


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()