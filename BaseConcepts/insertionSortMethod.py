def insertionSort(self): # Sorty by repeated inserts
    for outer in range(1, self.__nItems): # mark element of 'outer' index position
        temp=self.__a[outer]  #Store marked elem in temp
        inner=outer   #Inner loop starts at mark
        while inner>0 and temp<self.__a[inner-1]: #If marked item is smaller, then
            self.__a[inner]=self.__a[inner-1] # shift element to the right
            inner-=1
        self.__a[inner]=temp #move marked elem to 'hole'

