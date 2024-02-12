class student:
     # Constructor to initialize attributes
    def __init__(self, name, course, year):
        self.name = name
        self.course = course
        self.year = year

     # Method to display information
    def display_info(self):
        print(f"Name: {self.name}, Course: {self.course}, Year: {self.year}")
    
students = []
num = int(input("Enter the number of students: "))

for i in range(num):
    print(f"\nEnter details for Student {i + 1}:")
    name = input("Enter name: ")
    course = input("Enter course: ")
    year = int(input("Enter year: "))

 # Create a Student object with the provided information and add it to the list
    pupil = student(name, course, year)
    students.append(pupil)

# Display information for all students
print("\nInformation for all students:")
for student in students:
    student.display_info()