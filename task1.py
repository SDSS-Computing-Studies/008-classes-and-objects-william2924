#! python3
"""
(10 points) 
Create a class object for a student.
It should have the following properties
str name
str studentNumber
int grade
list courses - to corresepond with course names
list grades - to correspond with grades

It should have the following methods:
average()       - determines the mathematical average of all course grades
getHonorRoll()  - determines the average of the top 5 courses if there are at least 5 courses.
                  returns True if the average is 86 or higher (on the honor roll)
                  returns False if not on the honor roll
showCourses()   - prints a list of all courses
showGrade(int)  - takes 1 parameter, the index of the list
                - displays the course name and grade
getCourses(list)- Receives a list of courses and stores that in the class property
getGrades(list) - Receives a list of grades and stores that in the class property
constructor     - should require the student name, studentNumber and grade (in that order)
"""

class student:
    name = ""
    studentNumber = ""
    grade = 0
    courses = []
    grade = []

    # properties should be listed first

    def __init__(self, name, studentNumber, grade): 
        # You will need to create your own input parameters for all methods
        name = input(str(name()))
        grade = input(str(grade()))
        self.name = name
        slef.grade = grade


    def average(self):
        sum = 0

        return average

    def getHonorRoll(self):
        s = slef.grade
        s.sort(reverse = True)
        sum = 0

    def getGrades(self, l):
        for i in l:
            self.grade.append()