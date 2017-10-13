grade1 = int(input("Grade /20: "))
grade2 = int(input("Grade /20: "))

grade_sum = grade1 + grade2
result_scale_100 = (grade_sum * 100 //(2*20))
result_string = "Grade /100 = %i" % result_scale_100
print(result_string)