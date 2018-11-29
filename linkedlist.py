#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
         Best case runtime: O(1) Worst case runtime: O(n)"""
      
        if self.is_empty(): # Gets the length in constant time if there are no elements
            return 0 
        else: # Yields a runtime of O(n) since in a size of n, it will need to loop through n items
            current = self.head
            counter = 0
            while current is not None:
                counter += 1
                current = current.next
            return counter

            

    def append(self, item):
        """Insert the given item at the tail of this linked list.
           Both Best and Worst Case: O(1) since we have a tail attribute to be instantly used, if we didnt, we would have to iterate through the linked list to get to the end and would yield a runtime of O(n)
        """

        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(item)
        if self.tail is not None: 
            self.tail.next = new_node 
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and Worst case run time O(1) since we have a head property that we can use.
        """
        new_node = Node(item)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
         Best case running time: O(1) if the item is the first element in the LL
         Worst case running time: O(n) if the element was not in the linked list 
        """


        if self.head is not None:
            current = self.head 
            for _ in range(self.length()):
                if quality(current.data):
                    return current.data
                else:
                    current = current.next
            return None


        

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
         Best case running time: O(1) under the conditions of the item needed to be deleted is the first element
         Worst case running time: O(n) if the element is not in the LL and will iterate through the LL of size n"""

        
        if self.is_empty():
            raise ValueError("Linked List is empty")
        
        if self.head.data == item:
            self.head = self.head.next
            if self.tail.data == item:
                self.tail = None
            return

        current = self.head 
        previous = None

        while current:
            if current.data != item:
                previous = current 
                current = current.next
            else:
                if self.tail.data == item:
                    if previous:
                        previous.next = None 
                        self.tail = previous
                        return
                    else:
                        self.head = None
                        self.tail = None
                        return
                else:
                    previous.next = current.next
                    return
        
        raise ValueError('Item not found: {}'.format(item))
         
                 


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()