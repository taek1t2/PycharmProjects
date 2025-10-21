programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",

}

print(programming_dictionary["Bug"])

programming_dictionary["string"] = "A value that is wrapped around with double quotation.. Hey look, I made a string!"
print(programming_dictionary)

# empty_dictionary = {}
# To wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# This is the scoring criteria:
#
# - Scores 91 - 100: Grade = "Outstanding"
#
# - Scores 81 - 90: Grade = "Exceeds Expectations"
#
# - Scores 71 - 80: Grade = "Acceptable"
#
# - Scores 70 or lower: Grade = "Fail"

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

# how I coded it originally:
for each_student, scores in student_scores.items():
    if scores >= 91:
        print(each_student, ": Outstanding")
    elif scores >= 81:
        print(each_student, ": Exceeds Expectations")
    elif scores >= 71:
        print(each_student, ": Acceptable")
    else:
        print(each_student, ": Fail")

# another way
for student, score in student_scores.items():
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


