def reverse_k_group(head, k):
    if k <= 0:
        raise ValueError("k must be positive")

    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth = group_prev

        for _ in range(k):
            kth = kth.next
            if kth is None:
                return dummy.next

        group_next = kth.next
        prev = group_next
        current = group_prev.next

        while current is not group_next:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        old_group_head = group_prev.next
        group_prev.next = kth
        group_prev = old_group_head