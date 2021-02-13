#prompt questions about the the size of the area being carpeted
length = eval(input("What is the length of the room you are trying to carpetin in ft?: "))
width = eval(input("What is the width of the room you're trying to carpet in ft?: "))
print("\nGrade quailty of the carpet can be determined by 1 for good, 2 for better, 3 for the best carpet available!")
type_c = eval(input('\nEnter a number now for grade quailty choice: '))

#math to price match grade quality
total_cost = ((length * width) * 4)
total_cost2 = ((length * width) * 6)
total_cost3 = ((length * width) * 9)

#If statements and print price to carpet
if type_c <2:
print('\nThe Price to carpet this room will be $', int(total_cost))

elif type_c <3:
print('\nThe Price to carpet this room will bw $', int(total_cost2))

elif type_c >1:
print('\nThe Price to carpet this room will be $', int(total_cost3))
#you may run into an indent block shift+tab will fix this problem or manual space
