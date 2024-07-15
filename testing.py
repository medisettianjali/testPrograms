classesHeld=int(input("Enter no.of classes held:"))
classesAttended=int(input("Enter no.of classes attended:"))
percentage=(classesAttended/classesHeld)*100
print(percentage)
if percentage>75:
    print("Student is allowed for exam")
else:
    print("Student is not allowed for exam")
