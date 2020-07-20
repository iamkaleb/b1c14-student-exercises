from person import Person

class Student(Person):

    def __init__(self, first_name, last_name, slack_handle, cohort):
        super().__init__(first_name, last_name, slack_handle, cohort)
        self.exercises = list()