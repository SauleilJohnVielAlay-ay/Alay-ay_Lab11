grade = 1
passed = 0
list = []
student_num = 1
add_grade = 0
while grade != 0:
    grade = int(input(f"Enter Grade of Student {student_num} : "))
    if grade < 40 or grade > 100:
        print("Invalid Grade")
        break
    else:
        list.append(grade)
        student_num += 1
        if grade >= 75:
         passed += 1
    add_grade = input("Do you want to add another grade? (yes/done): ")
    
    if (add_grade.lower() == "yess"):
        continue
    elif (add_grade.lower() == "done"):
        list_sum = sum(list)
        ave = (list_sum / len(list))
        ave = round(ave, 2)
        passing = (passed/len(list)*100)
        passing = round(passing,2)
        
        print(f"Average Grade: {ave:.2f}")
        print(f"No. of Students Passed: {passed}%")
        print(f"Passing% {passing:.2f}")
        
        break
    else:
        print("Error: Invalid Quote")
        break