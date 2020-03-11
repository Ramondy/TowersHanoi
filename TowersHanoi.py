from node import Node
from stack import Stack


def create_board():
    left_stack, middle_stack, right_stack = Stack("Left"), Stack("Middle"), Stack("Right")
    return [left_stack, middle_stack, right_stack]


def create_choices():
    global stack_board
    return [e.get_initial() for e in stack_board]


def initialize_disks(min_disks=3):
    global num_disks
    global num_optimal_moves

    while num_disks < min_disks:
        num_disks = int(
            input("\nHow many disks do you want to play with?\nEnter a number greater than or equal to {0}\n"
                  .format(min_disks)))

    for i in range(num_disks, 0, -1):
        stack_board[0].push(i)

    num_optimal_moves = 2 ** num_disks - 1
    print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))
    return


def get_user_input():
    global stack_board
    choices = create_choices()
    while True:
        for i in range(len(choices)):
            print("Enter {0} for {1}".format(choices[i], stack_board[i].get_name()))
        user_input = input("")
        if user_input in choices:
            for e in stack_board:
                if e.get_initial() == user_input:
                    return e


if __name__ == '__main__':

    num_disks= 0
    num_optimal_moves = 0
    num_user_moves = 0

    print("\nLet's play Towers of Hanoi!!")

    #create the stack_board as list of 3 Stacks, chose number of disks, place disks in left stack:
    stack_board = create_board()
    initialize_disks()

    #PLAY THE GAME
    while stack_board[-1].get_size() != num_disks:
        print("\n\n\n...Current Stacks...")
        for stack in stack_board:
            stack.print_items()
            #stack.peek()
        break






    #get_user_input()
    #print(stack_board[0].peek())

    #print(middle_stack.peek())

