from person import Person

class Instructor(Person):

    def __init__(self, first_name, last_name, slack_handle, cohort, specialty):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.specialty = specialty

    def assign_exercise(self, exercise, student):
        student.exercises.append(exercise)
