monkey = input("Enter the position of the monkey: ")
banana = input("Enter the position of the banana: ")
roof = int(input("Is the banana hanging to ceiling (0/1): "))

box = ''
if(roof):
    box = input("Enter the initial position of the box: ")

climb = 0
if(monkey == box):
    climb =  int(input("Since monkey and box are in same position, Is the monkey on the box (0-No, 1-Yes): "))

print('\nsteps:')
i = 0

if(roof==0):
    i+=1
    print("Step-{}: Monkey goes from {} to {}".format(i,monkey,banana))
    i+=1
    print("Step-{}: Monkey grabs banana.... Mission done!".format(i))
else:
    if(climb and box != banana):
        i+=1
        print("Step-{}: Monkey gets down from the box".format(i))
        climb = 0
    if(monkey != box and box != banana):
        i+=1
        print("Step-{}: Monkey goes from {} to {}".format(i,monkey,box))
        monkey = box
    if(monkey == box and box != banana):
        i+=1
        print("Step-{}: Monkey pushes box from {} to {}".format(i,box,banana))
        monkey = banana
        box = banana
    if(monkey == box and box == banana and climb==0):
        i+=1
        print("Step-{}: Monkey climbs box".format(i))  
        climb = 1
    if(climb == 1 and box == banana):
        i+=1
        print("Step-{}: Monkey grabs banana.... Mission done!".format(i))
