class Link(object):  #one datum in a linked list
    def __init__(self, datum, next=None): #constructor
        self.__data = datum #The datum for this link
        self.__next = next #Reference to next Link

    def getData(self):
        return self.__data  #Return the datum stored in this link

    def setData(self, datum):  #Change the datums in this link
        self.__data = datum

    def getNext(self): return self.__next # Return the next link

    def setNext(self, link): #change the next link to a new link
        if link is None or isinstance(link, Link): #Must be Link or None
            self.__next = link
        else:
            raise Exception("next link must be Link or None")

    def isLast(self): #Test in link is in the chain
        return self.getNext() is None #True if & only if no next link

    def __str__(self): # Make a string representation of link
        return str(self.getData())



class LinkedList(object):  # A linked list of data elements
    def __init__(self):  # Constructor
        self.__first = None  # Reference to first Link

    def getFirst(self):
        return self.__first  # Return the first link

    def setFirst(self, link):  # Change the first link to a new Link
        if link is None or isinstance(link, Link):  # It must be None or
            self.__first = link  # a Link object
        else:
            raise Exception("First link must be Link or None")

    def getNext(self):
        return self.getFirst()  # First link is next

    def setNext(self, link):
        self.setFirst(link)  # First link is next

    def isEmpty(self):  # Test for empty list
        return self.getFirst() is None  # True iff no first Link

    def first(self):  # Return the first item in the list
        if self.isEmpty():  # as long as it is not empty
            raise Exception('No first item in empty list')
        return self.getFirst().getData()  # Return data item (not Link)