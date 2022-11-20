#comparing keys

def selectionSort(self): #Sort by selecting min and swaping min to the left most
    for outer in range(self.__nItems-1):
        min=outer     #Assume min to at the leftmost
        for inner in range(outer+1, self.__nItems): #Hunt until to the right most
            if self.__a[inner]<self.__a[min]: #if new min is found
                min=inner # update min index
        #__a[min] is smallest among __a[outer].....__a[_nItems-1]
        self.swap(outer, min)  #swap leftmost and min

