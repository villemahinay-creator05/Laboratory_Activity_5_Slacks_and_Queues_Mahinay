# Analysis: Stacks and Queues

A linked-list stack pushes and pops at the head because the head can be updated directly in constant time, O(1). If we push or pop at the tail of a singly linked list, we may need to travel through the list, which takes O(n) time. An array queue must be circular so that empty spaces at the beginning of the array can be reused after dequeue operations. The circular queue uses the modulo operator (%) to move the front and rear positions back to index 0 when they reach the end. This allows enqueue and dequeue to work in O(1) time.
