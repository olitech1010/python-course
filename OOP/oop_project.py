class Student:
    def __init__(self, first_name, last_name, course, score):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.score = score

    def set_details(self, first_name=None, last_name=None, course=None, score=None):
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if course is not None:
            self.course = course
        if score is not None:
            self.score = score

    def get_detials(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "course": self.course,
            "score": self.score,
    
        }
        

Student = Student(first_name="Haggith",last_name="Ama", course="Psychology", score=89)
Student.set_details(score=96)
print(Student.get_detials())
