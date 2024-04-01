from node import Stack

print("_______Tower of Hanoi_______")

stacks = []

num_disks = int(input("\n\n\nEnter a number of disks from 3:\n")) 

left_stack = Stack("Left", num_disks)
middle_stack = Stack("Middle", num_disks)
right_stack = Stack("Right", num_disks)

stacks += [left_stack, middle_stack, right_stack]

while num_disks < 3:
    user_input = int(input("\n\n\nEnter a valid number of disks from 3:\n"))

ideal_moves_num = (2** num_disks) - 1

print("\n\nThe ideal moves for {0} disks are {1}".format(num_disks, ideal_moves_num))

for i in range(len(stacks), 0, -1):
    left_stack.push(i)

def get_input():
    choices = [n.get_name()[0] for n in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            char = name[0]
            print("\nEnter {0} for {1}".format(char, name))
        user_input = input('')
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

num_user_moves = 0
while (right_stack.get_size() != num_disks):
    print("\n\n...Current Stacks...\n")
    for stack in stacks:
        stack.print_items()

    while True:
        print("\nWich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWich stack do you want to move to?\n")
        to_stack = get_input()
        print(to_stack.peek())
        if from_stack.get_size() == 0:
          print("\n\nInvalid Move. Try Again")
        elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
           disk = from_stack.pop()
           to_stack.push(disk)
           num_user_moves += 1
           break
        else:
           print("\n\nInvalid Move. Try Again")
print("\n\nYou completed the game in {} moves, and the optimal number of moves is {}".format(num_user_moves, ideal_moves_num))





