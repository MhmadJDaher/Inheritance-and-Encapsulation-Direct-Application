# Base class: User
class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def get_info(self):
        return f"Name: {self.__name}, Email: {self.__email}"

    def set_email(self, new_email):
        self.__email = new_email


# Subclass: Student
class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__enrolled_courses = []

    def enroll(self, course_name):
        if course_name not in self.__enrolled_courses:
            self.__enrolled_courses.append(course_name)
            print(f"Enrolled in course: {course_name}")
        else:
            print(f"Already enrolled in: {course_name}")

    def get_enrolled_courses(self):
        return self.__enrolled_courses
    

# Subclass: Instructor
class Instructor(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__teaching_courses = []

    def add_course(self, course_name):
        if course_name not in self.__teaching_courses:
            self.__teaching_courses.append(course_name)
            print(f"Added course to teach: {course_name}")
        else:
            print(f"Already teaching: {course_name}")

    def get_teaching_courses(self):
        return self.__teaching_courses