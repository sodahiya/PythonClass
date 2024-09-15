
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head=[1,2,3,4,5]
k = 2

if not head or not head.next or k == 0:
    print( head)

        # Step 1: Compute the length of the list
length = 1
current = head
while current.next:
    current = current.next
    length += 1

        # Step 2: Make the list circular
current.next = head

        # Step 3: Find the new head
k = k % length  # In case k is greater than the length
steps_to_new_head = length - k
new_tail = head

for _ in range(steps_to_new_head - 1):
    new_tail = new_tail.next

new_head = new_tail.next

        # Step 4: Break the circular list
new_tail.next = None

print(new_head)