# односвязанный список
from dataclasses import dataclass
from typing import Any, Optional
from collections import deque
from heapq import heappush, heappop

# @dataclass
# class Node:
#     val: Any
#     next: Optional["Node"] = None


# c = Node('C')
# b = Node('B', next=c)
# a = Node('A', next=b)


# def print_list(main: Optional[Node]):
#     curr = main
#     while curr.next != None:
#         print(curr.val, end=' -> ')
#         curr = curr.next
#     print(curr.val)

# print_list(a)

#двухсзвязанный список

# @dataclass
# class DoubleNode:
#     val: Any
#     next: Optional["DoubleNode"] = None
#     prev: Optional["DoubleNode"] = None

# a = DoubleNode('Page 1')
# b = DoubleNode('Page 2')
# c = DoubleNode('Page 3')

# a.next = b
# b.prev = a
# b.next = c
# c.prev = b

# print(c.prev.val)
# print(b.prev.val, '<->', b.val, '<->', b.next.val)

# стек

# stack = []
# stack.append('A')
# stack.append('B')
# stack.append('C')



# print(stack)
# print('последний элемент: ', stack[-1])
# print(stack.pop())
# print('последний элемент: ', stack[-1])

# def is_balanced(text: str) -> bool:
#     st = []
#     pair = {')': '(', ']': '[', '}': '{'}
#     for i in text:
#         if i in '({[':
#             st.append(i)
#         elif i in ')}]':
#             if len(st) == 0:
#                 return False
#             top = st.pop()
#             if pair[i] != top:
#                 return False
#     return len(st) == 0

# print(is_balanced('()[]{'))


# очередь

# queue = deque()
# queue.append('A')
# queue.append('B')
# queue.append('C')
# print(queue)
# print(queue.popleft())
# print(queue)

# приоритетная очередь

# q = []
# heappush(q, (3, 'C'))
# heappush(q, (1, "A"))
# heappush(q, (2, 'B'))
# while q:
#     pr, val = heappop(q)
#     print(f'{val} с приоритетом {pr}')

# дерево
@dataclass
class TreeNode:
    val: Any
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

root = TreeNode('A', left=TreeNode('B', left=TreeNode('D'), right=TreeNode('E')), right=TreeNode('C', right=TreeNode('F')))


def preodrer(node: Optional[TreeNode]) -> None:
    if node == None:
        return
    print(node.val)
    preodrer(node.left)
    preodrer(node.right)

preodrer(root)