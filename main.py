import BinaryTree as bt

# Q1: Write an efficient program for printing k largest elements in an array.
# Elements in array can be in any order.

# Q2: Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a^2 + b^2 = c^2

# Q3: Convert a given Binary Tree to a Doubly Linked List

# Q4: Given a binary tree (not a binary search tree) and two values say n1 and n2,
# write a program to find the least common ancestor.

# Q5: Design a Data Structure SpecialStack that supports all the stack operations like push(), pop(), isEmpty(), isFull()
# and an additional operation getMin() which should return the minimum element from the SpecialStack.
# All these operations of SpecialStack must be O(1). To implement SpecialStack, you should only use standard Stack data structure
# and no other data structure like arrays, list, etc...

# Q6: Given a linked list, write a function to reverse every k nodes (where k is an input to the function).

# Q7: Given two numbers represented by two lists, write a function that returns sum list.
# The sum list is list representation of two input numbers.

# Q8: Given a square matrix, turn it by 90 degrees in an anti-clockwise direction without using any extra space.

# Q9: The stock span problem is a financial problem where we have a series of n daily price quotes for a stock
# and we need to calculate the span of a stock's price for all n days.
# The span Si of the stock's price on a given day i is defined as the maximum number of consecutive days just before the given day,
# for which the price of the stock on the current day is less than or equal to its price on the given day.

binary_tree = bt.create_binary_tree([1, 2, 3, 4, 5, 6, 7])
print(binary_tree.get_preorder_list())
print(binary_tree.get_inorder_list())
print(binary_tree.get_postorder_list())