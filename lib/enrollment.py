from datetime import datetime
class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()
    def course_count(self):
        return len(self._enrollments)
    
    def set_grade(self, enrollment, grade):
        if enrollment in self._enrollments:
            self._grades[enrollment] = grade
        else:
            raise ValueError("Enrollment not found for this student")

    def aggregate_average_grade(self):
        if not self._grades:
            return None  # or return 0.0
        total = sum(self._grades.values())
        return total / len(self._grades)

    def __repr__(self):
        return f"Student({self.name})"
    

class Course:
    def __init__(self, title):

        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()
    
    def student_count(self):
        return len(self._enrollments)

    def get_students(self):
        return [enrollment.student for enrollment in self._enrollments]

    def __repr__(self):
        return f"Course({self.title})"


class Enrollment:
    all = []
    
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date
    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count

    def __repr__(self):
        return f"Enrollment({self.student.name}, {self.course.title})"
