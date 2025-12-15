class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __str__(self): 
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)
    
    def get_middle(self):
        slow = self.head
        fast = self.head
        if self.head is None:
            return self.head
        while (fast.next is not None) and (fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return
        middle = self.get_middle()
        right_head = middle.next
        middle.next = None

        left_list = LinkedList()
        left_list.head = self.head
        right_list = LinkedList()
        right_list.head = right_head

        left_list.merge_sort()
        right_list.merge_sort()

        self.head = merge_two_sorted_llists(left_list, right_list)
        return self.head



        



def merge_two_sorted_llists(linked_list_1, linked_list_2):
    llh_1 = linked_list_1.head
    llh_2 = linked_list_2.head

    if llh_1 == None:
        return llh_2
    if llh_2 == None:
        return llh_1
    
    if llh_1.data < llh_2.data:
        result_head = llh_1
        tail = llh_1
        llh_1 = llh_1.next
    else:
        result_head = llh_2
        tail = llh_2
        llh_2 = llh_2.next


    while llh_1 and llh_2:
        if llh_1.data < llh_2.data:
            picked = llh_1
            llh_1 = llh_1.next
        else:
            picked = llh_2
            llh_2 = llh_2.next
        tail.next = picked
        tail = picked
    if llh_1:
        tail.next = llh_1
    elif llh_2:
        tail.next = llh_2
    
    return result_head
            



llist_1 = LinkedList()
llist_1.insert_at_end(1)
llist_1.insert_at_end(3)
llist_1.insert_at_end(5)

llist_2 = LinkedList()
llist_2.insert_at_end(2)
llist_2.insert_at_end(4)
llist_2.insert_at_end(6)

llist_3 = LinkedList()
llist_3.insert_at_end(4)
llist_3.insert_at_end(2)
llist_3.insert_at_end(5)
llist_3.insert_at_end(1)
llist_3.insert_at_end(3)


merged_list = LinkedList()
merged_list.head = merge_two_sorted_llists(llist_1, llist_2)
print("Змержені два linked lists:")
print(merged_list)

print("Відсортований список")
llist_3.merge_sort()
print(llist_3)



