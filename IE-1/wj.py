max1 = int(input("Enter bigger jug max capacity :"))
max2 = int(input("Enter smaller jug max capacity :"))
tar = int(input("Enter the target volume :"))

def pour(jug1,jug2,rule):
    print("%d\t%d\t%s"%(jug1,jug2,rule))
    if jug1 == tar :
        print("%d\t%d\tGoal State"%(jug1,0))
    elif jug2 == tar :
        print("%d\t%d\tGoal State"%(0,jug2))
    elif jug1 == max1 :
        pour(jug1-(max2-jug2),max2,"Pour some water from jug1 to jug2")
    elif jug1 == 0 and jug2 != 0:
        pour(jug2,0,"pour all water from jug2 to jug1")
    elif jug2<max2 :
        pour(jug1,max2,"Fill jug2")
    elif jug1+jug2 < max1 :
        pour(jug1+jug2,0,"Pour water from jug2 to jug1")
    else :
        pour((max1-jug2)+jug1,  jug2-(max1-jug1),"Pour water from jug2 to jug1")

if(tar%(max1-max2)==0 and tar<=max1):
    print("\nSolution found !!")
    print("JUG1\tJUG2\tRule")
    pour(0,0,"Initial State")
else:
    print("\nNo Solution found !!")