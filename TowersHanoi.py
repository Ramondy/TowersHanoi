from stack import Stack


def create_board():
    '''
    :return: a list of three stacks
    '''
    left_stack, middle_stack, right_stack = Stack("Left"), Stack("Middle"), Stack("Right")
    return [left_stack, middle_stack, right_stack]


def create_choices():
    '''
    :return: a list of stack name initials
    '''
    return [e.get_initial() for e in stack_board]


def initialize_disks(min_disks=3):
    '''
    input the number of disks to play with, set the disks on Stack "Left", calculate optimal solution
    :param min_disks: int, minimum number of disks to play with, set to 3
    :return: None
    '''
    global num_optimal_moves
    global num_disks

    while num_disks < min_disks:
        num_disks = int(
            input("\nHow many disks? Enter a number greater than or equal to {0}.\n"
                  .format(min_disks)))

    for i in range(num_disks, 0, -1):
        stack_board[0].push(i)

    num_optimal_moves = 2 ** num_disks - 1
    print("\nThe fastest you can solve this game is in {0} moves. Good luck!".format(num_optimal_moves))
    return


def select_stack(user_input):
    '''
    select a stack based on user input
    :param user_input: char, initial stack.name
    :return: corresponding stack
    '''
    for e in stack_board:
        if e.get_initial() == user_input:
            return e


def get_user_input():
    '''
    guides user for data entry, capture user's next move
    :return: corresponding stack, using select_stack()
    '''
    while True:
        print("Enter: ", end="")
        for i in range(len(choices)):
            print("<{0} for {1}>".format(choices[i], stack_board[i].get_name()), end="\t\t")
        user_input = input("")
        if user_input in choices:
            return select_stack(user_input)


def check_move_validity(from_, to_):
    '''
    verifies legality of user's next move
    :param from_: stack
    :param to_: stack
    :return: bool
    '''
    if from_.is_empty() or not to_.has_space() or from_.peek() > to_.peek():
        return False
    else:
        return True


def record_move(from_, to_):
    '''
    keep a trace of all moves
    :param from_: stack
    :param to_: stack
    :return: list of strings
    '''
    global record
    record.append("{0} -> {1}".format(from_, to_))


def implement_move(from_, to_):
    '''
    implement a move (=move a disk) once declared legal
    :param from_: stack
    :param to_: stack
    :return: None
    '''
    global num_user_moves

    disk = from_.pop()
    to_.push(disk)
    num_user_moves += 1
    if player == "H":
        print("Played from {0} to {1}".format(from_, to_))


def determine_transit_loc(from_, to_):
    '''
    determine transit location for recursive implementation of play_as_computer
    :param from_: stack
    :param to_: stack
    :return: stack
    '''
    temp = choices[:]
    temp.remove(from_)
    temp.remove(to_)
    return temp.pop()


def play_as_computer(num_, from_, to_):
    '''
    recursive algorithm to solve optimally the Hanoi Tower problem
    :param num_: number of disks in play
    :param from_: stack
    :param to_: stack
    :return: None
    '''

    if num_ == 1:
        if check_move_validity(select_stack(from_), select_stack(to_)):
            implement_move(select_stack(from_), select_stack(to_))
            record_move(select_stack(from_), select_stack(to_))
        else:
            # will only run if there is an error in algorithm implementation
            print("Algo error!")

    else:
        transit_loc = determine_transit_loc(from_, to_)

        play_as_computer(num_ - 1, from_, transit_loc)
        play_as_computer(1, from_, to_)
        play_as_computer(num_ - 1, transit_loc, to_)


def finish_game():
    '''
    print final messages when game is won
    :return: None
    '''
    print("\n")
    if num_user_moves == num_optimal_moves:
        print("CONGRATULATIONS!")
    print("You completed the game in {0} moves, and the optimal number of moves is {1}.".
          format(num_user_moves, num_optimal_moves))
    if num_user_moves < 50:
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
    initialize_disks()

    player = ""
    while player not in ["H", "C"]:
        player = input("\nWho is playing? Human (H) or Computer (C)?")

    if player == "H":
        while stack_board[-1].get_size() != num_disks:
            print("\n...Current Stacks...")
            for stack in stack_board:
                stack.print_items()
            print("Moves used: " + str(num_user_moves))

            while True:
                print("\nWhich stack do you want to move from?")
                from_stack = get_user_input()
                print("\nWhich stack do you want to move to?")
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
