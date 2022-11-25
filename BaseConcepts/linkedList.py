# Constructor and tests for LinkedList Classes

class Link(object):  # One datum in a linked list
    def __init__(self, data, next=None):  # Constructor
        self.__data = data  # The datun for this link
        self.__next = next  # Reference to next Link

    def isLast(self):  # Test if link is last in the chain
        return self.__next is None  # True if & only if no next Link


class LinkedList(object):  # A linked list of data elements
    def __init__(self):  # Constructor
        self.__first = None  # Reference to first link

    def isEmpty(self):  # Test for empty list
        return self.__first is None  # True if & only if no 1st Link

