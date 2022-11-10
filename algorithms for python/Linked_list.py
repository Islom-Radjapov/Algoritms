class Node:
    """Tugun (node) obyekt"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LindekList:
    """Linked list obyekti"""
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        """List boshiga yangi element qoshish"""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def inserAfter(self, prev_node, new_data):
        """Biron tugundan so'ng tugun qoshish"""
        if prev_node is None:
            print("Tugun mavjud emas")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append_(self, new_data):
        """List oxiriga element qoshish"""
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        # listni oxirgi elementiga borish sikli
        while last.next:
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        """Listdan elementni ochirish"""
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return
        prev.next = temp.next
        temp = None


llist = LindekList()
llist.head = Node("Dushanba")
tuesday = Node("Seshanba")
wednesday = Node("Chorshanba")

llist.head.next = tuesday
tuesday.next = wednesday

llist.push("Yakshanba")

llist.inserAfter(llist.head.next.next, "Seshanba kechasi")
llist.append_("Juma")
llist.printList()
llist.deleteNode("Seshanba kechasi")
print("- - - - - - - - - - - - - - -")
llist.printList()




"""    
                  Linked listlar 3hil turda boladi
        1. SINGLY Linked list = Bir tomonlami royhat
        2. CICRULAR Linked list = Aylanma royhat
        3. DOUBLE Lindek list = Ikki tomonlami royhat

        Afzalliklari tez yozish va tez o'chirish yana 1 ta operatsiya blan bajariladi O(1)
        Kamchiliklari sekin qidirish va har bir tugun xotiradi koproq joy egallaydi   O(n)
"""
