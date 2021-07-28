class Solution(object):
    def hasCycle(self, head):
        oneStep =twoStep = head
        while twoStep and twoStep.next:
            twoStep = twoStep.next.next
            oneStep = oneStep.next
            if oneStep == twoStep:
                return True
        return False