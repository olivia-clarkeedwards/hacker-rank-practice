'''

Description: Merges two sorted linked lists.
Author: Olivia Clarke-Edwards

'''

#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node):
    while node:
        print(str(node.data))

        node = node.next

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    mergedList = SinglyLinkedList()
    currentNode1 = head1
    currentNode2 = head2

    while currentNode1 is not None or currentNode2 is not None:
        if currentNode1 is None:
            mergedList.insert_node(currentNode2.data)
            currentNode2 = currentNode2.next
        elif currentNode2 is None:
            mergedList.insert_node(currentNode1.data)
            currentNode1 = currentNode1.next
        else:
            if currentNode1.data > currentNode2.data:
                mergedList.insert_node(currentNode2.data)
                currentNode2 = currentNode2.next
            else:
                mergedList.insert_node(currentNode1.data)
                currentNode1 = currentNode1.next
                

    return mergedList


def main():
    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3.head)

main()