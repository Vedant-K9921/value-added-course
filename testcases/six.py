#check linked liest is palin
def is_palindrome(head):
    if not head or not head.next:
        return True

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = reverse_list(slow)
    first = head

    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True