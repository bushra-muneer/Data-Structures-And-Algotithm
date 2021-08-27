from math import floor

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Queue:
    my_list = []
    newlist = []

    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        self.my_list.append(data)
        self.newlist= self.my_list.copy()
        temp = Node(data)
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

    def first(self):
        return self.head.data

    def selectiosort(self):
        for i in range(0, len(self.my_list) - 1):
            min_pos = i
            for j in range(i + 1, len(self.my_list)):
                if self.my_list[min_pos] > self.my_list[j]:
                    min_pos = j
            self.my_list[i], self.my_list[min_pos] = self.my_list[min_pos], self.my_list[i]
        print(self.my_list)

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    def isEmpty(self):

        if self.head is None:
            return True
        else:
            return False

    def printqueue(self):
        print("***ELEMENTS IN QUEUE ARE***"+"\n")
        temp = self.head
        while temp is not None:
            print(temp.data, end="'")
            temp = temp.next

    def serach(self,data):
        count=0
        if self.head==None:
            return -1
        current=self.head
        while current!=None:
            count+=1
            if current.data==data:
                print("Element Found at Position",count)
                return
            if current.next!=None:
                current=current.next
            else:
                break
        print("search not found")
    def insertion_sort(self):
        for i in range(1,len(self.my_list)):
            j = self.my_list[i]
            x=i-1
            while x >= 0 and j<self.my_list[x]:
                self.my_list[x +1]=self.my_list[x]
                x =  x- 1
                self.my_list[x+1]=j
        print(self.my_list)

    def bubble_Sort(self):

        if (self.head == None):
            return
        else:
            current = self.head
            while (current.next != None):

                index = current.next
                while (index != None):

                    if (current.data > index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next

    def merge(self, first, second):

        if first is None:
            return second

        if second is None:
            return first

        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second

    def mergeSort(self, tempHead):
        if tempHead is None:
            return tempHead
        if tempHead.next is None:
            return tempHead
        second = self.split(tempHead)

        tempHead = self.mergeSort(tempHead)
        second = self.mergeSort(second)

        return self.merge(tempHead, second)


    def split(self, tempHead):
        fast = slow = tempHead
        while (True):
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        return temp

    def printList(self, node):
        temp = node

        while (node is not None):
            print(node.data)
            temp = node
            node = node.next

    def binary_Search(self,search):
        n = len(self.my_list)
        mid = 0
        l = 0
        r = n - 1
        while l < r:
            mid = floor((l + r) / 2)
            if self.my_list[mid] < search:
                l = mid + 1
            elif self.my_list[mid] > search:
                r = mid - 1
            elif self.my_list[mid] == search:
                return mid
        return "not found"


    def selection_sort(self):
        for i in range(len(self.my_list)):
            minimum_point = i
            for j in range(i + 1, (len(self.my_list))):
                if self.my_list[minimum_point] > self.my_list[j]:
                    minimum_point = j

            self.my_list[i], self.my_list[minimum_point] = self.my_list[minimum_point], self.my_list[i]
            print(self.my_list)

    def reset_list(self):

        print(self.newlist)


def Level_order(root):
    h = Height(root)  # at a time ek chly gi
    for i in range(1, h + 1):
        level_node_pick(root, i)

def level_node_pick(root, level):
    if root is None:
        return
    if level == 1:
        print((root.data))
    elif level > 1:
        level_node_pick(root.prev, level - 1)
        level_node_pick(root.next, level - 1)


def Height(node):
    if node is None:
        return 0
    else:
        prev_height = Height(node.prev)
        next_height = Height(node.next)
        if prev_height > next_height:
            return prev_height + 1
        else:
            return next_height + 1

i=input(print("Enter t to view the bfs (Inventory Management System)"))
if i=="t" or i=="T":

    root = Node("**Inventory Management System**")
    root.next = Node("Pharmacy")
    root.prev = Node("Grocery")
    root.prev.next = Node("Cosmetics")
    root.prev.prev = Node("Crockery")
    root.next.next = Node("Bakery")
    root.next.prev = Node("Dairy")
    print("\t" + "*BFS*")
    Level_order(root)
else:
    print("Sorry,Worng Input!")

queue = Queue()
print("\t"+"***** Inventory Management System *****")
while True:
    myinput=int(input(print("\n"+"Press 1 -- VIEW COMPLETE LIST"
                            +"\n"+"Press 2 -- TO VIEW FIRST ELEMENT "
                            +"\n"+"Press 3 -- TO VIEW LIST SIZE "
                            +"\n"+"Press 4 -- TO VIEW WHETHER THE LIST IS EMPTY (T/F) "
                            +"\n"+"Press 5 -- TO SEARCH AN ELEMENT "
                            +"\n"+"Press 6 -- TO APPLY SORT "
                            +"\n"+"Press 7 -- TO VIEW LIST AFTER (1x) DEQUEUE  "
                            +"\n"+"Press 8 -- TO Enqueue "
                            +"\n"+"Press 9 -- For Reset "
                            + "\n"+"Press 0 -- TO EXIT ")))
    if myinput==1:
        print("***Queue AND ITS OPERATIONS using doubly linked list***"+"\n")
        #queue.enqueue("DAIRY*")
        #queue.enqueue("COSMETICS*")
        #queue.enqueue("GROCERY*")
        #queue.enqueue("BEVERAGES*")
        #queue.enqueue("PHARMACY*")
        #queue.enqueue("BAKERY*")
        #queue.enqueue("FRUITS*")
        #queue.enqueue("CROCKERY*")
        queue.printqueue()
    elif myinput==2:
        print("\nFirst element is:", queue.first())
    elif myinput==3:
        print("Size of queue is:", queue.size())
    elif myinput==7:
        element = int(input(print("How many elements wanna dequeue ?")))
        for x in range(element):
            queue.dequeue()
    elif myinput==4:
        print("\nQueue is empty:", queue.isEmpty())
    elif myinput==5:
        entert = int(input(print("\n" + "Press-1 for linear-search  " + "\n" + "Press-2 for binary search ")))
        print("====SEARCH HERE====")
        search_item=input("Enter element to search")
        if entert==1:
            queue.serach(search_item)
        elif entert==2:
            if (queue.binary_Search(search_item)== None):
                print("Value not present")
            else:
                print("Present")
    elif myinput==6:
        enter=int(input(print("\n"+"Press-1 for bubble sort "+"\n"+"Press-2 for insertion sort "+"\n"+"Press-3 for selection sort"+"\n"+"Press-4 for merge sort ")))
        if enter==1:
            print("\n")
            print("\t"+"Before Bubble sort")
            queue.printqueue()
            print("\n")
            print("\t"+"After Bubble sort")
            queue.bubble_Sort()
            queue.printqueue()
            print("\n")
        elif enter==2:
            print("\n")
            print("\t"+"Before insertion sort")
            queue.printqueue()
            print("\n")
            print("\t"+"After insertion sort")
            queue.insertion_sort()
        elif enter==3:
            print("\n")
            print("\t"+"Before selection sort")
            queue.printqueue()
            print("\n")
            print("\t"+"After selection sort")
            queue.selectiosort()
        elif enter==4:
            print("\n")
            print("\t"+"Before merge sort")
            queue.printqueue()
            print("\n")
            print("\t"+"After merge sort")
            queue.head=queue.mergeSort(queue.head)
            queue.printList(queue.head)

    elif myinput==8:
        element=int(input(print("How many elements wanna enter ?")))
        for x in range(element):
            queue.enqueue(input(print("Enter element to Push in list --- : ")))
        #queue.printqueue()
    elif myinput==0:
        break

    elif myinput==9:
        queue.reset_list()

    else:
        print("Invalid input")
        if myinput>9:
            break


