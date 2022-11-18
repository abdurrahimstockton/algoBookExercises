#Implement an Array data structure as simplified type of list
class Array(object):
    def __init__(self, initialSize):  #constructor
        self.__a=[None]*initialSize #The array stored as a list
        self.__nItems=0 #No items in array initially

    def insert(self, item):  #Insert item at end
        self.__a[self.__nItems]= item # Items goes at current end
        self.__nItems+=1  #Increment number of items

    def search(self, item):
        for j in range(self.__nItems): #search among current items
            if self.__a[j]==item: # if found
                return self.__a[j]  #then return item

        return None  #If not found, return None

    def delete(self,item): # Delete the first instance
        for j in range(self.__nItems): #of an item
            if self.__a[j]==item: # Found item
                for k in range(j, self.__nItems):
                    self.__a[k]=self.__a[k+1] #move items from right over 1
                self.__nItems-=1
                return True
        return False#if not found

    def traverse(self,function=print):  #Traverse all items
        for j in range(self.__nItems):
            function(self.__a[j])