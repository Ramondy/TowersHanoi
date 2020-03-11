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
    global choices
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

    # create the stack_board as list of 3 Stacks
    stack_board = create_board()
    choices = create_choices()
    # chose number of disks, place disks in left stack:
    initialize_disks()
    num_on_goal = stack_board[-1].get_size()

    player = ""
    while player not in ["h", "c"]:
        player = input("\nWho is playing? Human (h) or Computer (c) ?")

    if player == "h":

        #PLAY THE GAME
        while num_on_goal != num_disks:
            print("\n...Current Stacks...")
            for stack in stack_board:
                stack.print_items()

            while True:
                print("\nWhich stack do you want to move from?\n")
                from_stack = get_user_input()
                print("\nWhich stack do you want to move to?\n")
                to_stack = get_user_input()
                if from_stack.is_empty() or not to_stack.has_space() or from_stack.peek() > to_stack.peek():
                    print("\nInvalid Move. Try Again")
                    continue
                else:
                    disk = from_stack.pop()
                    to_stack.push(disk)
                    num_user_moves += 1
                    break

        if num_user_moves == num_optimal_moves:
            print("\nCONGRATULATIONS!")
        print("\nYou completed the game in {0} moves, and the optimal number of moves is {1}.".
              format(num_user_moves, num_optimal_moves))

    if player == "c":

        play_as_computer()


        pass

def play_as_computer():

    global stack_board
    global num_disks
    global num_on_goal

    even_play = (num_disks % 2 == 0)
    num_at_play = 1 - num_on_goal

    while num_on_goal != num_disks:
        if even_play:
        else:
