# just a toy example to see how heap works

import math
class myHeap:
    def __init__(self):
        ''' This is a SET implementation - Assuming the key and values are the same '''
        self.array = [] # should be a private instance variable
    
    # only the three methods below are supposed to be used by the instance
    def heapify(self,mylist):
        self.array = mylist.copy()
        n = len(self.array)
        # Only the first half of the list heapify_down()
        for i in range(n//2,-1,-1):
            self._max_heapify_down(i)
    def insert(self, x):
        # insert at the end
        self.array.append(x)
        # heapify up
        self._max_heapify_up(len(self.array)-1)
    
    def delete_max(self):
        # swap first and last
        temp = self.array[0]
        self.array[0] = self.array[-1]
        self.array[-1]= temp
        # remove last
        self.array.pop()
        print("In max",self.array)
        # heapify down 
        self._max_heapify_down(0)
    
    # all the below methods are supposed to be private
    def _max_heapify_up(self,i):
        ''' The method restores the heap property of child with the parent'''
        if i==0:
            return
        pidx = self._parent(i)
        if self.array[pidx] < self.array[i]:
            temp = self.array[pidx]
            self.array[pidx] = self.array[i]
            self.array[i]= temp
            # recurse on parent
            self._max_heapify_up(pidx)
        
    def _max_heapify_down(self,i):
        '''This method restores the heap property of parent with the two child elements'''
        if self._isleaf(i):
            return
        
        # find max amongst child nodes
        c1,c2 = self._child(i)
        print(c1,c2)
        if c2<len(self.array):
            if self.array[c1] > self.array[c2]:
                maxidx = c1
            else:
                maxidx = c2
            maxval = max(self.array[c1], self.array[c2]) 
        else:
            maxval = self.array[c1]
            maxidx = c1
        # the max Child is compared with the parent and swapped if necessary
        if maxval > self.array[i]:
            temp = self.array[maxidx]
            self.array[maxidx]= self.array[i]
            self.array[i]= temp
            self._max_heapify_down(maxidx)
        
    
    # helper functions
    def _parent(self,i):
        return math.floor((i-1)/2)
    
    def _child(self,i):
        return 2*i+1, 2*i+2
    
    def _isleaf(self,i):
        c1,c2 = self._child(i)
        if c1>len(self.array)-1 and c2>len(self.array)-1:
            return True
        else:
            return False
        
# testing the heap
mylist = [5,8,7,6,3]
heap = myHeap()
heap.heapify(mylist)
print(heap.array)
heap.delete_max()
print(heap.array)
heap.insert(12)
heap.insert(10)
print(heap.array)


