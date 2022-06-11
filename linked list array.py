class Node:
    def __init__(self, data=None):
        self.data = data
        self.next=None

def rearrange(arr, head):
    dummy = Node("#")

    for i in arr:
        itr = head
        while itr.val!=i:
            itr = itr.next
        dummy.next = itr
        dummy = dummy.next


if __name__ == "__main__":
    head = Node(5)
    head.next = Node(4)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)
    arr = [1,2,3,4,5]

    rearrange(arr, head)