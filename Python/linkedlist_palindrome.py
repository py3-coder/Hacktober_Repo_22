class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def checkPalindrome(left, right):
    if right is None:
        return True, left

    val, left = checkPalindrome(left, right.next)
    result = val and (left.data == right.data)
    left = left.next

    return result, left

def checkPalin(head):
    return checkPalindrome(head, head)[0]


if __name__ == '__main__':
    keys = [1, 3, 4, 3, 1]

    head = None
    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)

    if checkPalin(head):
        print("Linked list is Palindrome")
    else:
        print("Linked list is not Palindrome")
