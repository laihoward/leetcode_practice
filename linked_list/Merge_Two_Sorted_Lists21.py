class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        printList = ListNode(-1)
        new_list=printList 
        while l1 and l2:
            if l1.val <= l2.val: #寫成>= 
                new_list.next = ListNode(l1.val)
                l1 = l1.next
                new_list = new_list.next #一開始沒有加 導致最後輸出只有一個NODE
            else:
                new_list.next =ListNode(l2.val) 
                l2 = l2.next
                new_list = new_list.next
        while l1:
            new_list.next = ListNode(l1.val)
            l1 = l1.next
            new_list = new_list.next
        while l2:
            new_list.next = ListNode(l2.val)
            l2 = l2.next
            new_list = new_list.next
        return printList.next