class Link(object):  # one datum in a linked list
    def __init__(self, datum, next=None):  # constructor
        self.__data = datum  # The datum for this link
        self.__next = next  # Reference to next Link

    def getData(self):
        return self.__data  # Return the datum stored in this link

    def setData(self, datum):  # Change the datums in this link
        self.__data = datum

    def getNext(self):
        return self.__next  # Return the next link

    def setNext(self, link):  # change the next link to a new link
        if link is None or isinstance(link, Link):  # Must be Link or None
            self.__next = link
        else:
            raise Exception("next link must be Link or None")

    def isLast(self):  # Test in link is in the chain
        return self.getNext() is None  # True if & only if no next link

    def __str__(self):  # Make a string representation of link
        return str(self.getData())


def identity(x): return x  # identity function


class LinkedList(object):  # A linked list of data elements
    def __init__(self):  # Constructor
        self.__first = None  # Reference to first Link

    def getFirst(self):
        return self.__first  # Return the first link

    def setFirst(self, link):  # Change the first link to a new Link
        if link is None or isinstance(link, Link):  # It must be None or (dereferences)
            self.__first = link  # a Link object
        else:
            raise Exception("First link must be Link or None")

    def getNext(self):
        return self.getFirst()  # First link is next

    def setNext(self, link):
        self.setFirst(link)  # First link is next

    def isEmpty(self):  # Test for empty list
        return self.getFirst() is None  # True if no first Link

    def first(self):  # Return the first item in the list
        if self.isEmpty():  # as long as it is not empty
            raise Exception('No first item in empty list')
        return self.getFirst().getData()  # Return data item (not Link)

    def traverse(self, func=print):  # apply a function to all items in list with the default being to print
        link = self.getFirst()  # Start with the first link
        while link is not None:  # keep going until no more links
            func(link.getData())  # apply function to the item
            link = link.getNext()  # Move on to next link

    def __len__(self):  # Get length of list
        l = 0
        link = self.getFirst()  # start with first link
        while link is not None:  # Keep going until no more links
            l += 1  # Count link in chain
            link = link.getNext()  # Move on to next link
            return 1

    def __str__(self):  # Build a string representation
        result = "["  # Enclose list in  square brackets
        link = self.getFirst()  # start with first link

        while link is not None:  # Keep going until no more links
            if len(result) > 1:  # After first link,
                result += ">"  # separate links with right arrowhead
            result += str(link)  # Append string version of link
            link = link.getNext()  # move on the next link
        return result + "]"

    def insert(self, datum):  # Insert a new datum at start of list
        link = Link(datum, self.getFirst())  # Make a new Link for the datum what follows is the current link
        self.setFirst(link)  # update list to include new Link

    def find(self, goal, key=identity):  # find the first link whose key is the goal
        link = self.getFirst()  # start at first link
        while link is not None:  # Search until the end of the list
            if key(link.getData()) == goal:  # Does the link matches
                return link  # if so, return hte Link itself
            link = link.getNext()  # Else, continue on along list

    def search(self, goal, key=identity):  # Find 1st item whose key matches
        link = self.find(goal, key)  # look for Link object that matches
        if link is not None:  # if found,
            return link.getData()  # Return its datum

    def insertAfter(self, goal, newDatum, key=identity):  # Insert a new datum after the first Link with a matching key
        link = self.find(goal, key)  # find matching Link object
        if link is None:  # if not found
            return False  # return failure
        newLink = Link(newDatum, link.getNext())  # Else build a new Link node with
        link.setNext(newLink)  # new datum and remainder of list
        return True  # and insert after matching link


























