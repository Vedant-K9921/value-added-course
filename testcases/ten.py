def sort_list(head):
    if not head or not head.next:
        return head

    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    left = sort_list(head)
    right = sort_list(second)

    return merge_two_lists(left, right)