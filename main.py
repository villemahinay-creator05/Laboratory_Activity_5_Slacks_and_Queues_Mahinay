from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def show_structure(structure):
    print("Current state:", structure.show())


def stack_menu(stack):
    while True:
        print("\nSTACK MENU")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Check if full")
        print("6. Show state")
        print("0. Back")
        choice = input("Choose an operation: ")

        try:
            if choice == "1":
                value = input("Enter value to push: ")
                stack.push(value)
                show_structure(stack)
            elif choice == "2":
                print("Popped value:", stack.pop())
                show_structure(stack)
            elif choice == "3":
                print("Top value:", stack.peek())
            elif choice == "4":
                print("Is empty:", stack.is_empty())
            elif choice == "5":
                print("Is full:", stack.is_full())
            elif choice == "6":
                show_structure(stack)
            elif choice == "0":
                break
            else:
                print("Invalid choice. Try again.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)


def queue_menu(queue):
    while True:
        print("\nQUEUE MENU")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek front")
        print("4. Check if empty")
        print("5. Check if full")
        print("6. Show state")
        print("0. Back")
        choice = input("Choose an operation: ")

        try:
            if choice == "1":
                value = input("Enter value to enqueue: ")
                queue.enqueue(value)
                show_structure(queue)
            elif choice == "2":
                print("Dequeued value:", queue.dequeue())
                show_structure(queue)
            elif choice == "3":
                print("Front value:", queue.peek_front())
            elif choice == "4":
                print("Is empty:", queue.is_empty())
            elif choice == "5":
                print("Is full:", queue.is_full())
            elif choice == "6":
                show_structure(queue)
            elif choice == "0":
                break
            else:
                print("Invalid choice. Try again.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)


def balanced_parentheses(expression):
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}

    for character in expression:
        if character in "([{":
            stack.append(character)
        elif character in ")]}":
            if len(stack) == 0:
                return False
            if stack.pop() != matching[character]:
                return False

    return len(stack) == 0


def parentheses_exercise():
    expression = input("Enter an expression with parentheses: ")
    if balanced_parentheses(expression):
        print("Result: Balanced")
    else:
        print("Result: Not balanced")


def print_queue_exercise():
    jobs = ArrayQueue(10)
    count = int(input("How many print jobs (1-10)? "))

    if count < 1 or count > 10:
        print("Please enter a number from 1 to 10.")
        return

    for i in range(count):
        job_id = input("Enter job ID: ")
        pages = input("Enter number of pages: ")
        jobs.enqueue(job_id + " (" + pages + " pages)")

    print("\nPrint order (FIFO):")
    order = 1
    while not jobs.is_empty():
        print(str(order) + ". Printing " + jobs.dequeue())
        order = order + 1


def main():
    while True:
        print("\n=== STACKS AND QUEUES LAB ===")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Circular Array Queue")
        print("4. Linked Queue")
        print("5. Parentheses Checker")
        print("6. Print Queue Simulation")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            stack_menu(ArrayStack(5))
        elif choice == "2":
            stack_menu(LinkedStack())
        elif choice == "3":
            queue_menu(ArrayQueue(5))
        elif choice == "4":
            queue_menu(LinkedQueue())
        elif choice == "5":
            parentheses_exercise()
        elif choice == "6":
            try:
                print_queue_exercise()
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "0":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
