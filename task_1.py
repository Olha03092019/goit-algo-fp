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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, "-->", end="")
            current = current.next
        print('None')

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        # знайти середину листа
        mid = self.get_middle(head)
        # розділити лист на дві частини
        right_half = mid.next
        mid.next = None
        left_half = head

        left_sorted = self.merge_sort(left_half)
        right_sorted = self.merge_sort(right_half)

        return self.merge(left_sorted,right_sorted)

    def merge(self,left, right):
        dummy = Node()
        merged = dummy

        while left is not None and  right is not None:
            if left.data <= right.data:
                merged.next=left
                left = left.next
            else:
                merged.next = right
                right = right.next
            merged=merged.next

        if left is not None:
            merged.next = left

        if right is not None:
            merged.next = right

        return dummy.next

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_sorted_lists(self, list1, list2):
        dummy = Node()
        result = dummy
        current_1 = list1.head
        current_2 = list2.head

       # поки обидва списки не порожні:
        while current_1 is not None and current_2 is not None:
            # беремо менший елемент
            if current_1.data <= current_2.data:
                result.next = current_1
                # рухаємо відповідний вказівник
                current_1=current_1.next
            else:
                result.next = current_2
                current_2 = current_2.next
            result = result.next
        # додаємо залишок одного зі списків
        if current_1 is not None:
            result.next = current_1

        if current_2 is not None:
            result.next = current_2

        merged = LinkedList()
        merged.head = dummy.next

        return merged

if __name__ == '__main__':
    first_list = LinkedList()
    first_list.insert_at_beginning(25)
    first_list.insert_at_beginning(20)
    first_list.insert_at_beginning(15)
    first_list.insert_at_beginning(10)
    first_list.insert_at_beginning(5)

    print("Зв'язний список: ")
    first_list.print_list()

    first_list.reverse()
    print("Зв'язний список після реверсування: ")
    first_list.print_list()

    first_list.head = first_list.merge_sort(first_list.head)
    print("Зв'язний список відсортовано: ")
    first_list.print_list()

    second_list = LinkedList()
    second_list.insert_at_beginning(59)
    second_list.insert_at_beginning(35)
    second_list.insert_at_beginning(20)

    merged_list = first_list.merge_sorted_lists(first_list, second_list)
    print("Зв'язний список відсортовано та замерджено: ")
    merged_list.print_list()
