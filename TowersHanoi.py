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


def select_stack(user_input):
    for e in stack_board:
        if e.get_initial() == user_input:
            return e


def get_user_input():
    while True:
        for i in range(len(choices)):
            print("Enter {0} for {1}".format(choices[i], stack_board[i].get_name()))
        user_input = input("")
        if user_input in choices:
            return select_stack(user_input)


def check_move_validity(from_, to_):
    if from_.is_empty() or not to_.has_space() or from_.peek() > to_.peek():
        return False
    else:
        return True


def record_move(from_, to_):
    global record
    record.append("{0} -> {1}".format(from_, to_))


def implement_move(from_, to_):
    global num_user_moves

    disk = from_.pop()
    to_.push(disk)
    num_user_moves += 1
    if player == "H":
        print("Played from {0} to {1}".format(from_, to_))
    return


def determine_transit_loc(from_, to_):
    temp = choices[:]
    temp.remove(from_)
    temp.remove(to_)
    return temp.pop()


def play_as_computer(num_, from_, to_):

    if num_ == 1:
        if check_move_validity(select_stack(from_), select_stack(to_)):
            implement_move(select_stack(from_), select_stack(to_))
            record_move(select_stack(from_), select_stack(to_))
            return
        else:
            print("Strategy error!")
            return

    else:
        transit_loc = determine_transit_loc(from_, to_)
        #print(num_, transit_loc)

        play_as_computer(num_ - 1, from_, transit_loc)
        play_as_computer(1, from_, to_)
        play_as_computer(num_ - 1, transit_loc, to_)
    return


def finish_game():
    if num_user_moves == num_optimal_moves:
        print("\nCONGRATULATIONS!")
    print("\nYou completed the game in {0} moves, and the optimal number of moves is {1}.".
          format(num_user_moves, num_optimal_moves))
    print("Here is the sequence of moves: ", record)


if __name__ == '__main__':

    num_disks= 0
    num_optimal_moves = 0
    num_user_moves = 0
    record = []

    print("\nLet's play Towers of Hanoi!!")

    # create the stack_board as list of 3 Stacks
    stack_board = create_board()
    choices = create_choices()
    # chose number of disks, place disks in left stack:
    initialize_disks(2)

    player = ""
    while player not in ["H", "C"]:
        player = input("\nWho is playing? Human (H) or Computer (C) ?")

    if player == "H":

        #PLAY THE GAME
        while stack_board[-1].get_size() != num_disks:
            print("\n...Current Stacks...")
            for stack in stack_board:
                stack.print_items()

            while True:
                print("\nWhich stack do you want to move from?\n")
                from_stack = get_user_input()
                print("\nWhich stack do you want to move to?\n")
                to_stack = get_user_input()

                if check_move_validity(from_stack, to_stack):
                    implement_move(from_stack, to_stack)
                    record_move(from_stack, to_stack)
                    break

                if not check_move_validity(from_stack, to_stack):
                    print("\nInvalid Move. Try Again")
                    continue

    if player == "C":

        while stack_board[-1].get_size() != num_disks:
            play_as_computer(num_disks, "L", "R")

    finish_game()



